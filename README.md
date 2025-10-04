# 🏥 Dự Án Dự Đoán Nguy Cơ Đột Quỵ - Healthcare Stroke Prediction

## 📋 Tổng Quan Dự Án

Dự án này sử dụng Machine Learning để dự đoán nguy cơ đột quỵ dựa trên các yếu tố sức khỏe và lối sống của bệnh nhân. Dataset chứa thông tin của 5,110 bệnh nhân với 11 thuộc tính khác nhau và biến mục tiêu là khả năng bị đột quỵ.

## 🎯 Mục Tiêu

- **Phân tích khám phá dữ liệu (EDA)**: Hiểu rõ các yếu tố nguy cơ gây đột quỵ
- **Xây dựng mô hình dự đoán**: Sử dụng nhiều thuật toán ML để dự đoán nguy cơ đột quỵ
- **Đánh giá hiệu suất**: So sánh các mô hình và chọn ra mô hình tối ưu
- **Ứng dụng thực tế**: Tạo công cụ hỗ trợ chẩn đoán sớm

## 📊 Thông Tin Dataset

### Đặc điểm chung:
- **Tổng số mẫu**: 5,110 bệnh nhân
- **Số ca đột quỵ**: 249 ca (4.87%)
- **Số ca không đột quỵ**: 4,861 ca (95.13%)
- **Tỷ lệ mất cân bằng**: Cao (1:19.5)

### Các thuộc tính:
1. **id**: Mã định danh bệnh nhân
2. **gender**: Giới tính (Male/Female/Other)
3. **age**: Tuổi (0.08-82 tuổi)
4. **hypertension**: Tăng huyết áp (0: Không, 1: Có)
5. **heart_disease**: Bệnh tim (0: Không, 1: Có)
6. **ever_married**: Tình trạng hôn nhân (Yes/No)
7. **work_type**: Loại công việc (Private/Self-employed/Govt_job/children/Never_worked)
8. **Residence_type**: Nơi cư trú (Urban/Rural)
9. **avg_glucose_level**: Mức glucose trung bình (55.12-271.74)
10. **bmi**: Chỉ số BMI (10.3-97.6, có giá trị thiếu)
11. **smoking_status**: Tình trạng hút thuốc (formerly smoked/never smoked/smokes/Unknown)
12. **stroke**: Biến mục tiêu (0: Không đột quỵ, 1: Đột quỵ)

## 🗂️ Cấu Trúc Dự Án

```
HeathCare---Dataset/
├── data/
│   ├── raw/                    # Dữ liệu gốc
│   └── processed/              # Dữ liệu đã xử lý
├── notebooks/                  # Jupyter notebooks
│   ├── 01_EDA.ipynb           # Khám phá dữ liệu
│   ├── 02_Preprocessing.ipynb  # Tiền xử lý
│   ├── 03_Modeling.ipynb      # Xây dựng mô hình
│   └── 04_Deployment_Complete.ipynb # Hướng dẫn triển khai
├── src/                       # Source code
│   ├── data_preprocessing.py   # Xử lý dữ liệu
│   ├── feature_engineering.py # Tạo đặc trưng
│   ├── model_training.py      # Huấn luyện mô hình
│   └── evaluation.py          # Đánh giá mô hình
├── scripts/                   # Deployment scripts
│   ├── run_streamlit.sh       # Chạy Streamlit app
│   ├── run_flask.sh          # Chạy Flask API
│   └── deploy_docker.sh      # Docker deployment
├── config/                    # Configuration files
├── tests/                     # Unit tests
├── models/                    # Mô hình đã huấn luyện
├── results/                   # Kết quả và biểu đồ
├── docs/                      # Tài liệu
│   └── table_of_contents.md   # Mục lục chi tiết
├── img/                       # Hình ảnh
├── requirements.txt           # Dependencies
└── README.md                  # File này
```

## 🚀 Cài Đặt và Sử Dụng

### 1. Clone repository
```bash
git clone https://github.com/yourusername/HeathCare---Dataset.git
cd HeathCare---Dataset
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Chạy Jupyter Notebook
```bash
jupyter notebook
```

### 4. Thực hiện phân tích
- Bắt đầu với `notebooks/01_EDA.ipynb` để khám phá dữ liệu
- Tiếp tục với các notebook theo thứ tự số
- Xem `notebooks/04_Deployment_Complete.ipynb` để triển khai mô hình

### 5. Triển khai ứng dụng (Tùy chọn)
```bash
# Chạy Streamlit app
chmod +x scripts/run_streamlit.sh
./scripts/run_streamlit.sh

# Hoặc chạy Flask API
chmod +x scripts/run_flask.sh
./scripts/run_flask.sh

# Triển khai với Docker
chmod +x scripts/deploy_docker.sh
./scripts/deploy_docker.sh
```

## 🔬 Phương Pháp Nghiên Cứu

### 1. Khám Phá Dữ Liệu (EDA)
- Phân tích phân bố các biến
- Tìm hiểu mối tương quan
- Xác định các yếu tố nguy cơ chính
- Phát hiện dữ liệu ngoại lai

### 2. Tiền Xử Lý Dữ Liệu
- Xử lý giá trị thiếu trong BMI
- Mã hóa biến phân loại
- Chuẩn hóa dữ liệu số
- Xử lý mất cân bằng dữ liệu (SMOTE, undersampling)

### 3. Xây Dựng Mô Hình
- **Logistic Regression**: Mô hình baseline
- **Random Forest**: Ensemble method
- **XGBoost**: Gradient boosting
- **LightGBM**: Efficient gradient boosting
- **K-Nearest Neighbors**: Instance-based learning

### 4. Đánh Giá Mô Hình
- **Metrics**: Accuracy, Precision, Recall, F1-score, AUC-ROC
- **Cross-validation**: 5-fold stratified CV
- **Feature Importance**: Phân tích tầm quan trọng của các đặc trưng

## 📈 Kết Quả Dự Kiến

### Các yếu tố nguy cơ chính:
- Tuổi cao (>65 tuổi)
- Tăng huyết áp
- Bệnh tim mạch
- Mức glucose cao
- BMI cao
- Tình trạng hút thuốc

### Hiệu suất mô hình mong đợi:
- **AUC-ROC**: > 0.85
- **Precision**: > 0.70 (giảm false positive)
- **Recall**: > 0.75 (phát hiện được nhiều ca đột quỵ)
- **F1-score**: > 0.72

## 🛠️ Công Nghệ Sử Dụng

### Core Libraries:
- **Python 3.8+**
- **Pandas & NumPy**: Xử lý dữ liệu
- **Matplotlib & Seaborn**: Visualization
- **Plotly**: Interactive visualizations
- **Scikit-learn**: Machine Learning
- **XGBoost & LightGBM**: Advanced ML algorithms
- **Imbalanced-learn**: Xử lý dữ liệu mất cân bằng
- **Jupyter Notebook**: Interactive development

### Deployment & Web Apps:
- **Streamlit**: Web application framework
- **Flask**: REST API development
- **Docker**: Containerization
- **Gunicorn**: WSGI HTTP Server

### Development Tools:
- **Pytest**: Unit testing
- **Black**: Code formatting
- **Flake8**: Code linting

## 📝 Nhiệm Vụ Cụ Thể

### Task 1: Exploratory Data Analysis (EDA)
- [ ] Phân tích thống kê mô tả cho tất cả các biến
- [ ] Tạo visualization cho phân bố dữ liệu
- [ ] Phân tích correlation matrix
- [ ] Tìm hiểu mối quan hệ giữa các yếu tố và đột quỵ
- [ ] Phát hiện và xử lý outliers

### Task 2: Data Preprocessing
- [ ] Xử lý missing values trong cột BMI
- [ ] One-hot encoding cho categorical variables
- [ ] Feature scaling/normalization
- [ ] Train-test split với stratification
- [ ] Áp dụng SMOTE để cân bằng dữ liệu

### Task 3: Model Development
- [ ] Implement baseline Logistic Regression
- [ ] Xây dựng Random Forest với hyperparameter tuning
- [ ] Triển khai XGBoost và LightGBM
- [ ] So sánh hiệu suất các mô hình
- [ ] Feature importance analysis

### Task 4: Model Evaluation & Deployment
- [x] Cross-validation và model selection
- [x] Tạo confusion matrix và classification report
- [x] ROC curve và AUC analysis
- [x] Model interpretation và explainability
- [x] Tạo prediction pipeline
- [x] Streamlit web application
- [x] Flask REST API
- [x] Docker containerization
- [x] Deployment documentation

## 🤝 Đóng Góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📄 License

Dự án này được phân phối dưới MIT License. Xem `LICENSE` để biết thêm thông tin.

## 📞 Liên Hệ

- **Tác giả**: [Tên của bạn]
- **Email**: [email@example.com]
- **GitHub**: [https://github.com/yourusername]

## 🙏 Acknowledgments

- Dataset được cung cấp bởi [Kaggle Stroke Prediction Dataset]
- Cảm ơn cộng đồng Machine Learning và Healthcare Analytics
- Tham khảo các nghiên cứu về dự đoán đột quỵ trong y học

---

**⚠️ Lưu ý**: Dự án này chỉ mang tính chất nghiên cứu và học tập. Không sử dụng để thay thế chẩn đoán y khoa chuyên nghiệp.