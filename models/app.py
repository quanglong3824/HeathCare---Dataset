import streamlit as st
import pandas as pd
import joblib
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the preprocessor and the model using joblib
try:
    preprocessor = joblib.load(os.path.join(current_dir, 'preprocessor.pkl'))
    model = joblib.load(os.path.join(current_dir, 'moHinhDotQuy_final.pkl'))
except Exception as e:
    st.error(f"Lỗi khi tải mô hình: {e}")
    st.stop()

st.title('Dự đoán nguy cơ đột quỵ')

# Hàm tính BMI từ chiều cao và cân nặng
def tinh_BMI(chieu_cao_cm, can_nang_kg):
    """
    Tính chỉ số BMI từ chiều cao (cm) và cân nặng (kg)
    BMI = cân nặng (kg) / (chiều cao (m))^2
    """
    chieu_cao_m = chieu_cao_cm / 100  # Chuyển đổi từ cm sang m
    bmi = can_nang_kg / (chieu_cao_m ** 2)
    return round(bmi, 2)

# Hàm tính đường huyết trung bình
def tinh_duong_huyet_tb(duong_huyet_ac, duong_huyet_sau_an):
    """
    Tính đường huyết trung bình từ đường huyết lúc đói và sau ăn
    """
    duong_huyet_tb = (duong_huyet_ac + duong_huyet_sau_an) / 2
    return round(duong_huyet_tb, 2)

# Create the user interface to get patient data
gender = st.selectbox('Giới tính', ['Male', 'Female', 'Other'])
age = st.number_input('Tuổi', min_value=0, max_value=120, value=50)
hypertension = st.selectbox('Tăng huyết áp', [0, 1])
heart_disease = st.selectbox('Bệnh tim', [0, 1])
ever_married = st.selectbox('Đã từng kết hôn', ['No', 'Yes'])
work_type = st.selectbox('Loại công việc', ['Self-employed', 'Govt_job', 'Never_worked', 'Private', 'children'])
Residence_type = st.selectbox('Loại hình cư trú', ['Rural', 'Urban'])

# Thêm các trường nhập liệu mới cho BMI
st.subheader('Thông tin cơ thể')
col1, col2 = st.columns(2)
with col1:
    chieu_cao = st.number_input('Chiều cao (cm)', min_value=50.0, max_value=250.0, value=170.0)
    can_nang = st.number_input('Cân nặng (kg)', min_value=10.0, max_value=300.0, value=70.0)

with col2:
    # Tính BMI tự động
    bmi_tu_dong = tinh_BMI(chieu_cao, can_nang)
    st.write(f'**BMI tự động tính:** {bmi_tu_dong}')
    # Cho phép người dùng nhập BMI thủ công hoặc sử dụng BMI tự động
    bmi = st.number_input('Chỉ số BMI (có thể chỉnh sửa)', min_value=0.0, value=float(bmi_tu_dong))

# Thêm các trường nhập liệu cho đường huyết
st.subheader('Thông tin đường huyết')
col3, col4 = st.columns(2)
with col3:
    duong_huyet_ac = st.number_input('Đường huyết lúc đói (mg/dL)', min_value=0.0, value=90.0)
    duong_huyet_sau_an = st.number_input('Đường huyết sau ăn (mg/dL)', min_value=0.0, value=120.0)

with col4:
    # Tính đường huyết trung bình tự động
    duong_huyet_tb_tu_dong = tinh_duong_huyet_tb(duong_huyet_ac, duong_huyet_sau_an)
    st.write(f'**Đường huyết TB tự động:** {duong_huyet_tb_tu_dong} mg/dL')
    # Cho phép người dùng nhập đường huyết thủ công hoặc sử dụng giá trị tự động
    avg_glucose_level = st.number_input('Mức đường huyết trung bình (có thể chỉnh sửa)', min_value=0.0, value=float(duong_huyet_tb_tu_dong))

smoking_status = st.selectbox('Tình trạng hút thuốc', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

# Create a button to make a prediction
if st.button('Dự đoán'):
    # Feature engineering functions (same as in training)
    def phanLoaiTuoi(tuoi):
        if tuoi < 18: return 'treEm'
        elif tuoi < 30: return 'tuoiTre'
        elif tuoi < 50: return 'trungNien'
        elif tuoi < 65: return 'truocTuoiHuu'
        else: return 'tuoiCao'

    def phanLoaiBMI(bmi):
        # Tiêu chuẩn BMI cho người châu Á (WHO Asian BMI cut-offs)
        if bmi < 18.5: return 'thieuCan'
        elif bmi < 23: return 'binhThuong'  # Giảm từ 25 xuống 23
        elif bmi < 27.5: return 'thua Can'  # Giảm từ 30 xuống 27.5
        else: return 'beoPhi'  # ≥27.5 thay vì ≥30

    def phanLoaiGlucose(glucose):
        # Tiêu chuẩn đường huyết cho người châu Á (dựa trên nghiên cứu Asian populations)
        if glucose < 100: return 'binhThuong'
        elif glucose < 110: return 'tienTieuDuong'  # Giảm từ 126 xuống 110 cho người châu Á
        else: return 'tieuDuong'

    # Create engineered features
    nhomTuoi = phanLoaiTuoi(age)
    nhomBMI = phanLoaiBMI(bmi)
    nhomGlucose = phanLoaiGlucose(avg_glucose_level)
    
    # Calculate risk score - Điều chỉnh theo tiêu chuẩn châu Á
    diemNguyCo = (
        hypertension +
        heart_disease +
        (1 if age > 65 else 0) +
        (1 if bmi > 27.5 else 0) +  # Giảm từ 30 xuống 27.5 cho người châu Á
        (1 if avg_glucose_level > 110 else 0)  # Giảm từ 126 xuống 110 cho người châu Á
    )

    # Create a dataframe from the user's input with all required features
    input_data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type],
        'Residence_type': [Residence_type],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status],
        'nhomTuoi': [nhomTuoi],
        'nhomBMI': [nhomBMI],
        'nhomGlucose': [nhomGlucose],
        'diemNguyCo': [diemNguyCo]
    })

    # Preprocess the input data
    input_processed = preprocessor.transform(input_data)

    # Make a prediction
    prediction = model.predict(input_processed)
    prediction_proba = model.predict_proba(input_processed)

    # Hiển thị kết quả dưới dạng tỉ trọng xác suất
    st.subheader('🎯 Kết quả dự đoán')
    
    # Tính toán tỉ trọng xác suất
    xac_suat_khong_dot_quy = prediction_proba[0][0]
    xac_suat_dot_quy = prediction_proba[0][1]
    
    # Hiển thị bằng progress bar
    col_result1, col_result2 = st.columns(2)
    
    with col_result1:
        st.metric(
            label="🟢 Không có nguy cơ đột quỵ",
            value=f"{xac_suat_khong_dot_quy:.1%}",
            delta=None
        )
        st.progress(xac_suat_khong_dot_quy)
    
    with col_result2:
        st.metric(
            label="🔴 Có nguy cơ đột quỵ", 
            value=f"{xac_suat_dot_quy:.1%}",
            delta=None
        )
        st.progress(xac_suat_dot_quy)
    
    # Hiển thị kết luận chính
    if prediction[0] == 1:
        st.error(f'⚠️ **CẢNH BÁO**: Bệnh nhân có nguy cơ cao bị đột quỵ!')
        st.write(f'📊 **Tỉ trọng xác suất đột quỵ**: {xac_suat_dot_quy:.1%}')
        
        # Đưa ra lời khuyên
        st.info("""
        **💡 Khuyến nghị:**
        - Tham khảo ý kiến bác sĩ chuyên khoa ngay lập tức
        - Kiểm soát các yếu tố nguy cơ (huyết áp, đường huyết, BMI)
        - Duy trì lối sống lành mạnh và tập thể dục đều đặn
        """)
    else:
        st.success(f'✅ **KẾT QUẢ TỐT**: Bệnh nhân có nguy cơ thấp bị đột quỵ!')
        st.write(f'📊 **Tỉ trọng xác suất an toàn**: {xac_suat_khong_dot_quy:.1%}')
        
        # Đưa ra lời khuyên
        st.info("""
        **💡 Khuyến nghị:**
        - Tiếp tục duy trì lối sống lành mạnh
        - Kiểm tra sức khỏe định kỳ
        - Theo dõi các chỉ số sức khỏe quan trọng
        """)
    
    # Hiển thị biểu đồ tỉ trọng
    st.subheader('📈 Biểu đồ tỉ trọng xác suất')
    chart_data = pd.DataFrame({
        'Kết quả': ['Không đột quỵ', 'Có đột quỵ'],
        'Xác suất': [xac_suat_khong_dot_quy, xac_suat_dot_quy]
    })
    st.bar_chart(chart_data.set_index('Kết quả'))
    
    # Hiển thị thông tin bổ sung
    with st.expander("📋 Thông tin chi tiết về dự đoán"):
        st.write("**Các yếu tố đã được phân tích:**")
        st.write(f"- Nhóm tuổi: {nhomTuoi}")
        st.write(f"- Nhóm BMI: {nhomBMI}")  
        st.write(f"- Nhóm đường huyết: {nhomGlucose}")
        st.write(f"- Điểm nguy cơ tổng hợp: {diemNguyCo}/5")
        st.write(f"- BMI được tính từ: Chiều cao {chieu_cao}cm, Cân nặng {can_nang}kg")
        st.write(f"- Đường huyết TB từ: Lúc đói {duong_huyet_ac}mg/dL, Sau ăn {duong_huyet_sau_an}mg/dL")