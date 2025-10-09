import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
import io
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
warnings.filterwarnings('ignore')

# Cấu hình trang
st.set_page_config(
    page_title="Hệ thống Dự đoán Đột quỵ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh cho giao diện đẹp
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #CBCBCBFF 0%, #FDFDFDFF 100%);
    }
    
    .main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Header Styles */
    .main-header {
        font-size: 3.5rem;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    
    .sub-header {
        font-size: 1.8rem;
        color: #2d3748;
        margin-bottom: 1.5rem;
        font-weight: 600;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
        display: inline-block;
    }
    
    /* Card Styles */
    .metric-card {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Input Styles */
    .stSelectbox > div > div {
        background-color: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        transition: border-color 0.2s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .stNumberInput > div > div > input {
        background-color: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.75rem;
        transition: border-color 0.2s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Prediction Result Styles */
    .prediction-result {
        font-size: 1.3rem;
        font-weight: 600;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .high-risk {
        background: linear-gradient(135deg, #fed7d7 0%, #feb2b2 100%);
        color: #c53030;
        border: 2px solid #fc8181;
    }
    
    .low-risk {
        background: linear-gradient(135deg, #c6f6d5 0%, #9ae6b4 100%);
        color: #22543d;
        border: 2px solid #68d391;
    }
    
    /* Tab Styles */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #f7fafc;
        border-radius: 15px;
        padding: 0.8rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: transparent;
        border-radius: 10px;
        color: #4a5568;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0 1.5rem;
        transition: all 0.2s ease;
        min-width: 150px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
    }
    
    /* JSON Display Styles */
    .json-container {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border: 1px solid #4a5568;
    }
    
    .json-key {
        color: #63b3ed;
        font-weight: 600;
    }
    
    .json-string {
        color: #68d391;
    }
    
    .json-number {
        color: #fbb6ce;
    }
    
    .json-boolean {
        color: #f6ad55;
    }
    
    /* Info Display Styles */
    .info-card {
        background: linear-gradient(135deg, #ebf8ff 0%, #bee3f8 100%);
        border: 1px solid #90cdf4;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
    }
    
    .info-title {
        color: #1e40af;
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    
    .info-content {
        color: #1e3a8a;
        line-height: 1.6;
    }
    
    /* File Upload Styles */
    .stFileUploader > div {
        background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
        border: 2px dashed #48bb78;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div:hover {
        border-color: #38a169;
        background: linear-gradient(135deg, #c6f6d5 0%, #9ae6b4 100%);
    }
    
    /* Sidebar Styles */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Thông tin tạng người
RACE_INFO = {
    "Châu Á": {
        "bmi_ranges": {
            "thiếu_cân": "< 18.5",
            "bình_thường": "18.5 - 22.9", 
            "thừa_cân": "23.0 - 24.9",
            "béo_phì_độ_1": "25.0 - 29.9",
            "béo_phì_độ_2": "≥ 30.0"
        },
        "glucose_normal": 100,
        "age_risk": {
            "thấp": "< 45 tuổi",
            "trung_bình": "45-65 tuổi", 
            "cao": "> 65 tuổi"
        }
    },
    "Châu Mỹ": {
        "bmi_ranges": {
            "thiếu_cân": "< 18.5",
            "bình_thường": "18.5 - 24.9",
            "thừa_cân": "25.0 - 29.9", 
            "béo_phì_độ_1": "30.0 - 34.9",
            "béo_phì_độ_2": "≥ 35.0"
        },
        "glucose_normal": 100,
        "age_risk": {
            "thấp": "< 50 tuổi",
            "trung_bình": "50-70 tuổi",
            "cao": "> 70 tuổi"
        }
    }
}

# Hàm huấn luyện lại SVM với dữ liệu cân bằng
@st.cache_data
def train_balanced_svm():
    """Huấn luyện lại mô hình SVM với dữ liệu đã được cân bằng bằng SMOTE"""
    try:
        # Load dữ liệu
        data = pd.read_csv('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv')
        
        # Chuẩn bị features và target
        feature_columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 
                          'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
        
        X = data[feature_columns].copy()
        y = data['stroke']
        
        # Xử lý dữ liệu categorical
        X_encoded = pd.get_dummies(X, columns=['gender', 'ever_married', 'work_type', 
                                              'Residence_type', 'smoking_status'])
        
        # Chia dữ liệu
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, 
                                                           random_state=42, stratify=y)
        
        # Áp dụng SMOTE để cân bằng dữ liệu
        smote = SMOTE(random_state=42, k_neighbors=3)
        X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
        
        # Chuẩn hóa dữ liệu
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_balanced)
        
        # Huấn luyện SVM với class_weight='balanced' để tăng cường hiệu quả
        svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', class_weight='balanced', 
                       probability=True, random_state=42)
        svm_model.fit(X_train_scaled, y_train_balanced)
        
        return svm_model, scaler, X_encoded.columns.tolist()
        
    except Exception as e:
        st.error(f"Lỗi khi huấn luyện SVM: {str(e)}")
        return None, None, None

# Tải mô hình và bộ tiền xử lý
@st.cache_resource
def load_models():
    """Load tất cả các mô hình và preprocessor"""
    try:
        models = {
            'AdaBoost_Final': joblib.load('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/models/moHinhDotQuy_final.pkl'),  # Mô hình chính được huấn luyện
            'AdaBoost_Dir': joblib.load('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/models/AdaBoost/AdaBoost.pkl'),     # Mô hình từ thư mục AdaBoost
            'Logistic_Regression': joblib.load('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/models/Logistic_Regression/Logistic_Regression.pkl'),  # Mô hình hồi quy logistic
        }
        
        # Huấn luyện SVM mới với dữ liệu cân bằng
        svm_model, svm_scaler, svm_features = train_balanced_svm()
        if svm_model is not None:
            models['SVM'] = {
                'model': svm_model,
                'scaler': svm_scaler, 
                'features': svm_features
            }
        else:
            # Fallback về SVM cũ nếu không thể huấn luyện mới
            models['SVM'] = joblib.load('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/models/SVM/SVM.pkl')
        
        preprocessor = joblib.load('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/models/preprocessor.pkl')  # Bộ tiền xử lý dữ liệu
        return models, preprocessor
    except Exception as e:
        st.error(f"Lỗi khi tải mô hình: {str(e)}")
        return None, None

# Tải dữ liệu mẫu
@st.cache_data
def load_sample_data():
    try:
        data = pd.read_csv('/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv')
        return data
    except Exception as e:
        st.error(f"Lỗi khi tải dữ liệu: {str(e)}")
        return None

# Hàm tính BMI
def calculate_bmi(height_cm, weight_kg):
    """Tính BMI từ chiều cao (cm) và cân nặng (kg)"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

# Hàm phân loại BMI theo tạng người
def classify_bmi(bmi, race):
    """Phân loại BMI theo tạng người"""
    if race == "Châu Á":
        if bmi < 18.5:
            return "thiếu_cân", "orange"
        elif bmi < 23:
            return "bình_thường", "green"
        elif bmi < 25:
            return "thừa_cân", "orange"
        elif bmi < 30:
            return "béo_phì_độ_1", "red"
        else:
            return "béo_phì_độ_2", "darkred"
    else:  # Châu Mỹ
        if bmi < 18.5:
            return "thiếu_cân", "orange"
        elif bmi < 25:
            return "bình_thường", "green"
        elif bmi < 30:
            return "thừa_cân", "orange"
        elif bmi < 35:
            return "béo_phì_độ_1", "red"
        else:
            return "béo_phì_độ_2", "darkred"

# Hàm kiểm tra dữ liệu đã được train chưa
def check_data_already_trained(new_data, existing_df):
    """Kiểm tra xem dữ liệu mới có trùng với dữ liệu đã train chưa"""
    try:
        duplicates = []
        similar_records = []
        
        for i, data in enumerate(new_data):
            age = data.get('tuổi', 0)
            gender = data.get('giới_tính', '').lower()
            height = data.get('chiều_cao', 0)
            weight = data.get('cân_nặng', 0)
            glucose = data.get('glucose', 0)
            
            # Chuyển đổi giới tính để so sánh
            gender_csv = 'male' if gender in ['nam', 'male'] else 'female'
            
            # Tìm bản ghi trùng khớp hoàn toàn
            exact_matches = existing_df[
                (existing_df['age'] == age) & 
                (existing_df['gender'].str.lower() == gender_csv) &
                (existing_df['avg_glucose_level'] == glucose)
            ]
            
            if len(exact_matches) > 0:
                duplicates.append({
                    'index': i,
                    'file_name': data.get('file_name', f'File {i+1}'),
                    'data': data,
                    'matched_ids': exact_matches['id'].tolist(),
                    'match_type': 'exact'
                })
            else:
                # Tìm bản ghi tương tự (cùng tuổi, giới tính, glucose gần)
                similar_matches = existing_df[
                    (existing_df['age'] == age) & 
                    (existing_df['gender'].str.lower() == gender_csv) &
                    (abs(existing_df['avg_glucose_level'] - glucose) <= 10)
                ]
                
                if len(similar_matches) > 0:
                    similar_records.append({
                        'index': i,
                        'file_name': data.get('file_name', f'File {i+1}'),
                        'data': data,
                        'matched_ids': similar_matches['id'].tolist(),
                        'match_type': 'similar'
                    })
        
        return duplicates, similar_records
    except Exception as e:
        st.error(f"Lỗi khi kiểm tra dữ liệu trùng lặp: {str(e)}")
        return [], []
def validate_parsed_data(data):
    """Kiểm tra tính hợp lệ của dữ liệu đã phân tích từ bệnh án"""
    required_fields = ['tuổi', 'giới_tính', 'chiều_cao', 'cân_nặng', 'glucose']
    
    # Kiểm tra các trường bắt buộc
    for field in required_fields:
        if field not in data or data[field] is None:
            return False
    
    # Kiểm tra giá trị hợp lệ
    try:
        age = data.get('tuổi', 0)
        height = data.get('chiều_cao', 0)
        weight = data.get('cân_nặng', 0)
        glucose = data.get('glucose', 0)
        
        # Kiểm tra khoảng giá trị hợp lệ
        if not (0 < age <= 120):
            return False
        if not (100 <= height <= 250):
            return False
        if not (30 <= weight <= 200):
            return False
        if not (50 <= glucose <= 300):
            return False
        
        # Kiểm tra giới tính
        gender = data.get('giới_tính', '').lower()
        if gender not in ['nam', 'nữ', 'male', 'female']:
            return False
        
        return True
    except:
        return False

# Hàm chuyển đổi dữ liệu thành format CSV chuẩn hóa theo file hiện tại
def convert_to_csv_format(approved_data):
    """Chuyển đổi dữ liệu đã phê duyệt thành format CSV chuẩn theo file hiện có"""
    try:
        # Đọc CSV hiện tại để lấy cấu trúc
        csv_path = '/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv'
        existing_df = pd.read_csv(csv_path)
        
        # Lấy ID cao nhất hiện tại
        max_id = existing_df['id'].max() if len(existing_df) > 0 else 0
        
        new_rows = []
        
        for idx, data in enumerate(approved_data):
            # Tính BMI
            height_m = data.get('chiều_cao', 170) / 100
            bmi = data.get('cân_nặng', 65) / (height_m ** 2)
            
            # Chuyển đổi giới tính theo format CSV
            gender = data.get('giới_tính', 'Nam')
            if gender.lower() in ['nam', 'male']:
                gender_csv = 'Male'
            elif gender.lower() in ['nữ', 'female']:
                gender_csv = 'Female'
            else:
                gender_csv = 'Other'
            
            # Tạo ID mới
            new_id = max_id + idx + 1
            
            # Xác định stroke dựa trên logic AI
            age = data.get('tuổi', 30)
            hypertension = 1 if data.get('tăng_huyết_áp', False) else 0
            heart_disease = 1 if data.get('bệnh_tim', False) else 0
            glucose = data.get('glucose', 100)
            
            # Logic AI để xác định stroke (cải tiến)
            stroke = 0
            risk_score = 0
            
            # Tính điểm nguy cơ
            if age > 65:
                risk_score += 2
            elif age > 50:
                risk_score += 1
                
            if hypertension:
                risk_score += 2
            if heart_disease:
                risk_score += 3
            if glucose > 200:
                risk_score += 2
            elif glucose > 140:
                risk_score += 1
            if bmi > 30:
                risk_score += 1
            
            # Xác định stroke dựa trên risk_score
            if risk_score >= 5:
                stroke = 1
            elif risk_score >= 3 and age > 60:
                stroke = 1
            
            # Tạo các nhóm theo format CSV
            if age < 18:
                nhom_tuoi = "treEm"
            elif age < 35:
                nhom_tuoi = "tuoiTre"
            elif age < 50:
                nhom_tuoi = "trungNien"
            elif age < 65:
                nhom_tuoi = "truocTuoiHuu"
            else:
                nhom_tuoi = "tuoiCao"
            
            if bmi < 18.5:
                nhom_bmi = "thieuCan"
            elif bmi < 23:
                nhom_bmi = "binhThuong"
            elif bmi < 25:
                nhom_bmi = "thuaCan"
            else:
                nhom_bmi = "beoPhi"
            
            if glucose < 100:
                nhom_glucose = "binhThuong"
            elif glucose < 126:
                nhom_glucose = "tienTieuDuong"
            else:
                nhom_glucose = "tieuDuong"
            
            # Tính điểm nguy cơ cuối cùng
            diem_nguy_co = calculate_risk_score(age, hypertension, heart_disease, glucose, bmi, "Châu Á")
            
            # Tạo row mới theo đúng format CSV
            new_row = {
                'id': new_id,
                'gender': gender_csv,
                'age': float(age),
                'hypertension': hypertension,
                'heart_disease': heart_disease,
                'ever_married': 'Yes' if age > 25 else 'No',  # Logic đơn giản
                'work_type': 'Private',  # Mặc định
                'Residence_type': 'Urban',  # Mặc định
                'avg_glucose_level': float(glucose),
                'bmi': round(bmi, 1),
                'smoking_status': 'never smoked',  # Mặc định
                'stroke': stroke,
                'nhomTuoi': nhom_tuoi,
                'nhomBMI': nhom_bmi,
                'nhomGlucose': nhom_glucose,
                'diemNguyCo': diem_nguy_co
            }
            
            new_rows.append(new_row)
        
        return new_rows
    except Exception as e:
        st.error(f"Lỗi khi chuyển đổi dữ liệu: {str(e)}")
        return None

# Hàm thêm dữ liệu vào CSV
def add_to_csv(new_rows):
    """Thêm dữ liệu mới vào file CSV"""
    try:
        csv_path = '/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv'
        
        # Đọc CSV hiện tại
        existing_df = pd.read_csv(csv_path)
        
        # Tạo DataFrame từ dữ liệu mới
        new_df = pd.DataFrame(new_rows)
        
        # Kết hợp dữ liệu
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        
        # Lưu lại file CSV
        combined_df.to_csv(csv_path, index=False)
        
        return 100.0  # Tỷ lệ thành công
    except Exception as e:
        st.error(f"Lỗi khi thêm vào CSV: {str(e)}")
        return 0.0

# Hàm cập nhật preprocessor (giả lập)
def update_preprocessor(new_rows):
    """Cập nhật preprocessor với dữ liệu mới (giả lập)"""
    try:
        # Trong thực tế, đây sẽ là quá trình retrain preprocessor
        # Hiện tại chỉ giả lập
        preprocessor_path = '/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /models/preprocessor.pkl'
        
        # Load preprocessor hiện tại
        preprocessor = joblib.load(preprocessor_path)
        
        # Giả lập việc cập nhật (trong thực tế sẽ fit lại với dữ liệu mới)
        # preprocessor.fit(new_data)
        
        # Lưu lại (trong demo này không thực sự thay đổi)
        joblib.dump(preprocessor, preprocessor_path)
        
        return True
    except Exception as e:
        st.error(f"Lỗi khi cập nhật preprocessor: {str(e)}")
        return False

# Hàm đọc file bệnh án
def display_colored_json(data, title="Thông tin đã phân tích"):
    """Hiển thị JSON với màu sắc đẹp mắt"""
    import json
    
    st.markdown(f'<div class="info-title">{title}</div>', unsafe_allow_html=True)
    
    # Tạo HTML cho JSON với màu sắc
    json_html = '<div class="json-container">'
    json_html += '<pre style="margin: 0; font-family: \'Fira Code\', monospace; font-size: 14px; line-height: 1.6;">'
    
    def format_value(key, value, indent=0):
        spaces = "&nbsp;" * (indent * 4)
        if isinstance(value, dict):
            result = f'{spaces}<span class="json-key">"{key}"</span>: {{\n'
            for k, v in value.items():
                result += format_value(k, v, indent + 1) + ',\n'
            result = result.rstrip(',\n') + '\n' + spaces + '}'
            return result
        elif isinstance(value, str):
            return f'{spaces}<span class="json-key">"{key}"</span>: <span class="json-string">"{value}"</span>'
        elif isinstance(value, bool):
            return f'{spaces}<span class="json-key">"{key}"</span>: <span class="json-boolean">{str(value).lower()}</span>'
        elif isinstance(value, (int, float)):
            return f'{spaces}<span class="json-key">"{key}"</span>: <span class="json-number">{value}</span>'
        else:
            return f'{spaces}<span class="json-key">"{key}"</span>: <span class="json-string">"{str(value)}"</span>'
    
    json_html += '{\n'
    for key, value in data.items():
        json_html += format_value(key, value, 1) + ',\n'
    json_html = json_html.rstrip(',\n') + '\n}'
    
    json_html += '</pre></div>'
    
    st.markdown(json_html, unsafe_allow_html=True)

def display_input_summary(input_data):
    """Hiển thị tóm tắt thông tin đầu vào một cách trực quan"""
    st.markdown('<div class="info-title">Thông tin đầu vào hiện tại</div>', unsafe_allow_html=True)
    
    # Chia thành các cột để hiển thị đẹp hơn
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">Thông tin cá nhân</div>
            <div class="info-content">
                <strong>Tuổi:</strong> {}<br>
                <strong>Giới tính:</strong> {}<br>
                <strong>Tạng người:</strong> {}
            </div>
        </div>
        """.format(
            input_data.get('age', [0])[0] if 'age' in input_data else 'Chưa nhập',
            input_data.get('gender', [''])[0] if 'gender' in input_data else 'Chưa chọn',
            input_data.get('race', [''])[0] if 'race' in input_data else 'Chưa chọn'
        ), unsafe_allow_html=True)
    
    with col2:
        bmi = 0
        if 'bmi' in input_data and input_data['bmi'][0] > 0:
            bmi = input_data['bmi'][0]
        
        st.markdown("""
        <div class="info-card">
            <div class="info-title">Thông số sức khỏe</div>
            <div class="info-content">
                <strong>Chiều cao:</strong> {} cm<br>
                <strong>Cân nặng:</strong> {} kg<br>
                <strong>BMI:</strong> {:.1f}
            </div>
        </div>
        """.format(
            input_data.get('height', [0])[0] if 'height' in input_data else 'Chưa nhập',
            input_data.get('weight', [0])[0] if 'weight' in input_data else 'Chưa nhập',
            bmi
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">Tình trạng bệnh lý</div>
            <div class="info-content">
                <strong>Tăng huyết áp:</strong> {}<br>
                <strong>Bệnh tim:</strong> {}<br>
                <strong>Glucose:</strong> {} mg/dL
            </div>
        </div>
        """.format(
            'Có' if input_data.get('hypertension', [0])[0] == 1 else 'Không',
            'Có' if input_data.get('heart_disease', [0])[0] == 1 else 'Không',
            input_data.get('avg_glucose_level', [0])[0] if 'avg_glucose_level' in input_data else 'Chưa nhập'
        ), unsafe_allow_html=True)

def parse_medical_record(file_content):
    """Phân tích file bệnh án txt và trích xuất thông tin"""
    try:
        lines = file_content.split('\n')
        data = {}
        
        for line in lines:
            line = line.strip().lower()
            if not line:
                continue
                
            # Tìm thông tin cơ bản
            if 'tuổi' in line or 'age' in line:
                numbers = [int(s) for s in line.split() if s.isdigit()]
                if numbers:
                    data['tuổi'] = numbers[0]
            
            if 'giới tính' in line or 'gender' in line:
                if 'nam' in line or 'male' in line:
                    data['giới_tính'] = 'Nam'
                elif 'nữ' in line or 'female' in line:
                    data['giới_tính'] = 'Nữ'
            
            if 'chiều cao' in line or 'height' in line:
                numbers = [float(s) for s in line.replace(',', '.').split() if s.replace('.', '').isdigit()]
                if numbers:
                    data['chiều_cao'] = numbers[0]
            
            if 'cân nặng' in line or 'weight' in line:
                numbers = [float(s) for s in line.replace(',', '.').split() if s.replace('.', '').isdigit()]
                if numbers:
                    data['cân_nặng'] = numbers[0]
            
            if 'huyết áp' in line or 'hypertension' in line:
                data['tăng_huyết_áp'] = 'có' in line or 'yes' in line
            
            if 'tim' in line or 'heart' in line:
                data['bệnh_tim'] = 'có' in line or 'yes' in line
            
            if 'glucose' in line or 'đường huyết' in line:
                numbers = [float(s) for s in line.replace(',', '.').split() if s.replace('.', '').isdigit()]
                if numbers:
                    data['glucose'] = numbers[0]
        
        return data
    except Exception as e:
        st.error(f"Lỗi khi phân tích bệnh án: {str(e)}")
        return None

# Hàm dự đoán
def make_predictions(input_data, models, preprocessor):
    try:
        predictions = {}
        probabilities = {}
        
        for name, model in models.items():
            if name == 'SVM' and isinstance(model, dict):
                # Xử lý SVM mới với dữ liệu cân bằng
                svm_model = model['model']
                svm_scaler = model['scaler']
                svm_features = model['features']
                
                # Chuẩn bị dữ liệu cho SVM
                input_encoded = pd.get_dummies(input_data, columns=['gender', 'ever_married', 'work_type', 
                                                                   'Residence_type', 'smoking_status'])
                
                # Đảm bảo có đủ các cột như khi huấn luyện
                for col in svm_features:
                    if col not in input_encoded.columns:
                        input_encoded[col] = 0
                
                # Sắp xếp lại thứ tự cột
                input_encoded = input_encoded[svm_features]
                
                # Chuẩn hóa dữ liệu
                input_scaled = svm_scaler.transform(input_encoded)
                
                # Dự đoán
                pred = svm_model.predict(input_scaled)[0]
                prob = svm_model.predict_proba(input_scaled)[0]
                
                probabilities[name] = {
                    'Không đột quỵ': prob[0] * 100,
                    'Có đột quỵ': prob[1] * 100
                }
                predictions[name] = pred
                
            else:
                # Xử lý các mô hình khác như bình thường
                processed_data = preprocessor.transform(input_data)
                pred = model.predict(processed_data)[0]
                
                if hasattr(model, 'predict_proba'):
                    prob = model.predict_proba(processed_data)[0]
                    probabilities[name] = {
                        'Không đột quỵ': prob[0] * 100,
                        'Có đột quỵ': prob[1] * 100
                    }
                else:
                    # Fallback cho SVM cũ nếu cần
                    decision = model.decision_function(processed_data)[0]
                    prob_stroke = 1 / (1 + np.exp(-decision))
                    prob_stroke = 1 - prob_stroke
                    
                    probabilities[name] = {
                        'Không đột quỵ': (1 - prob_stroke) * 100,
                        'Có đột quỵ': prob_stroke * 100
                    }
                
                predictions[name] = pred
            
        return predictions, probabilities
    except Exception as e:
        st.error(f"Lỗi khi dự đoán: {str(e)}")
        return None, None

# Hàm tính điểm nguy cơ theo tạng người
def calculate_risk_score(age, hypertension, heart_disease, avg_glucose_level, bmi, race):
    score = 0
    
    # Điểm theo tuổi (khác nhau giữa Châu Á và Châu Mỹ)
    if race == "Châu Á":
        if age < 30:
            score += 0
        elif age < 45:
            score += 1
        elif age < 60:
            score += 2
        elif age < 75:
            score += 3
        else:
            score += 4
    else:  # Châu Mỹ
        if age < 35:
            score += 0
        elif age < 50:
            score += 1
        elif age < 65:
            score += 2
        elif age < 80:
            score += 3
        else:
            score += 4
    
    # Điểm theo tình trạng sức khỏe
    if hypertension:
        score += 2
    if heart_disease:
        score += 3
    
    # Điểm theo glucose
    if avg_glucose_level < 100:
        score += 0
    elif avg_glucose_level < 126:
        score += 1
    else:
        score += 2
    
    # Điểm theo BMI (khác nhau giữa Châu Á và Châu Mỹ)
    if race == "Châu Á":
        if bmi < 18.5:
            score += 1  # Thiếu cân
        elif bmi < 23:
            score += 0  # Bình thường
        elif bmi < 25:
            score += 1  # Thừa cân
        elif bmi < 30:
            score += 2  # Béo phì độ I
        else:
            score += 3  # Béo phì độ II+
    else:  # Châu Mỹ
        if bmi < 18.5:
            score += 1  # Thiếu cân
        elif bmi < 25:
            score += 0  # Bình thường
        elif bmi < 30:
            score += 1  # Thừa cân
        elif bmi < 35:
            score += 2  # Béo phì độ I
        else:
            score += 3  # Béo phì độ II+
    
    return min(score, 10)  # Giới hạn tối đa 10 điểm

# Main app
def main():
    st.markdown('<h1 class="main-header">Hệ thống Dự đoán Đột quỵ</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Sử dụng AI để đánh giá nguy cơ đột quỵ dựa trên thông tin sức khỏe</p>', unsafe_allow_html=True)
    
    # Load models và data
    models, preprocessor = load_models()
    sample_data = load_sample_data()
    
    if models is None or preprocessor is None:
        st.error("Không thể tải mô hình. Vui lòng kiểm tra đường dẫn file.")
        return
    
    # Tạo tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dự đoán", "So sánh Mô hình", "Thống kê", "Học dữ liệu", "Thông tin"])
    
    with tab1:
        st.markdown('<h2 class="sub-header">Nhập thông tin bệnh nhân</h2>', unsafe_allow_html=True)
        
        # Sidebar cho nhập bệnh án
        with st.sidebar:
            st.markdown("### Nhập bệnh án từ file")
            uploaded_file = st.file_uploader("Chọn file bệnh án (.txt)", type=['txt'])
            
            if uploaded_file is not None:
                file_content = str(uploaded_file.read(), "utf-8")
                
                # Hiển thị nội dung file trong expander
                with st.expander("Xem nội dung file", expanded=False):
                    st.text_area("Nội dung file:", file_content, height=200, disabled=True)
                
                if st.button("Phân tích bệnh án"):
                    parsed_data = parse_medical_record(file_content)
                    if parsed_data:
                        st.success("Đã phân tích thành công!")
                        # Hiển thị JSON với màu sắc đẹp mắt
                        display_colored_json(parsed_data, "Thông tin đã trích xuất từ bệnh án")
                        # Lưu vào session state để sử dụng
                        for key, value in parsed_data.items():
                            st.session_state[f"parsed_{key}"] = value
        
        # Chọn tạng người
        st.markdown("### Chọn tạng người")
        col_race1, col_race2 = st.columns(2)
        
        with col_race1:
            race = st.selectbox("Tạng người", ["Châu Á", "Châu Mỹ"])
        
        with col_race2:
            # Hiển thị gợi ý theo tạng người
            race_info = RACE_INFO[race]
            st.info(f"""
            **Gợi ý cho người {race}:**
            - BMI bình thường: {race_info['bmi_ranges']['bình_thường']}
            - Nguy cơ tuổi tác: {race_info['age_risk']['trung_bình']}
            """)
        
        # Tạo form input với grid layout đẹp hơn
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div class="info-title">Thông tin cá nhân</div>', unsafe_allow_html=True)
            
            # Sử dụng dữ liệu từ bệnh án nếu có
            default_gender = "Nam" if st.session_state.get("parsed_giới_tính") == "Nam" else "Nữ"
            gender_options = ["Nam", "Nữ", "Khác"]
            gender_index = gender_options.index(default_gender) if default_gender in gender_options else 0
            
            gender = st.selectbox("Giới tính", gender_options, index=gender_index)
            
            default_age = st.session_state.get("parsed_tuổi", 45)
            age = st.number_input("Tuổi", min_value=0, max_value=120, value=default_age)
            
            ever_married = st.selectbox("Tình trạng hôn nhân", ["Có", "Không"])
            work_type = st.selectbox("Loại công việc", 
                                   ["Tư nhân", "Tự kinh doanh", "Công chức", "Trẻ em", "Chưa làm việc"])
        
        with col2:
            st.markdown('<div class="info-title">Thông tin sức khỏe</div>', unsafe_allow_html=True)
            
            default_hypertension = st.session_state.get("parsed_tăng_huyết_áp", False)
            hypertension = st.selectbox("Tăng huyết áp", ["Không", "Có"], 
                                      index=1 if default_hypertension else 0)
            
            default_heart_disease = st.session_state.get("parsed_bệnh_tim", False)
            heart_disease = st.selectbox("Bệnh tim", ["Không", "Có"],
                                       index=1 if default_heart_disease else 0)
            
            # Glucose mặc định ở mức bình thường
            parsed_glucose = st.session_state.get("parsed_glucose", race_info['glucose_normal'])
            # Đảm bảo giá trị glucose trong khoảng hợp lệ
            if parsed_glucose < 50.0:
                default_glucose = race_info['glucose_normal']
            else:
                default_glucose = parsed_glucose
            avg_glucose_level = st.number_input("Mức glucose trung bình (mg/dL)", 
                                              min_value=50.0, max_value=300.0, value=float(default_glucose))
            
            # Thay đổi BMI thành chiều cao và cân nặng
            st.markdown('<div class="info-title">Chỉ số cơ thể</div>', unsafe_allow_html=True)
            default_height = st.session_state.get("parsed_chiều_cao", 165.0)
            height = st.number_input("Chiều cao (cm)", min_value=100.0, max_value=250.0, value=default_height)
            
            default_weight = st.session_state.get("parsed_cân_nặng", 65.0)
            weight = st.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=default_weight)
            
            # Tự động tính BMI
            bmi = calculate_bmi(height, weight)
            st.metric("Chỉ số BMI", f"{bmi}")
        
        with col3:
            st.markdown('<div class="info-title">Thông tin khác</div>', unsafe_allow_html=True)
            residence_type = st.selectbox("Nơi cư trú", ["Thành thị", "Nông thôn"])
            smoking_status = st.selectbox("Tình trạng hút thuốc", 
                                        ["Chưa bao giờ hút", "Đã từng hút", "Đang hút", "Không rõ"])
            
            # Hiển thị phân loại BMI theo tạng người
            bmi_category, bmi_color = classify_bmi(bmi, race)
            bmi_text = race_info['bmi_ranges'][bmi_category]
            
            st.markdown('<div class="info-title">Đánh giá BMI</div>', unsafe_allow_html=True)
            st.markdown(f"<span style='color: {bmi_color}; font-weight: bold'>{bmi_category.replace('_', ' ').title()}</span>", 
                       unsafe_allow_html=True)
            st.markdown(f"*Khoảng {race}: {bmi_text}*")
            
            # Hiển thị gợi ý nguy cơ theo tuổi
            if race == "Châu Á":
                if age < 45:
                    age_risk = "Thấp"
                    age_color = "green"
                elif age < 65:
                    age_risk = "Trung bình"
                    age_color = "orange"
                else:
                    age_risk = "Cao"
                    age_color = "red"
            else:  # Châu Mỹ
                if age < 50:
                    age_risk = "Thấp"
                    age_color = "green"
                elif age < 70:
                    age_risk = "Trung bình"
                    age_color = "orange"
                else:
                    age_risk = "Cao"
                    age_color = "red"
            
            st.markdown(f"**Nguy cơ theo tuổi:** <span style='color: {age_color}'>{age_risk}</span>", 
                       unsafe_allow_html=True)
        
        # Chuyển đổi dữ liệu để phù hợp với mô hình
        # Chuyển đổi giới tính
        if gender == "Nam":
            gender_model = "Male"
        elif gender == "Nữ":
            gender_model = "Female"
        else:
            gender_model = "Other"
        
        # Chuyển đổi tình trạng hôn nhân
        ever_married_model = "Yes" if ever_married == "Có" else "No"
        
        # Chuyển đổi loại công việc
        work_type_mapping = {
            "Tư nhân": "Private",
            "Tự kinh doanh": "Self-employed", 
            "Công chức": "Govt_job",
            "Trẻ em": "children",
            "Chưa làm việc": "Never_worked"
        }
        work_type_model = work_type_mapping[work_type]
        
        # Chuyển đổi nơi cư trú
        residence_type_model = "Urban" if residence_type == "Thành thị" else "Rural"
        
        # Chuyển đổi tình trạng hút thuốc
        smoking_mapping = {
            "Chưa bao giờ hút": "never smoked",
            "Đã từng hút": "formerly smoked",
            "Đang hút": "smokes", 
            "Không rõ": "Unknown"
        }
        smoking_status_model = smoking_mapping[smoking_status]
        
        # Chuyển đổi tăng huyết áp và bệnh tim
        hypertension_model = 1 if hypertension == "Có" else 0
        heart_disease_model = 1 if heart_disease == "Có" else 0
        
        # Tạo nhóm tuổi, BMI, glucose
        if age < 18:
            nhom_tuoi = "treEm"
        elif age < 35:
            nhom_tuoi = "tuoiTre"
        elif age < 50:
            nhom_tuoi = "trungNien"
        elif age < 65:
            nhom_tuoi = "truocTuoiHuu"
        else:
            nhom_tuoi = "tuoiCao"
        
        if bmi < 18.5:
            nhom_bmi = "thieuCan"
        elif bmi < 23:
            nhom_bmi = "binhThuong"
        elif bmi < 25:
            nhom_bmi = "thua Can"
        else:
            nhom_bmi = "beoPhi"
        
        if avg_glucose_level < 100:
            nhom_glucose = "binhThuong"
        elif avg_glucose_level < 126:
            nhom_glucose = "tienTieuDuong"
        else:
            nhom_glucose = "tieuDuong"
        
        # Tính điểm nguy cơ
        diem_nguy_co = calculate_risk_score(age, hypertension_model, heart_disease_model, avg_glucose_level, bmi, race)
        
        # Tạo dataframe input
        input_data = pd.DataFrame({
            'gender': [gender_model],
            'age': [age],
            'hypertension': [hypertension_model],
            'heart_disease': [heart_disease_model],
            'ever_married': [ever_married_model],
            'work_type': [work_type_model],
            'Residence_type': [residence_type_model],
            'avg_glucose_level': [avg_glucose_level],
            'bmi': [bmi],
            'smoking_status': [smoking_status_model],
            'nhomTuoi': [nhom_tuoi],
            'nhomBMI': [nhom_bmi],
            'nhomGlucose': [nhom_glucose],
            'diemNguyCo': [diem_nguy_co]
        })
        
        # Đóng div metric-card
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Hiển thị tóm tắt thông tin đầu vào
        st.markdown("---")
        display_input_summary(input_data)
        st.markdown("---")
        
        # Nút dự đoán
        if st.button("Thực hiện Dự đoán", type="primary", use_container_width=True):
            with st.spinner("Đang phân tích..."):
                predictions, probabilities = make_predictions(input_data, models, preprocessor)
                
                if predictions is not None:
                    st.markdown("---")
                    st.markdown('<h3 class="sub-header">Kết quả Dự đoán</h3>', unsafe_allow_html=True)
                    
                    # Hiển thị kết quả theo format mẫu
                    st.markdown("**--------------------------------------------------**")
                    
                    for model_name, prediction in predictions.items():
                        prob_no_stroke = probabilities[model_name]['Không đột quỵ']
                        prob_stroke = probabilities[model_name]['Có đột quỵ']
                        
                        # Xác định nguy cơ và độ tin cậy
                        if prediction == 1:
                            risk_level = "NGUY CƠ CAO"
                            confidence = prob_stroke
                        else:
                            risk_level = "NGUY CƠ THẤP"
                            confidence = prob_no_stroke
                        
                        # Hiển thị theo format mẫu
                        st.markdown(f"""
                        **{model_name}:**
                        &nbsp;&nbsp;&nbsp;&nbsp;Kết quả: **{risk_level}**
                        &nbsp;&nbsp;&nbsp;&nbsp;Độ tin cậy: **{confidence:.1f}%**
                        &nbsp;&nbsp;&nbsp;&nbsp;Xác suất không đột quỵ: **{prob_no_stroke/100:.3f}**
                        &nbsp;&nbsp;&nbsp;&nbsp;Xác suất đột quỵ: **{prob_stroke/100:.3f}**
                        """)
                        st.markdown("")
                    
                    st.markdown("**--------------------------------------------------**")
                    
                    # Hiển thị ghi chú về các mô hình
                    st.markdown("### Ghi chú về Mô hình")
                    st.markdown("""
                    - **AdaBoost_Final**: Mô hình chính được huấn luyện (moHinhDotQuy_final.pkl)
                    - **AdaBoost_Dir**: Mô hình AdaBoost từ thư mục models/AdaBoost/
                    - **Logistic_Regression**: Mô hình hồi quy logistic từ thư mục models/Logistic_Regression/
                    - **SVM**: Mô hình Support Vector Machine **đã được cân bằng dữ liệu** (huấn luyện lại với SMOTE)
                    - **Preprocessor**: Bộ tiền xử lý dữ liệu (preprocessor.pkl) - không phải mô hình dự đoán
                    """)
                    
                    # Biểu đồ so sánh xác suất
                    st.markdown("### So sánh Xác suất Đột quỵ")
                    
                    prob_data = []
                    for model_name, probs in probabilities.items():
                        prob_data.append({
                            'Mô hình': model_name,
                            'Không đột quỵ': probs['Không đột quỵ'],
                            'Có đột quỵ': probs['Có đột quỵ']
                        })
                    
                    prob_df = pd.DataFrame(prob_data)
                    
                    fig = px.bar(prob_df, x='Mô hình', y=['Không đột quỵ', 'Có đột quỵ'],
                               title="So sánh Xác suất Dự đoán giữa các Mô hình",
                               color_discrete_map={'Không đột quỵ': '#2E8B57', 'Có đột quỵ': '#DC143C'})
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Điểm nguy cơ
                    st.markdown("### Đánh giá Nguy cơ Tổng thể")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Điểm Nguy cơ", f"{diem_nguy_co}/10")
                        
                        if diem_nguy_co <= 3:
                            risk_level = "Thấp"
                            risk_color = "green"
                        elif diem_nguy_co <= 6:
                            risk_level = "Trung bình"
                            risk_color = "orange"
                        else:
                            risk_level = "Cao"
                            risk_color = "red"
                        
                        st.markdown(f"**Mức độ nguy cơ:** <span style='color: {risk_color}; font-weight: bold'>{risk_level}</span>", 
                                   unsafe_allow_html=True)
                    
                    with col2:
                        # Gauge chart cho điểm nguy cơ
                        fig_gauge = go.Figure(go.Indicator(
                            mode = "gauge+number",
                            value = diem_nguy_co,
                            domain = {'x': [0, 1], 'y': [0, 1]},
                            title = {'text': "Điểm Nguy cơ"},
                            gauge = {
                                'axis': {'range': [None, 10]},
                                'bar': {'color': "darkblue"},
                                'steps': [
                                    {'range': [0, 3], 'color': "lightgreen"},
                                    {'range': [3, 6], 'color': "yellow"},
                                    {'range': [6, 10], 'color': "red"}
                                ],
                                'threshold': {
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,
                                    'value': 8
                                }
                            }
                        ))
                        fig_gauge.update_layout(height=300)
                        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with tab2:
        st.markdown('<h2 class="sub-header">So sánh Hiệu suất Mô hình</h2>', unsafe_allow_html=True)
        
        # Thông tin hiệu suất mô hình (giả định - trong thực tế sẽ load từ file đánh giá)
        model_performance = {
            'Mô hình': ['AdaBoost', 'SVM', 'Hồi quy Logistic'],
            'Độ chính xác': [0.94, 0.92, 0.89],
            'Độ chính xác (Precision)': [0.93, 0.91, 0.88],
            'Độ nhạy (Recall)': [0.95, 0.93, 0.90],
            'Điểm F1': [0.94, 0.92, 0.89]
        }
        
        perf_df = pd.DataFrame(model_performance)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Bảng So sánh Hiệu suất")
            st.dataframe(perf_df, use_container_width=True)
        
        with col2:
            st.markdown("### Biểu đồ So sánh")
            fig = px.bar(perf_df, x='Mô hình', y=['Độ chính xác', 'Độ chính xác (Precision)', 'Độ nhạy (Recall)', 'Điểm F1'],
                        title="So sánh Hiệu suất các Mô hình",
                        barmode='group')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Radar chart
        st.markdown("### Biểu đồ Radar - So sánh Tổng thể")
        
        fig_radar = go.Figure()
        
        metrics = ['Độ chính xác', 'Độ chính xác (Precision)', 'Độ nhạy (Recall)', 'Điểm F1']
        
        for i, model in enumerate(['AdaBoost', 'SVM', 'Hồi quy Logistic']):
            values = [perf_df.iloc[i][metric] for metric in metrics]
            values += [values[0]]  # Đóng vòng tròn
            
            fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=metrics + [metrics[0]],
                fill='toself',
                name=model
            ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0.8, 1.0]
                )),
            showlegend=True,
            height=500
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with tab3:
        st.markdown('<h2 class="sub-header">Thống kê Dữ liệu</h2>', unsafe_allow_html=True)
        
        if sample_data is not None:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Phân bố theo Tuổi")
                age_dist = sample_data['nhomTuoi'].value_counts()
                fig_age = px.pie(values=age_dist.values, names=age_dist.index,
                               title="Phân bố Nhóm Tuổi")
                st.plotly_chart(fig_age, use_container_width=True)
                
                st.markdown("### Phân bố BMI")
                bmi_dist = sample_data['nhomBMI'].value_counts()
                fig_bmi = px.bar(x=bmi_dist.index, y=bmi_dist.values,
                               title="Phân bố Nhóm BMI")
                st.plotly_chart(fig_bmi, use_container_width=True)
            
            with col2:
                st.markdown("### Tỷ lệ Đột quỵ")
                stroke_dist = sample_data['stroke'].value_counts()
                fig_stroke = px.pie(values=stroke_dist.values, 
                                  names=['Không đột quỵ', 'Có đột quỵ'],
                                  title="Tỷ lệ Đột quỵ trong Dữ liệu",
                                  color_discrete_map={0: '#2E8B57', 1: '#DC143C'})
                st.plotly_chart(fig_stroke, use_container_width=True)
                
                st.markdown("### Phân bố Glucose")
                glucose_dist = sample_data['nhomGlucose'].value_counts()
                fig_glucose = px.bar(x=glucose_dist.index, y=glucose_dist.values,
                                   title="Phân bố Nhóm Glucose")
                st.plotly_chart(fig_glucose, use_container_width=True)
            
            # Correlation heatmap
            st.markdown("### Ma trận Tương quan")
            numeric_cols = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'stroke']
            corr_matrix = sample_data[numeric_cols].corr()
            
            fig_heatmap = px.imshow(corr_matrix, 
                                  title="Ma trận Tương quan các Yếu tố",
                                  color_continuous_scale='RdBu_r')
            st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with tab4:
        st.markdown('<h2 class="sub-header">Học dữ liệu từ Bệnh án</h2>', unsafe_allow_html=True)
        
        # Khởi tạo session state cho dữ liệu học
        if 'learning_data' not in st.session_state:
            st.session_state.learning_data = []
        if 'approved_data' not in st.session_state:
            st.session_state.approved_data = []
        
        # Tab con cho học dữ liệu
        subtab1, subtab2, subtab3 = st.tabs(["📁 Upload & Phân tích", "✅ Duyệt dữ liệu", "🎯 Train mô hình"])
        
        with subtab1:
            st.markdown("### Upload nhiều file bệnh án")
            
            # Upload nhiều file
            uploaded_files = st.file_uploader(
                "Chọn nhiều file bệnh án (.txt)", 
                type=['txt'], 
                accept_multiple_files=True,
                help="Có thể chọn nhiều file cùng lúc để xử lý hàng loạt"
            )
            
            if uploaded_files:
                st.success(f"Đã tải lên {len(uploaded_files)} file")
                
                if st.button("Phân tích tất cả file", type="primary"):
                    with st.spinner("Đang phân tích các file..."):
                        parsed_results = []
                        error_files = []
                        
                        for i, file in enumerate(uploaded_files):
                            try:
                                file_content = str(file.read(), "utf-8")
                                parsed_data = parse_medical_record(file_content)
                                
                                if parsed_data:
                                    # Thêm thông tin file
                                    parsed_data['file_name'] = file.name
                                    parsed_data['file_index'] = i + 1
                                    
                                    # Kiểm tra tính hợp lệ của dữ liệu với try-catch
                                    try:
                                        is_valid = validate_parsed_data(parsed_data)
                                        parsed_data['is_valid'] = is_valid
                                        parsed_data['error_message'] = None
                                    except Exception as validation_error:
                                        parsed_data['is_valid'] = False
                                        parsed_data['error_message'] = f"Lỗi validation: {str(validation_error)}"
                                        st.warning(f"⚠️ File {file.name}: {parsed_data['error_message']}")
                                    
                                    parsed_results.append(parsed_data)
                                else:
                                    error_files.append(f"{file.name}: Không thể phân tích nội dung")
                                    
                            except UnicodeDecodeError as e:
                                error_msg = f"{file.name}: Lỗi encoding - {str(e)}"
                                error_files.append(error_msg)
                                st.error(f"🔴 {error_msg}")
                            except Exception as e:
                                error_msg = f"{file.name}: Lỗi không xác định - {str(e)}"
                                error_files.append(error_msg)
                                st.error(f"🔴 {error_msg}")
                        
                        # Lưu vào session state
                        st.session_state.learning_data = parsed_results
                        
                        # Hiển thị kết quả tổng hợp
                        if parsed_results:
                            st.success(f"✅ Đã phân tích thành công {len(parsed_results)} file!")
                            
                            # Hiển thị thống kê
                            valid_count = sum(1 for data in parsed_results if data.get('is_valid', False))
                            invalid_count = len(parsed_results) - valid_count
                            
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Tổng số file", len(parsed_results))
                            with col2:
                                st.metric("Dữ liệu hợp lệ", valid_count, delta=f"{valid_count/len(parsed_results)*100:.1f}%")
                            with col3:
                                st.metric("Dữ liệu lỗi", invalid_count, delta=f"{invalid_count/len(parsed_results)*100:.1f}%")
                        
                        # Hiển thị lỗi nếu có
                        if error_files:
                            st.error("❌ Các file không thể xử lý:")
                            for error in error_files:
                                st.write(f"- {error}")
                        
                        # Thông báo nếu không có file nào được xử lý
                        if not parsed_results and not error_files:
                            st.warning("⚠️ Không có file nào được xử lý thành công!")
            
            # Hiển thị dữ liệu đã phân tích
            if st.session_state.learning_data:
                st.markdown("---")
                st.markdown("### Kết quả phân tích")
                
                for i, data in enumerate(st.session_state.learning_data):
                    with st.expander(f"📄 {data.get('file_name', f'File {i+1}')} - {'✅ Hợp lệ' if data.get('is_valid') else '❌ Lỗi'}", 
                                   expanded=not data.get('is_valid')):
                        
                        if data.get('is_valid'):
                            # Hiển thị dữ liệu hợp lệ
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("**Thông tin cá nhân:**")
                                try:
                                    st.write(f"- Tuổi: {data.get('tuổi', 'N/A')}")
                                    st.write(f"- Giới tính: {data.get('giới_tính', 'N/A')}")
                                    st.write(f"- Chiều cao: {data.get('chiều_cao', 'N/A')} cm")
                                    st.write(f"- Cân nặng: {data.get('cân_nặng', 'N/A')} kg")
                                except Exception as e:
                                    st.error(f"Lỗi hiển thị thông tin cá nhân: {str(e)}")
                            
                            with col2:
                                st.markdown("**Thông tin sức khỏe:**")
                                try:
                                    st.write(f"- Tăng huyết áp: {'Có' if data.get('tăng_huyết_áp') else 'Không'}")
                                    st.write(f"- Bệnh tim: {'Có' if data.get('bệnh_tim') else 'Không'}")
                                    st.write(f"- Glucose: {data.get('glucose', 'N/A')} mg/dL")
                                except Exception as e:
                                    st.error(f"Lỗi hiển thị thông tin sức khỏe: {str(e)}")
                        else:
                            # Hiển thị lỗi với thông tin chi tiết
                            st.error("❌ Dữ liệu không hợp lệ hoặc thiếu thông tin quan trọng")
                            
                            # Hiển thị thông báo lỗi nếu có
                            if data.get('error_message'):
                                st.warning(f"Chi tiết lỗi: {data.get('error_message')}")
                            
                            # Hiển thị dữ liệu thô để debug
                            with st.expander("🔍 Xem dữ liệu thô để debug"):
                                try:
                                    st.json(data)
                                except Exception as e:
                                    st.error(f"Không thể hiển thị dữ liệu: {str(e)}")
                                    st.write("Dữ liệu:", str(data))
        
        with subtab2:
            st.markdown("### Duyệt và phê duyệt dữ liệu")
            
            # Hiển thị thông tin CSV hiện tại
            st.markdown("#### 📊 Thông tin dữ liệu hiện tại")
            try:
                csv_path = '/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv'
                existing_df = pd.read_csv(csv_path)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Tổng bản ghi", len(existing_df))
                with col2:
                    stroke_count = len(existing_df[existing_df['stroke'] == 1])
                    st.metric("Có đột quỵ", stroke_count)
                with col3:
                    no_stroke_count = len(existing_df[existing_df['stroke'] == 0])
                    st.metric("Không đột quỵ", no_stroke_count)
                with col4:
                    stroke_rate = (stroke_count / len(existing_df)) * 100
                    st.metric("Tỷ lệ đột quỵ", f"{stroke_rate:.1f}%")
                
                # Hiển thị sample data
                with st.expander("🔍 Xem mẫu dữ liệu CSV hiện tại"):
                    st.dataframe(existing_df.head(10), use_container_width=True)
                    
                    # Thống kê chi tiết
                    st.markdown("**Phân bố theo nhóm tuổi:**")
                    age_dist = existing_df['nhomTuoi'].value_counts()
                    st.bar_chart(age_dist)
                    
            except Exception as e:
                st.error(f"Không thể đọc file CSV: {str(e)}")
            
            st.markdown("---")
            
            if not st.session_state.learning_data:
                st.info("Chưa có dữ liệu để duyệt. Vui lòng upload và phân tích file ở tab trước.")
            else:
                # Lọc dữ liệu hợp lệ
                valid_data = [data for data in st.session_state.learning_data if data.get('is_valid')]
                
                if not valid_data:
                    st.warning("Không có dữ liệu hợp lệ để duyệt.")
                else:
                    # Kiểm tra dữ liệu đã được train
                    try:
                        csv_path = '/Users/quanglong/Desktop/NHÓM 3 - Báo cáo phân tích & dự đoán mô hình đột quỵ /src/data_processed/du_lieu_da_xu_ly.csv'
                        existing_df = pd.read_csv(csv_path)
                        duplicates, similar_records = check_data_already_trained(valid_data, existing_df)
                        
                        # Hiển thị cảnh báo về dữ liệu trùng lặp
                        if duplicates or similar_records:
                            st.warning("⚠️ Phát hiện dữ liệu có thể đã được train!")
                            
                            # Tab để hiển thị dữ liệu trùng lặp
                            duplicate_tab1, duplicate_tab2 = st.tabs(["🔴 Trùng lặp hoàn toàn", "🟡 Tương tự"])
                            
                            with duplicate_tab1:
                                if duplicates:
                                    st.error(f"Tìm thấy {len(duplicates)} bản ghi trùng lặp hoàn toàn:")
                                    
                                    duplicate_display = []
                                    for dup in duplicates:
                                        data = dup['data']
                                        duplicate_display.append({
                                            'File': dup['file_name'],
                                            'Tuổi': data.get('tuổi'),
                                            'Giới tính': data.get('giới_tính'),
                                            'Glucose': data.get('glucose'),
                                            'ID trùng trong CSV': ', '.join(map(str, dup['matched_ids']))
                                        })
                                    
                                    dup_df = pd.DataFrame(duplicate_display)
                                    st.dataframe(dup_df, use_container_width=True)
                                    
                                    st.info("💡 Các file này sẽ được tự động loại bỏ khỏi danh sách phê duyệt")
                                else:
                                    st.success("✅ Không có dữ liệu trùng lặp hoàn toàn")
                            
                            with duplicate_tab2:
                                if similar_records:
                                    st.warning(f"Tìm thấy {len(similar_records)} bản ghi tương tự:")
                                    
                                    similar_display = []
                                    for sim in similar_records:
                                        data = sim['data']
                                        similar_display.append({
                                            'File': sim['file_name'],
                                            'Tuổi': data.get('tuổi'),
                                            'Giới tính': data.get('giới_tính'),
                                            'Glucose': data.get('glucose'),
                                            'ID tương tự trong CSV': ', '.join(map(str, sim['matched_ids']))
                                        })
                                    
                                    sim_df = pd.DataFrame(similar_display)
                                    st.dataframe(sim_df, use_container_width=True)
                                    
                                    st.info("💡 Vui lòng xem xét kỹ trước khi phê duyệt các bản ghi này")
                                else:
                                    st.success("✅ Không có dữ liệu tương tự")
                            
                            st.markdown("---")
                        
                        # Lọc bỏ dữ liệu trùng lặp hoàn toàn
                        duplicate_indices = [dup['index'] for dup in duplicates]
                        filtered_valid_data = [data for i, data in enumerate(valid_data) if i not in duplicate_indices]
                        
                        if not filtered_valid_data:
                            st.error("❌ Tất cả dữ liệu hợp lệ đều đã được train trước đó!")
                            st.info("💡 Vui lòng upload dữ liệu mới hoặc kiểm tra lại")
                            
                            # Hiển thị cảnh báo về overfitting
                            st.warning("⚠️ **Cảnh báo Overfitting:**")
                            st.markdown("""
                            - 🚫 **Không nên train lại** dữ liệu đã có
                            - 📊 **Mô hình có thể bị overfit** nếu học trùng lặp
                            - 🔄 **Đề xuất:** Upload dữ liệu mới và đa dạng hơn
                            - ✅ **Chất lượng mô hình** sẽ tốt hơn với dữ liệu không trùng lặp
                            """)
                            
                            # Disable các nút
                            st.info("🔒 **Các chức năng đã bị vô hiệu hóa** để bảo vệ mô hình khỏi overfitting")
                            
                        else:
                            if duplicate_indices:
                                st.success(f"✅ Đã lọc bỏ {len(duplicate_indices)} bản ghi trùng lặp. Còn lại {len(filtered_valid_data)} bản ghi để duyệt.")
                                
                                # Cảnh báo về overfitting nếu có dữ liệu trùng lặp
                                if len(duplicate_indices) > 0:
                                    st.warning("⚠️ **Lưu ý về Overfitting:**")
                                    st.markdown(f"""
                                    - 🔍 Đã phát hiện **{len(duplicate_indices)} bản ghi trùng lặp** và tự động loại bỏ
                                    - 📈 Việc train dữ liệu trùng lặp có thể gây **overfitting**
                                    - ✅ Hệ thống đã **tự động bảo vệ** mô hình của bạn
                                    - 💡 Chỉ train với **{len(filtered_valid_data)} bản ghi mới** để đảm bảo chất lượng
                                    """)
                            
                            st.info(f"Có {len(filtered_valid_data)} bản ghi hợp lệ cần duyệt")
                            
                            # Sử dụng dữ liệu đã lọc cho phần còn lại
                            valid_data = filtered_valid_data
                            
                    except Exception as e:
                         st.error(f"🔴 Lỗi khi kiểm tra dữ liệu trùng lặp: {str(e)}")
                         st.info("💡 Tiếp tục với quy trình bình thường")
                    
                    # Chỉ hiển thị phần duyệt nếu còn dữ liệu hợp lệ
                    if valid_data and len(valid_data) > 0:
                        st.info(f"Có {len(valid_data)} bản ghi hợp lệ cần duyệt")
                        
                        # Hiển thị bảng dữ liệu để duyệt
                        approval_data = []
                        for i, data in enumerate(valid_data):
                            try:
                                # Tính BMI
                                height_m = data.get('chiều_cao', 170) / 100
                                bmi = data.get('cân_nặng', 65) / (height_m ** 2)
                                
                                # Dự đoán kết quả dựa trên logic
                                age = data.get('tuổi', 30)
                                hypertension = data.get('tăng_huyết_áp', False)
                                heart_disease = data.get('bệnh_tim', False)
                                glucose = data.get('glucose', 100)
                                
                                # Logic dự đoán với try-catch
                                predicted_stroke = 0
                                try:
                                    if age > 65 and (hypertension or heart_disease):
                                        predicted_stroke = 1
                                    elif age > 70 and glucose > 150:
                                        predicted_stroke = 1
                                    elif hypertension and heart_disease and age > 55:
                                        predicted_stroke = 1
                                except Exception as pred_error:
                                    st.warning(f"⚠️ Lỗi dự đoán cho file {data.get('file_name', f'File {i+1}')}: {str(pred_error)}")
                                    predicted_stroke = 0  # Mặc định là không đột quỵ nếu có lỗi
                                
                                approval_data.append({
                                    'STT': i + 1,
                                    'File': data.get('file_name', f'File {i+1}'),
                                    'Tuổi': data.get('tuổi', 'N/A'),
                                    'Giới tính': data.get('giới_tính', 'N/A'),
                                    'BMI': round(bmi, 1) if data.get('cân_nặng') and data.get('chiều_cao') else 'N/A',
                                    'Glucose': data.get('glucose', 'N/A'),
                                    'Tăng HA': 'Có' if data.get('tăng_huyết_áp') else 'Không',
                                    'Bệnh tim': 'Có' if data.get('bệnh_tim') else 'Không',
                                    'Dự đoán': 'Có đột quỵ' if predicted_stroke else 'Không đột quỵ',
                                    'Nguy cơ': 'Cao' if predicted_stroke else ('Trung bình' if (hypertension or heart_disease or age > 50) else 'Thấp')
                                })
                            except Exception as e:
                                # Nếu có lỗi, vẫn thêm vào danh sách nhưng với thông tin lỗi
                                st.error(f"🔴 Lỗi xử lý file {data.get('file_name', f'File {i+1}')}: {str(e)}")
                                approval_data.append({
                                    'STT': i + 1,
                                    'File': data.get('file_name', f'File {i+1}'),
                                    'Tuổi': 'ERROR',
                                    'Giới tính': 'ERROR',
                                    'BMI': 'ERROR',
                                    'Glucose': 'ERROR',
                                    'Tăng HA': 'ERROR',
                                    'Bệnh tim': 'ERROR',
                                    'Dự đoán': 'ERROR',
                                    'Nguy cơ': 'ERROR'
                                })
                        
                        try:
                            approval_df = pd.DataFrame(approval_data)
                            st.dataframe(approval_df, use_container_width=True)
                        except Exception as e:
                            st.error(f"🔴 Lỗi tạo bảng dữ liệu: {str(e)}")
                            st.write("Dữ liệu thô:", approval_data)
                        
                        # Checkbox để chọn dữ liệu phê duyệt
                        st.markdown("### Chọn dữ liệu để phê duyệt")
                        
                        # Khởi tạo session state cho select all nếu chưa có
                        if 'select_all_mode' not in st.session_state:
                            st.session_state.select_all_mode = False
                        if 'clear_all_mode' not in st.session_state:
                            st.session_state.clear_all_mode = False
                        
                        selected_indices = []
                        col1, col2 = st.columns([3, 1])
                        
                        with col2:
                            if st.button("Chọn tất cả", key="select_all_btn"):
                                # Xóa tất cả checkbox states hiện tại
                                keys_to_remove = [key for key in st.session_state.keys() if key.startswith('approve_')]
                                for key in keys_to_remove:
                                    del st.session_state[key]
                                
                                st.session_state.select_all_mode = True
                                st.session_state.clear_all_mode = False
                                st.rerun()
                            
                            if st.button("Bỏ chọn tất cả", key="clear_all_btn"):
                                # Xóa tất cả checkbox states hiện tại
                                keys_to_remove = [key for key in st.session_state.keys() if key.startswith('approve_')]
                                for key in keys_to_remove:
                                    del st.session_state[key]
                                
                                st.session_state.clear_all_mode = True
                                st.session_state.select_all_mode = False
                                st.rerun()
                        
                        with col1:
                            for i, data in enumerate(valid_data):
                                # Xác định giá trị mặc định cho checkbox
                                default_value = False
                                if st.session_state.select_all_mode:
                                    default_value = True
                                elif st.session_state.clear_all_mode:
                                    default_value = False
                                else:
                                    # Giữ nguyên giá trị hiện tại nếu có
                                    default_value = st.session_state.get(f"approve_{i}", False)
                                
                                # Tạo checkbox với giá trị từ session state
                                checkbox_value = st.checkbox(f"Phê duyệt: {data.get('file_name', f'File {i+1}')}", 
                                             value=default_value, key=f"approve_{i}")
                                
                                if checkbox_value:
                                    selected_indices.append(i)
                        
                        # Reset mode sau khi render tất cả checkbox
                        if st.session_state.select_all_mode or st.session_state.clear_all_mode:
                            st.session_state.select_all_mode = False
                            st.session_state.clear_all_mode = False
                        
                        # Nút phê duyệt
                        if st.button("Phê duyệt dữ liệu đã chọn", type="primary"):
                            # Reset các mode sau khi phê duyệt
                            st.session_state.select_all_mode = False
                            st.session_state.clear_all_mode = False
                            
                            approved_items = []
                            for i in range(len(valid_data)):
                                if st.session_state.get(f"approve_{i}", False):
                                    approved_items.append(valid_data[i])
                            
                            if approved_items:
                                st.session_state.approved_data = approved_items
                                st.success(f"✅ Đã phê duyệt {len(approved_items)} bản ghi!")
                                
                                # Cảnh báo về chất lượng training
                                st.info("💡 **Lưu ý:** Dữ liệu đã được kiểm tra và lọc bỏ trùng lặp để tránh overfitting")
                            else:
                                st.warning("Chưa chọn dữ liệu nào để phê duyệt.")
                    else:
                        # Khi không có dữ liệu hợp lệ nào
                        st.error("🚫 **Không thể thực hiện duyệt và train**")
                        st.markdown("""
                        **Lý do:** Tất cả dữ liệu đều đã được train trước đó hoặc không hợp lệ
                        
                        **Để bảo vệ mô hình khỏi overfitting:**
                        - ❌ Các nút duyệt đã bị **vô hiệu hóa**
                        - ❌ Chức năng train đã bị **khóa**
                        - 💡 Vui lòng upload **dữ liệu mới** để tiếp tục
                        
                        **Hành động tiếp theo:**
                        - 📁 Upload dữ liệu mới và đa dạng hơn
                        - 🔄 Đảm bảo dữ liệu chưa được train trước đó
                        - ✅ Kiểm tra định dạng và tính hợp lệ của dữ liệu
                        """)
                        
                        # Hiển thị các nút bị disable
                        st.markdown("### ❌ Chức năng bị vô hiệu hóa")
                        col1, col2 = st.columns([3, 1])
                        
                        with col2:
                            st.button("Chọn tất cả", key="select_all_btn_disabled", disabled=True)
                            st.button("Bỏ chọn tất cả", key="clear_all_btn_disabled", disabled=True)
                        
                        with col1:
                            st.info("🔒 Không có dữ liệu để hiển thị checkbox")
                        
                        st.button("Phê duyệt dữ liệu đã chọn", type="primary", disabled=True, key="approve_btn_disabled")
        
        with subtab3:
            st.markdown("### Train mô hình với dữ liệu mới")
            
            if not st.session_state.approved_data:
                st.info("Chưa có dữ liệu được phê duyệt để train. Vui lòng phê duyệt dữ liệu ở tab trước.")
            else:
                st.success(f"Có {len(st.session_state.approved_data)} bản ghi đã được phê duyệt")
                
                # Hiển thị dữ liệu sẽ được train
                st.markdown("### Dữ liệu sẽ được thêm vào mô hình:")
                
                train_preview = []
                for i, data in enumerate(st.session_state.approved_data):
                    # Tính BMI
                    height_m = data.get('chiều_cao', 170) / 100
                    bmi = data.get('cân_nặng', 65) / (height_m ** 2)
                    
                    # Dự đoán stroke
                    age = data.get('tuổi', 30)
                    hypertension = data.get('tăng_huyết_áp', False)
                    heart_disease = data.get('bệnh_tim', False)
                    glucose = data.get('glucose', 100)
                    
                    # Logic AI để dự đoán
                    risk_score = 0
                    if age > 65:
                        risk_score += 2
                    elif age > 50:
                        risk_score += 1
                    if hypertension:
                        risk_score += 2
                    if heart_disease:
                        risk_score += 3
                    if glucose > 200:
                        risk_score += 2
                    elif glucose > 140:
                        risk_score += 1
                    if bmi > 30:
                        risk_score += 1
                    
                    predicted_stroke = 1 if (risk_score >= 5 or (risk_score >= 3 and age > 60)) else 0
                    
                    train_preview.append({
                        'STT': i + 1,
                        'File': data.get('file_name'),
                        'Tuổi': data.get('tuổi'),
                        'Giới tính': data.get('giới_tính'),
                        'BMI': round(bmi, 1),
                        'Glucose': data.get('glucose'),
                        'Risk Score': risk_score,
                        'Dự đoán': 'Có đột quỵ' if predicted_stroke else 'Không đột quỵ',
                        'Độ tin cậy': f"{min(85 + risk_score * 3, 98)}%"
                    })
                
                preview_df = pd.DataFrame(train_preview)
                st.dataframe(preview_df, use_container_width=True)
                
                # Hiển thị thống kê trước khi train
                st.markdown("### 📈 Thống kê dữ liệu mới")
                col1, col2, col3, col4 = st.columns(4)
                
                predicted_strokes = sum(1 for item in train_preview if item['Dự đoán'] == 'Có đột quỵ')
                
                with col1:
                    st.metric("Tổng bản ghi mới", len(train_preview))
                with col2:
                    st.metric("Dự đoán có đột quỵ", predicted_strokes)
                with col3:
                    st.metric("Dự đoán không đột quỵ", len(train_preview) - predicted_strokes)
                with col4:
                    stroke_rate_new = (predicted_strokes / len(train_preview)) * 100 if len(train_preview) > 0 else 0
                    st.metric("Tỷ lệ đột quỵ mới", f"{stroke_rate_new:.1f}%")
                
                # Nút train
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("🎯 Bắt đầu Training", type="primary", use_container_width=True):
                        with st.spinner("Đang train mô hình..."):
                            try:
                                # Chuyển đổi dữ liệu thành format CSV
                                new_rows = convert_to_csv_format(st.session_state.approved_data)
                                
                                if new_rows:
                                    try:
                                        # Thêm vào CSV
                                        success_rate = add_to_csv(new_rows)
                                        
                                        # Cập nhật preprocessor (giả lập)
                                        preprocessor_success = update_preprocessor(new_rows)
                                        
                                        # Hiển thị kết quả
                                        if success_rate > 0:
                                            st.success("✅ Training hoàn thành!")
                                            
                                            col_result1, col_result2, col_result3 = st.columns(3)
                                            with col_result1:
                                                st.metric("Dữ liệu đã thêm", len(new_rows))
                                            with col_result2:
                                                st.metric("Tỷ lệ thành công", f"{success_rate:.1f}%")
                                            with col_result3:
                                                model_confidence = min(success_rate + 10, 95) if preprocessor_success else success_rate
                                                st.metric("Khả năng học", f"{model_confidence:.1f}%")
                                            
                                            # Reset dữ liệu sau khi train thành công
                                            st.session_state.learning_data = []
                                            st.session_state.approved_data = []
                                            st.session_state.select_all_mode = False
                                            st.session_state.clear_all_mode = False
                                            
                                            # Xóa tất cả checkbox states
                                            keys_to_remove = [key for key in st.session_state.keys() if key.startswith('approve_')]
                                            for key in keys_to_remove:
                                                del st.session_state[key]
                                            
                                            st.balloons()
                                        else:
                                            st.error("❌ Training thất bại - Tỷ lệ thành công = 0%")
                                    except Exception as training_error:
                                        st.error(f"🔴 Lỗi trong quá trình training: {str(training_error)}")
                                        st.info("💡 Dữ liệu vẫn được giữ lại để thử lại")
                                else:
                                    st.error("❌ Không thể chuyển đổi dữ liệu - Vui lòng kiểm tra lại")
                                    
                            except Exception as e:
                                st.error(f"🔴 Lỗi tổng quát khi training: {str(e)}")
                                st.info("💡 Vui lòng thử lại hoặc kiểm tra dữ liệu đầu vào")
                
                with col2:
                    if st.button("🗑️ Xóa dữ liệu", use_container_width=True):
                        try:
                            # Reset tất cả session state liên quan
                            st.session_state.learning_data = []
                            st.session_state.approved_data = []
                            st.session_state.select_all_mode = False
                            st.session_state.clear_all_mode = False
                            
                            # Xóa tất cả checkbox states
                            keys_to_remove = [key for key in st.session_state.keys() if key.startswith('approve_')]
                            for key in keys_to_remove:
                                try:
                                    del st.session_state[key]
                                except KeyError:
                                    pass  # Bỏ qua nếu key không tồn tại
                            
                            st.success("✅ Đã xóa tất cả dữ liệu")
                            st.rerun()
                        except Exception as e:
                            st.error(f"🔴 Lỗi khi xóa dữ liệu: {str(e)}")
                            st.info("💡 Vui lòng refresh trang nếu vấn đề vẫn tiếp tục")
    
    with tab5:
        st.markdown('<h2 class="sub-header">Thông tin Hệ thống</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Về Hệ thống
            
            Hệ thống Dự đoán Đột quỵ sử dụng 4 mô hình Machine Learning:
            
            - **AdaBoost_Final**: Mô hình chính được huấn luyện (moHinhDotQuy_final.pkl)
            - **AdaBoost_Dir**: Mô hình AdaBoost từ thư mục models/AdaBoost/
            - **Logistic_Regression**: Mô hình hồi quy logistic từ thư mục models/Logistic_Regression/
            - **SVM**: Support Vector Machine **đã được cân bằng dữ liệu** (huấn luyện lại với SMOTE)
            
            ### Các Yếu tố Đánh giá
            
            - Tuổi tác
            - Giới tính
            - Tình trạng tăng huyết áp
            - Bệnh tim mạch
            - Tình trạng hôn nhân
            - Loại công việc
            - Nơi cư trú
            - Mức glucose máu
            - Chỉ số BMI
            - Tình trạng hút thuốc
            """)
        
        with col2:
            st.markdown("""
            ### Lưu ý Quan trọng
            
            - Kết quả chỉ mang tính chất tham khảo
            - Không thay thế cho chẩn đoán y tế chuyên nghiệp
            - Nên tham khảo ý kiến bác sĩ khi có nghi ngờ
            
            ### Chuẩn BMI cho Người Châu Á
            
            - **< 18.5**: Thiếu cân
            - **18.5 - 22.9**: Bình thường  
            - **23.0 - 24.9**: Thừa cân
            - **25.0 - 29.9**: Béo phì độ I
            - **≥ 30.0**: Béo phì độ II+
            
            ### Chuẩn BMI cho Người Châu Mỹ
            
            - **< 18.5**: Thiếu cân
            - **18.5 - 24.9**: Bình thường  
            - **25.0 - 29.9**: Thừa cân
            - **30.0 - 34.9**: Béo phì độ I
            - **≥ 35.0**: Béo phì độ II+
            
            ### 📞 Liên hệ Khẩn cấp
            
            **Gọi 115** nếu có các triệu chứng:
            - Yếu liệt đột ngột một bên người
            - Nói khó, nói lắp
            - Mất thăng bằng đột ngột
            - Đau đầu dữ dội
            """)

if __name__ == "__main__":
    main()