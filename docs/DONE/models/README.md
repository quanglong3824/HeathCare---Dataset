# Thư mục Models

## Mô tả
Thư mục này chứa các mô hình machine learning đã được train cho dự án phân tích dữ liệu đột quỵ.

## Cấu trúc thư mục
```
models/
├── README.md                 # File hướng dẫn này
├── best_model.pkl           # Mô hình tốt nhất được chọn
├── model_info.pkl           # Thông tin về mô hình (metrics, parameters)
├── preprocessor.pkl         # Pipeline preprocessing
├── feature_names.pkl        # Tên các features
└── training_history/        # Lịch sử training các mô hình
    ├── logistic_regression.pkl
    ├── random_forest.pkl
    ├── xgboost.pkl
    └── ...
```

## Cách sử dụng

### Load mô hình đã train
```python
import joblib

# Load mô hình tốt nhất
model = joblib.load('models/best_model.pkl')

# Load preprocessor
preprocessor = joblib.load('models/preprocessor.pkl')

# Load thông tin mô hình
model_info = joblib.load('models/model_info.pkl')
```

### Dự đoán cho dữ liệu mới
```python
# Preprocessing dữ liệu mới
X_processed = preprocessor.transform(X_new)

# Dự đoán
predictions = model.predict(X_processed)
probabilities = model.predict_proba(X_processed)
```

## Thông tin mô hình
- **Loại bài toán**: Binary Classification (Dự đoán nguy cơ đột quỵ)
- **Target variable**: stroke (0: Không đột quỵ, 1: Có đột quỵ)
- **Features**: 11 đặc trưng y tế
- **Preprocessing**: StandardScaler, OneHotEncoder, SMOTE
- **Evaluation metrics**: F1-Score, ROC-AUC, Precision, Recall

## Lưu ý quan trọng
1. **Chỉ sử dụng cho mục đích nghiên cứu và học tập**
2. **Không thay thế cho chẩn đoán y tế chuyên nghiệp**
3. **Cần validation thêm trước khi ứng dụng thực tế**
4. **Tuân thủ quy định về bảo mật dữ liệu y tế**

## Cập nhật mô hình
Khi có dữ liệu mới hoặc cần cải thiện mô hình:
1. Chạy lại notebook 03_xayDungVaDanhGiaMoHinh.ipynb
2. So sánh hiệu suất với mô hình hiện tại
3. Backup mô hình cũ trước khi thay thế
4. Cập nhật file model_info.pkl

## Liên hệ
Nếu có thắc mắc về mô hình, vui lòng liên hệ team phát triển.