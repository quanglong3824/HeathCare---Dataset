# CHƯƠNG 4: XÂY DỰNG VÀ ĐÁNH GIÁ MÔ HÌNH DỰ ĐOÁN

Chương này trình bày chi tiết quá trình xây dựng, huấn luyện và đánh giá các mô hình học máy nhằm dự đoán nguy cơ đột quỵ. Dựa trên những phân tích từ các chương trước, các bước được thực hiện một cách có hệ thống để tìm ra mô hình hoạt động hiệu quả nhất cho bài toán này.

## 4.1. Chuẩn bị dữ liệu cho Machine Learning

### 4.1.1. Lựa chọn biến và xác định tập features (X) và target (y)

Tập Features (X): Bao gồm tất cả các biến độc lập trong tập dữ liệu đã qua xử lý (`du_lieu_da_xu_ly.csv`), ngoại trừ các biến nhóm đã được tạo (`nhomTuoi`, `nhomBMI`, `nhomGlucose`) để tránh đa cộng tuyến và dư thừa thông tin.
Biến Mục tiêu (y): Là cột `stroke`, với giá trị 1 (có đột quỵ) và 0 (không đột quỵ).

### 4.1.2. Phân chia tập dữ liệu (Training và Test set)

Tập dữ liệu được phân chia thành hai tập:

Tập huấn luyện (Training set): Chiếm 80% dữ liệu, được sử dụng để huấn luyện các mô hình.
Tập kiểm tra (Test set): Chiếm 20% dữ liệu còn lại, được giữ riêng và chỉ sử dụng một lần duy nhất để đánh giá hiệu suất cuối cùng của mô hình tốt nhất. Điều này đảm bảo kết quả đánh giá là khách quan.

Việc phân chia được thực hiện theo phương pháp `stratified sampling` (lấy mẫu phân tầng) dựa trên biến mục tiêu `y` để đảm bảo tỷ lệ các lớp (có/không đột quỵ) trong cả hai tập huấn luyện và kiểm tra là tương đương nhau.

### 4.1.3. Xây dựng quy trình tiền xử lý (Preprocessing Pipeline)

Để đảm bảo các bước tiền xử lý được áp dụng một cách nhất quán và tự động cho cả dữ liệu huấn luyện và kiểm tra, một `Pipeline` của Scikit-learn đã được xây dựng. Quy trình này bao gồm hai bước chính:

1.  Mã hóa biến định tính (Categorical Encoding): Các biến có kiểu dữ liệu `object` (ví dụ: `gender`, `work_type`) được chuyển đổi thành dạng số bằng phương pháp One-Hot Encoding. Phương pháp này tạo ra các cột nhị phân mới cho mỗi giá trị của biến, phù hợp cho các thuật toán tuyến tính và dựa trên cây.
2.  Co giãn dữ liệu (Data Scaling): Các biến số (ví dụ: `age`, `avg_glucose_level`, `bmi`) được chuẩn hóa bằng StandardScaler. Kỹ thuật này biến đổi dữ liệu sao cho có giá trị trung bình bằng 0 và độ lệch chuẩn bằng 1, giúp các thuật toán nhạy cảm với thang đo (như Logistic Regression, SVM) hoạt động hiệu quả hơn.

## 4.2. Xử lý mất cân bằng dữ liệu trên tập huấn luyện

Như đã phân tích, sự mất cân bằng dữ liệu là một thách thức lớn. Để giải quyết vấn đề này, kỹ thuật SMOTE (Synthetic Minority Over-sampling Technique) đã được áp dụng.

Phương pháp: SMOTE hoạt động bằng cách tạo ra các mẫu tổng hợp mới cho lớp thiểu số (lớp "có đột quỵ") dựa trên các mẫu hiện có. Các mẫu mới này được tạo ra trên không gian đặc trưng, nằm giữa các mẫu thiểu số gần nhau.
Phạm vi áp dụng: Kỹ thuật này chỉ được áp dụng trên tập huấn luyện (training set). Việc này rất quan trọng để tránh rò rỉ dữ liệu (data leakage), vì tập kiểm tra phải phản ánh đúng phân phối dữ liệu trong thực tế.

Sau khi áp dụng SMOTE, số lượng mẫu của lớp thiểu số và lớp đa số trong tập huấn luyện đã trở nên cân bằng.

## 4.3. Xây dựng và so sánh các mô hình Machine Learning

### 4.3.1. Các thuật toán được lựa chọn

Nhiều thuật toán học máy phổ biến cho bài toán phân loại đã được lựa chọn để huấn luyện và so sánh, bao gồm:

Logistic Regression: Một mô hình tuyến tính cơ bản, nhanh và dễ diễn giải.
Decision Tree: Một mô hình dựa trên cây quyết định, dễ hiểu nhưng dễ bị quá khớp (overfitting).
Random Forest: Một thuật toán học tập quần thể (ensemble) kết hợp nhiều cây quyết định, thường cho hiệu suất cao và ổn định.
Gradient Boosting: Một thuật toán ensemble mạnh mẽ khác, xây dựng các cây một cách tuần tự để sửa lỗi của các cây trước đó.
XGBoost (Extreme Gradient Boosting): Một phiên bản tối ưu và hiệu quả của Gradient Boosting, rất phổ biến trong các cuộc thi Kaggle.
LightGBM (Light Gradient Boosting Machine): Một phiên bản khác của Gradient Boosting, được tối ưu hóa về tốc độ và hiệu quả sử dụng bộ nhớ.
Support Vector Machine (SVM): Một thuật toán mạnh mẽ tìm ranh giới quyết định tối ưu giữa các lớp.

### 4.3.2. Các chỉ số đánh giá (Metrics) và ý nghĩa

Do sự mất cân bằng dữ liệu, chỉ sử dụng độ chính xác (Accuracy) là không đủ. Các chỉ số sau được ưu tiên sử dụng:

F1-Score: Là trung bình điều hòa của Precision và Recall, đây là chỉ số quan trọng nhất cho bài toán này vì nó cân bằng giữa việc dự đoán đúng các ca đột quỵ (Recall) và việc không dự đoán nhầm các ca không đột quỵ thành có đột quỵ (Precision).
Recall (Sensitivity): Tỷ lệ các ca đột quỵ thực tế được mô hình dự đoán đúng. Chỉ số này rất quan trọng trong y tế vì bỏ sót một ca bệnh còn nguy hiểm hơn là chẩn đoán nhầm.
Precision: Tỷ lệ các ca được dự đoán là đột quỵ thực sự bị đột quỵ.
ROC-AUC Score: Đo lường khả năng của mô hình trong việc phân biệt giữa hai lớp. Giá trị càng gần 1 càng tốt.

### 4.3.3. Kết quả so sánh hiệu suất các mô hình

Các mô hình được huấn luyện trên tập dữ liệu đã qua SMOTE và đánh giá trên tập kiểm tra ban đầu. Kết quả cho thấy:

*   Các mô hình dựa trên cây như Random Forest, XGBoost, và LightGBM cho kết quả vượt trội so với các mô hình khác như Logistic Regression hay SVM.
*   Trong số đó, LightGBM nổi bật với F1-Score cao nhất, cho thấy sự cân bằng tốt nhất giữa Precision và Recall.

Do đó, LightGBM được lựa chọn là mô hình tốt nhất để tiếp tục tinh chỉnh và đánh giá sâu hơn.

## 4.4. Lựa chọn và Tinh chỉnh mô hình hiệu quả nhất

### 4.4.1. Tinh chỉnh siêu tham số (Hyperparameter Tuning)

Mô hình LightGBM đã được tinh chỉnh các siêu tham số quan trọng (như `n_estimators`, `learning_rate`, `max_depth`, v.v.) bằng kỹ thuật Grid Search với Cross-Validation (GridSearchCV). Kỹ thuật này thử nghiệm một cách có hệ thống nhiều sự kết hợp của các siêu tham số và sử dụng kiểm định chéo để tìm ra bộ tham số cho hiệu suất tốt nhất trên tập huấn luyện.

### 4.4.2. Đánh giá chi tiết mô hình cuối cùng trên tập kiểm tra

Mô hình LightGBM sau khi đã được tinh chỉnh (gọi là mô hình cuối cùng) được đánh giá lần cuối trên tập kiểm tra. Kết quả chi tiết như sau:

Ma trận nhầm lẫn (Confusion Matrix): Cung cấp cái nhìn chi tiết về số lượng dự đoán đúng/sai cho từng lớp. Mô hình đã có khả năng nhận diện được một số lượng đáng kể các ca đột quỵ (True Positives) trong khi vẫn giữ được tỷ lệ dự đoán sai (False Positives) ở mức chấp nhận được.
Đường cong ROC (ROC Curve): Đường cong ROC của mô hình nằm xa đường chéo, và giá trị AUC cao, khẳng định khả năng phân loại tốt của mô hình.
Các chỉ số chính: Mô hình cuối cùng đạt được các chỉ số F1-Score, Recall và Precision cân bằng và tốt hơn so với mô hình mặc định ban đầu.

## 4.5. Diễn giải mô hình (Model Interpretation)

### 4.5.1. Phân tích mức độ quan trọng của các biến (Feature Importance)

Sử dụng thuộc tính `feature_importances_` của mô hình LightGBM, chúng ta có thể xác định các biến có ảnh hưởng lớn nhất đến kết quả dự đoán. Kết quả phân tích cho thấy các biến quan trọng nhất, xếp theo thứ tự giảm dần, bao gồm:

1.  `age` (Tuổi)
2.  `avg_glucose_level` (Mức đường huyết trung bình)
3.  `bmi` (Chỉ số khối cơ thể)
4.  `smoking_status` (Tình trạng hút thuốc)

Điều này hoàn toàn phù hợp với các phân tích thống kê ở Chương 3 và kiến thức y khoa, củng cố độ tin cậy của mô hình.

### 4.5.2. Phân tích SHAP để giải thích các dự đoán cụ thể

(Phần này có thể được bổ sung nếu phân tích SHAP đã được thực hiện trong notebook)

Để hiểu sâu hơn về cách mô hình đưa ra dự đoán cho từng trường hợp cụ thể, kỹ thuật SHAP (SHapley Additive exPlanations) có thể được sử dụng. SHAP giúp diễn giải "đóng góp" của từng giá trị đặc trưng vào kết quả dự đoán cuối cùng, làm tăng tính minh bạch và khả năng diễn giải của mô hình "hộp đen" như LightGBM.

## 4.6. Lưu trữ mô hình và các thành phần liên quan

Cuối cùng, các đối tượng quan trọng đã được lưu lại để có thể tái sử dụng hoặc triển khai trong tương lai:

Mô hình LightGBM đã được huấn luyện (`moHinhDotQuy_final.pkl`): Chứa toàn bộ mô hình đã được tinh chỉnh.
Đối tượng Pipeline tiền xử lý (`preprocessor.pkl`): Để có thể áp dụng chính xác các bước tiền xử lý cho dữ liệu mới.
Thông tin về mô hình (`model_info.pkl`): Bao gồm danh sách các cột, các chỉ số đánh giá, v.v.

Việc lưu trữ này đảm bảo tính tái lập và sẵn sàng cho việc triển khai thành một ứng dụng thực tế.