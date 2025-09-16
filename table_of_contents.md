# MỤC LỤC ĐỒ ÁN PHÂN TÍCH DỮ LIỆU HEALTHCARE

## PHẦN MỞ ĐẦU
- Trang bìa
- Lời cảm ơn
- Tóm tắt đồ án
- Danh mục các từ viết tắt
- Danh mục các bảng biểu
- Danh mục các hình ảnh

## CHƯƠNG 1: GIỚI THIỆU
1.1. Bối cảnh và tầm quan trọng của đề tài
1.2. Mục tiêu nghiên cứu
   1.2.1. Mục tiêu tổng quát
   1.2.2. Mục tiêu cụ thể
1.3. Phạm vi nghiên cứu
1.4. Câu hỏi nghiên cứu
1.5. Ý nghĩa khoa học và thực tiễn
1.6. Cấu trúc đồ án

## CHƯƠNG 2: TỔNG QUAN TÀI LIỆU
2.1. Tổng quan về đột quỵ
   2.1.1. Định nghĩa và phân loại
   2.1.2. Dịch tễ học đột quỵ
   2.1.3. Các yếu tố nguy cơ đã biết
2.2. Ứng dụng học máy trong dự đoán đột quỵ
   2.2.1. Các nghiên cứu trước đây
   2.2.2. Các mô hình dự đoán phổ biến
   2.2.3. Thách thức trong dự đoán đột quỵ
2.3. Khung lý thuyết nghiên cứu

## CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU
3.1. Thiết kế nghiên cứu
3.2. Nguồn dữ liệu
   3.2.1. Mô tả bộ dữ liệu
   3.2.2. Các biến trong nghiên cứu
3.3. Quy trình phân tích dữ liệu
   3.3.1. Tiền xử lý dữ liệu
   3.3.2. Khám phá dữ liệu
   3.3.3. Xây dựng mô hình
   3.3.4. Đánh giá mô hình
3.4. Công cụ và môi trường phát triển

## CHƯƠNG 4: KHÁM PHÁ VÀ TIỀN XỬ LÝ DỮ LIỆU
4.1. Tổng quan về bộ dữ liệu
   4.1.1. Cấu trúc dữ liệu
   4.1.2. Thống kê mô tả
4.2. Làm sạch dữ liệu
   4.2.1. Xử lý giá trị thiếu
   4.2.2. Xử lý giá trị ngoại lai
4.3. Biến đổi dữ liệu
   4.3.1. Mã hóa biến phân loại
   4.3.2. Chuẩn hóa biến số học
   4.3.3. Tạo biến mới
4.4. Cân bằng dữ liệu

## CHƯƠNG 5: PHÂN TÍCH DỮ LIỆU CHUYÊN SÂU
5.1. Phân tích đơn biến
   5.1.1. Phân tích biến mục tiêu (đột quỵ)
   5.1.2. Phân tích các biến số học
   5.1.3. Phân tích các biến phân loại
5.2. Phân tích hai biến
   5.2.1. Mối quan hệ giữa các biến số học và đột quỵ
   5.2.2. Mối quan hệ giữa các biến phân loại và đột quỵ
5.3. Phân tích đa biến
   5.3.1. Ma trận tương quan
   5.3.2. Phân tích nhóm
5.4. Kiểm định thống kê
   5.4.1. Kiểm định t-test
   5.4.2. Kiểm định Chi-square
   5.4.3. Phân tích ANOVA
5.5. Kết quả và thảo luận

## CHƯƠNG 6: XÂY DỰNG MÔ HÌNH DỰ ĐOÁN
6.1. Chuẩn bị dữ liệu cho mô hình
   6.1.1. Chia tập dữ liệu
   6.1.2. Lựa chọn đặc trưng
6.2. Xây dựng các mô hình cơ bản
   6.2.1. Hồi quy Logistic
   6.2.2. Cây quyết định
   6.2.3. Random Forest
6.3. Xây dựng các mô hình nâng cao
   6.3.1. XGBoost
   6.3.2. LightGBM
   6.3.3. Neural Networks
6.4. Đánh giá và so sánh mô hình
   6.4.1. Các metrics đánh giá
   6.4.2. Phân tích đường cong ROC và PR
   6.4.3. Đánh giá độ quan trọng của đặc trưng
   6.4.4. Cross-validation

## CHƯƠNG 7: TỐI ƯU HÓA MÔ HÌNH
7.1. Tinh chỉnh siêu tham số
   7.1.1. Grid Search
   7.1.2. Random Search
   7.1.3. Bayesian Optimization
7.2. Kỹ thuật ensemble
   7.2.1. Stacking
   7.2.2. Voting
   7.2.3. Boosting và Bagging
7.3. Xử lý vấn đề overfitting/underfitting
7.4. Kết quả sau tối ưu hóa

## CHƯƠNG 8: PHÂN TÍCH KẾT QUẢ VÀ ĐỀ XUẤT
8.1. Phân tích kết quả mô hình
   8.1.1. Các yếu tố quan trọng ảnh hưởng đến nguy cơ đột quỵ
   8.1.2. Phân tích các trường hợp dự đoán sai
   8.1.3. Đánh giá độ tin cậy của mô hình
8.2. Đề xuất y tế và sức khỏe cộng đồng
   8.2.1. Nhóm đối tượng có nguy cơ cao
   8.2.2. Biện pháp can thiệp dựa trên yếu tố nguy cơ
   8.2.3. Hướng dẫn sàng lọc
8.3. Đề xuất ứng dụng thực tế
   8.3.1. Công cụ dự đoán nguy cơ đột quỵ
   8.3.2. Tích hợp với hệ thống chăm sóc sức khỏe
   8.3.3. Đề xuất nghiên cứu tiếp theo

## CHƯƠNG 9: KẾT LUẬN
9.1. Tổng kết nghiên cứu
9.2. Đóng góp của nghiên cứu
9.3. Hạn chế của nghiên cứu
9.4. Hướng phát triển tương lai

## TÀI LIỆU THAM KHẢO

## PHỤ LỤC
- Phụ lục A: Mã nguồn
- Phụ lục B: Kết quả chi tiết các mô hình
- Phụ lục C: Bảng dữ liệu bổ sung