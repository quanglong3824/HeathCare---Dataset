# 🏥 Healthcare Dataset - Dự đoán Nguy cơ Đột quỵ

## 📋 Giới thiệu

Dự án này sử dụng Machine Learning để phân tích và dự đoán nguy cơ đột quỵ dựa trên các yếu tố y tế và lối sống của bệnh nhân. Hệ thống bao gồm một ứng dụng web tương tác được xây dựng bằng Streamlit, cho phép người dùng nhập thông tin bệnh nhân và nhận được dự đoán nguy cơ đột quỵ theo thời gian thực.

### 🎯 Mục tiêu chính
- Phân tích dữ liệu y tế để hiểu các yếu tố nguy cơ đột quỵ
- Xây dựng mô hình Machine Learning để dự đoán nguy cơ đột quỵ
- Tạo ứng dụng web thân thiện với người dùng
- Cung cấp công cụ hỗ trợ quyết định y tế

### 🔬 Phương pháp nghiên cứu
- **Khám phá và làm sạch dữ liệu**: Phân tích EDA, xử lý missing values, outliers
- **Phân tích thống kê và trực quan hóa**: Tạo các biểu đồ và insights từ dữ liệu
- **Xây dựng và đánh giá mô hình**: So sánh nhiều thuật toán ML khác nhau
- **Triển khai ứng dụng**: Tạo giao diện web để sử dụng mô hình

## 📁 Cấu trúc Dự án

```
HeathCare---Dataset/
├── 📊 app/                          # Ứng dụng web Streamlit
│   ├── app.py                       # File chính của ứng dụng
│   └── requirements.txt             # Dependencies cho ứng dụng
├── 📚 data_learning/                # Dữ liệu học tập (bệnh án mẫu)
│   ├── benh_an_hoc_*.txt           # 42 bệnh án học tập
│   ├── benh_an_stroke_*.txt        # 35 bệnh án đột quỵ
│   └── benh_an_edge_case.txt       # Trường hợp biên
├── 🔄 data_processed/               # Dữ liệu đã xử lý
│   ├── du_lieu_da_xu_ly.csv        # Dataset chính đã làm sạch
│   └── healthcare-dataset-stroke-data.csv.xls
├── 🧪 data_test/                    # Dữ liệu test
│   └── benh_an_*.txt               # 11 bệnh án test với các trường hợp khác nhau
├── 🤖 models/                       # Mô hình Machine Learning
│   ├── AdaBoost/                   # Mô hình AdaBoost
│   ├── Logistic_Regression/        # Mô hình Logistic Regression  
│   ├── SVM/                        # Mô hình Support Vector Machine
│   └── README.md                   # Hướng dẫn sử dụng models
├── 🐍 python/                       # Jupyter Notebooks phân tích
│   ├── 01_khamPhaVaLamSachDuLieu.ipynb
│   ├── 02_phanTichThongKeVaTrucQuanHoa.ipynb
│   ├── 03_xayDungVaDanhGiaMoHinh.ipynb
│   └── 04_ketLuanVaDeXuat.ipynb
├── 📄 BÁO CÁO PHÂN TÍCH - NHÓM 3.docx
├── 📊 presentation.09-31-21-812_1.pptx
└── 📖 README.md                     # File này
```

## 🚀 Hướng dẫn Cài đặt và Chạy

### Yêu cầu hệ thống
- Python 3.8 hoặc cao hơn
- pip (Python package manager)

### Bước 1: Clone repository
```bash
git clone https://github.com/your-username/HeathCare---Dataset.git
cd HeathCare---Dataset
```

### Bước 2: Cài đặt dependencies
```bash
cd app
pip install -r requirements.txt
```

### Bước 3: Chạy ứng dụng web
```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại địa chỉ: `http://localhost:8501`

### Bước 4: Chạy Jupyter Notebooks (tùy chọn)
```bash
cd ../python
jupyter notebook
```

## 📊 Dataset và Features

### Thông tin Dataset
- **Nguồn**: Healthcare Dataset Stroke Data
- **Số lượng mẫu**: ~5,000 bệnh nhân
- **Số features**: 11 đặc trưng y tế
- **Target**: Nguy cơ đột quỵ (0: Không, 1: Có)

### Các đặc trưng chính
1. **Thông tin cá nhân**:
   - `age`: Tuổi
   - `gender`: Giới tính
   - `hypertension`: Tăng huyết áp
   - `heart_disease`: Bệnh tim

2. **Thông tin sức khỏe**:
   - `avg_glucose_level`: Mức glucose trung bình
   - `bmi`: Chỉ số BMI
   - `smoking_status`: Tình trạng hút thuốc

3. **Thông tin xã hội**:
   - `work_type`: Loại công việc
   - `Residence_type`: Nơi cư trú
   - `ever_married`: Tình trạng hôn nhân

## 🔬 Quy trình Phân tích

### 1. Khám phá và Làm sạch Dữ liệu
- Phân tích cấu trúc và chất lượng dữ liệu
- Xử lý missing values và outliers
- Feature engineering và transformation

### 2. Phân tích Thống kê và Trực quan hóa
- Exploratory Data Analysis (EDA)
- Phân tích correlation và distribution
- Tạo insights và patterns từ dữ liệu

### 3. Xây dựng và Đánh giá Mô hình
- So sánh nhiều thuật toán: Logistic Regression, SVM, AdaBoost, Random Forest
- Hyperparameter tuning
- Cross-validation và model evaluation
- Feature importance analysis

### 4. Kết luận và Đề xuất
- Tổng kết kết quả và insights
- Đề xuất cải tiến và ứng dụng thực tế

## 🎯 Tính năng Ứng dụng Web

### 🏠 Trang chủ
- Giới thiệu về hệ thống
- Thống kê tổng quan về dataset
- Hướng dẫn sử dụng

### 🔮 Dự đoán Nguy cơ
- Form nhập thông tin bệnh nhân
- Dự đoán nguy cơ đột quỵ theo thời gian thực
- Hiển thị xác suất và mức độ nguy cơ
- Giải thích kết quả dự đoán

### 📊 Phân tích Dữ liệu
- Biểu đồ thống kê tương tác
- Phân tích correlation matrix
- Distribution plots cho các features
- Feature importance visualization

### 📈 So sánh Mô hình
- Bảng so sánh performance các mô hình
- ROC curves và confusion matrices
- Metrics chi tiết (Accuracy, Precision, Recall, F1-score)

### 📋 Phân tích Batch
- Upload file CSV để dự đoán hàng loạt
- Export kết quả dự đoán
- Thống kê tổng quan cho batch data

## 🛠️ Công nghệ Sử dụng

### Machine Learning
- **scikit-learn**: Thuật toán ML và preprocessing
- **pandas**: Data manipulation và analysis
- **numpy**: Numerical computing

### Visualization
- **plotly**: Interactive charts
- **seaborn**: Statistical visualization
- **matplotlib**: Basic plotting

### Web Application
- **streamlit**: Web framework
- **joblib**: Model serialization

## 📈 Kết quả và Performance

### Mô hình tốt nhất
- **Thuật toán**: [Sẽ được cập nhật sau khi chạy notebook 03]
- **Accuracy**: [Sẽ được cập nhật]
- **Precision**: [Sẽ được cập nhật]
- **Recall**: [Sẽ được cập nhật]
- **F1-Score**: [Sẽ được cập nhật]

### Insights chính
- [Sẽ được cập nhật sau khi hoàn thành phân tích]

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp cho dự án! Vui lòng:

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📝 License

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 👥 Tác giả

**Nhóm 3 - Phân tích Dữ liệu Y tế**

- 👨‍💻 [Tên thành viên 1] - [Email/GitHub]
- 👩‍💻 [Tên thành viên 2] - [Email/GitHub]  
- 👨‍💻 [Tên thành viên 3] - [Email/GitHub]

## 📞 Liên hệ

Nếu bạn có bất kỳ câu hỏi nào về dự án, vui lòng liên hệ:

- 📧 Email: [your-email@example.com]
- 🐙 GitHub Issues: [Link to issues page]
- 💬 Discussion: [Link to discussions]

## 🙏 Lời cảm ơn

- Cảm ơn cộng đồng Machine Learning và Healthcare Analytics
- Cảm ơn các tác giả của dataset gốc
- Cảm ơn các thư viện mã nguồn mở đã sử dụng

---

⭐ **Nếu dự án này hữu ích cho bạn, hãy cho chúng tôi một star!** ⭐