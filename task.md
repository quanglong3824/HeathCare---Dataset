# Nhiệm vụ phân tích dữ liệu trong Notebook Exploration

## 1. Tổng quan về dữ liệu
- Hiểu cấu trúc dữ liệu (số lượng dòng, cột)
- Kiểm tra thông tin cơ bản của dataset (dtypes, null values)
- Thống kê mô tả (describe) cho các biến số học
- Hiển thị một số mẫu dữ liệu đầu và cuối

## 2. Xử lý dữ liệu ban đầu
- Đổi tên cột từ tiếng Anh sang tiếng Việt
- Kiểm tra và xử lý giá trị null (đặc biệt là cột BMI)
- Kiểm tra và xử lý giá trị ngoại lai (outliers)
- Chuyển đổi kiểu dữ liệu nếu cần thiết

## 3. Phân tích đơn biến
- Phân tích biến mục tiêu (stroke - đột quỵ)
  - Tỷ lệ đột quỵ trong tập dữ liệu
  - Biểu đồ phân phối
- Phân tích các biến số học
  - Phân phối tuổi (age)
  - Phân phối mức đường huyết trung bình (avg_glucose_level)
  - Phân phối chỉ số BMI
- Phân tích các biến phân loại
  - Phân phối giới tính (gender)
  - Phân phối tình trạng hôn nhân (ever_married)
  - Phân phối loại công việc (work_type)
  - Phân phối nơi cư trú (Residence_type)
  - Phân phối tình trạng hút thuốc (smoking_status)

## 4. Phân tích hai biến
- Mối quan hệ giữa tuổi và đột quỵ
- Mối quan hệ giữa giới tính và đột quỵ
- Mối quan hệ giữa tăng huyết áp (hypertension) và đột quỵ
- Mối quan hệ giữa bệnh tim (heart_disease) và đột quỵ
- Mối quan hệ giữa mức đường huyết trung bình và đột quỵ
- Mối quan hệ giữa BMI và đột quỵ
- Mối quan hệ giữa tình trạng hút thuốc và đột quỵ

## 5. Phân tích đa biến
- Mối tương quan giữa các biến số học
- Biểu đồ heatmap thể hiện tương quan
- Phân tích nhóm theo nhiều biến (ví dụ: tuổi, giới tính và đột quỵ)

## 6. Kiểm định thống kê
- Kiểm định t-test cho các biến số học theo nhóm đột quỵ
- Kiểm định Chi-square cho các biến phân loại với đột quỵ
- Phân tích ANOVA nếu cần thiết

## 7. Trực quan hóa nâng cao
- Biểu đồ phân phối kết hợp (pair plots)
- Biểu đồ violin/box plot cho các biến số học theo nhóm đột quỵ
- Biểu đồ tương tác sử dụng plotly

## 8. Kết luận và insights
- Tổng hợp các phát hiện chính
- Xác định các yếu tố nguy cơ hàng đầu liên quan đến đột quỵ
- Đề xuất hướng phân tích tiếp theo và mô hình dự đoán