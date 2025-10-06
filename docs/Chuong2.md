# CHƯƠNG 2: KHÁM PHÁ VÀ TIỀN XỬ LÝ DỮ LIỆU

Chương này trình bày chi tiết quá trình làm việc với tập dữ liệu gốc, từ việc tìm hiểu, khám phá sơ bộ cho đến các bước làm sạch và chuẩn bị dữ liệu. Mục tiêu của chương này là tạo ra một tập dữ liệu chất lượng, sẵn sàng cho việc phân tích thống kê và xây dựng mô hình ở các chương sau.

## 2.1. Giới thiệu tập dữ liệu

### 2.1.1. Nguồn gốc và mô tả

Dự án sử dụng tập dữ liệu "Healthcare Dataset Stroke Data" được công bố trên nền tảng Kaggle. Đây là một tập dữ liệu phổ biến trong cộng đồng khoa học dữ liệu, thường được dùng cho các bài toán dự đoán nguy cơ đột quỵ dựa trên các thông tin về nhân khẩu học và sức khỏe.

   Nguồn: [Kaggle: Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
   Kích thước ban đầu: Tập dữ liệu gồm 5,110 mẫu (bệnh nhân) và 12 thuộc tính (cột).

### 2.1.2. Mô tả các biến

Mỗi dòng trong tập dữ liệu đại diện cho một bệnh nhân và bao gồm các thông tin sau:

| Tên biến            | Kiểu dữ liệu | Mô tả                                                                            |
| ------------------- | ------------ | -----------------------------------------------------------------------          |
| `id`                | Số (int)     | Mã định danh duy nhất của bệnh nhân.                                             |
| `gender`            | Chữ (object) | Giới tính của bệnh nhân (Male, Female, hoặc Other).                              |
| `age`               | Số (float)   | Tuổi của bệnh nhân.                                                              |
| `hypertension`      | Nhị phân (int) | Có tiền sử tăng huyết áp hay không (1: Có, 0: Không).                          |
| `heart_disease`     | Nhị phân (int) | Có tiền sử bệnh tim hay không (1: Có, 0: Không).                               |
| `ever_married`      | Chữ (object) | Đã từng kết hôn hay chưa (Yes, No).                                              |
| `work_type`         | Chữ (object) | Loại hình công việc (Private, Self-employed, Govt_job, children, Never_worked).  |
| `Residence_type`    | Chữ (object) | Khu vực sinh sống (Urban: Thành thị, Rural: Nông thôn).                          |
| `avg_glucose_level` | Số (float)   | Mức đường huyết trung bình trong máu.                                            |
| `bmi`               | Số (float)   | Chỉ số khối cơ thể (Body Mass Index).                                            |
| `smoking_status`    | Chữ (object) | Tình trạng hút thuốc (formerly smoked, never smoked, smokes, Unknown).           |
| `stroke`            | Nhị phân (int) | Biến mục tiêu: Bệnh nhân có bị đột quỵ hay không (1: Có, 0: Không).            |

## 2.2. Khám phá dữ liệu sơ bộ (Exploratory Data Analysis - EDA)

### 2.2.1. Phân tích thống kê mô tả

Một cái nhìn tổng quan về các biến số trong dữ liệu cho thấy:

   Tuổi (`age`): Độ tuổi của các bệnh nhân trong mẫu dao động từ trẻ sơ sinh (0.08 tuổi) đến người cao tuổi (82 tuổi), với độ tuổi trung bình là 43.2.
   Mức đường huyết (`avg_glucose_level`): Có sự biến thiên lớn, từ 55.12 đến 271.74, cho thấy sự đa dạng về tình trạng sức khỏe của các bệnh nhân.
   Chỉ số BMI (`bmi`): Chỉ số BMI trung bình là 28.9, nhưng cũng có sự dao động đáng kể.

### 2.2.2. Kiểm tra kiểu dữ liệu và thông tin chung

Kiểm tra ban đầu cho thấy các kiểu dữ liệu đã phù hợp với mô tả. Tuy nhiên, một phát hiện quan trọng là sự xuất hiện của các giá trị thiếu:

   Cột `bmi` có 201 giá trị bị thiếu, chiếm khoảng 3.9% tổng số dữ liệu. Đây là vấn đề cần được xử lý trong bước làm sạch.
   Các cột còn lại đều có đủ 5,110 giá trị.

## 2.3. Làm sạch dữ liệu (Data Cleaning)

### 2.3.1. Xử lý giá trị thiếu (Missing Values)

Như đã xác định, chỉ có cột `bmi` chứa giá trị thiếu. Dựa trên phân tích phân phối của biến `bmi`, phương pháp thay thế các giá trị thiếu bằng giá trị trung vị (median) đã được lựa chọn. Lý do là vì phân phối của `bmi` có xu hướng bị lệch, và giá trị trung vị ít bị ảnh hưởng bởi các giá trị ngoại lai hơn so với giá trị trung bình, do đó đây là một lựa chọn thay thế hợp lý và an toàn.

Sau khi xử lý, tập dữ liệu không còn giá trị thiếu.

### 2.3.2. Phân tích và xử lý giá trị ngoại lai (Outliers)

Phân tích ngoại lai được thực hiện cho các biến số `age`, `avg_glucose_level`, và `bmi` bằng phương pháp IQR (Interquartile Range). Các biểu đồ boxplot cho thấy sự tồn tại của các giá trị ngoại lai, đặc biệt ở `avg_glucose_level`. Tuy nhiên, trong bối cảnh y tế, các giá trị này có thể là những trường hợp bệnh lý thực tế và chứa thông tin quan trọng. Do đó, dự án quyết định không loại bỏ các giá trị ngoại lai mà giữ lại để mô hình có thể học được từ những trường hợp đa dạng này.

### 2.3.3. Kiểm tra tính hợp lệ và logic của dữ liệu

   Cột `id`: Cột này chỉ là mã định danh, không mang giá trị phân tích nên đã được loại bỏ.
   Cột `gender`: Có một giá trị "Other". Vì số lượng quá ít (chỉ 1 trường hợp), không đủ để đưa ra kết luận thống kê, nên dòng dữ liệu này đã được loại bỏ để đảm bảo tính nhất quán.
   Kiểm tra trùng lặp: Không có dòng dữ liệu nào bị trùng lặp hoàn toàn.

## 2.4. Kỹ thuật tạo biến (Feature Engineering)

Để làm giàu thông tin cho mô hình, một số biến mới đã được tạo ra từ các biến hiện có.

### 2.4.1. Tạo các biến nhóm (Tuổi, BMI, Glucose)

   `nhomTuoi`: Bệnh nhân được phân vào các nhóm tuổi khác nhau (Vị thành niên, Thanh niên, Trung niên, Cao niên) để mô hình có thể học được các ngưỡng nguy cơ theo độ tuổi.
   `nhomBMI`: Phân loại tình trạng cơ thể dựa trên chỉ số BMI theo chuẩn của WHO (Thiếu cân, Bình thường, Thừa cân, Béo phì).
   `nhomGlucose`: Phân loại mức đường huyết (Bình thường, Tiền tiểu đường, Tiểu đường) để làm nổi bật các mức độ nguy cơ khác nhau.

### 2.4.2. Tạo biến tổng hợp "Điểm nguy cơ"

Một biến mới là `diemNguyCo` được tạo ra bằng cách cộng điểm từ các yếu tố nguy cơ đã biết như `hypertension`, `heart_disease`, và các nhóm `nhomBMI`, `nhomGlucose` vừa tạo. Biến này giúp tổng hợp nhiều yếu tố rủi ro vào một chỉ số duy nhất, có khả năng cung cấp một tín hiệu mạnh mẽ hơn cho mô hình.

## 2.5. Kiểm tra chất lượng dữ liệu sau xử lý

Sau tất cả các bước làm sạch và tạo biến, tập dữ liệu cuối cùng có 5,109 mẫu và 15 cột. Dữ liệu đã sạch, không còn giá trị thiếu hay các giá trị không hợp lệ.

Một phân tích quan trọng về biến mục tiêu `stroke` cho thấy một vấn đề nổi bật: sự mất cân bằng dữ liệu nghiêm trọng. Chỉ có 249 trường hợp đột quỵ (4.9%) so với 4,860 trường hợp không đột quỵ (95.1%). Đây là một thách thức lớn cần được giải quyết trong giai đoạn xây dựng mô hình để tránh việc mô hình bị thiên vị, chỉ dự đoán "không đột quỵ".

## 2.6. Lưu trữ dữ liệu đã xử lý

Để thuận tiện cho các bước tiếp theo, tập dữ liệu đã qua xử lý được lưu lại thành một file CSV mới có tên là `du_lieu_da_xu_ly.csv`. File này sẽ là đầu vào cho quá trình phân tích thống kê và huấn luyện mô hình.