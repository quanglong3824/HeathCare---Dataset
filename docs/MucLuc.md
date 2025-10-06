# MỤC LỤC BÁO CÁO DỰ ÁN: PHÂN TÍCH DỮ LIỆU VÀ DỰ ĐOÁN NGUY CƠ ĐỘT QUỴ

LỜI NÓI ĐẦU

TÓM TẮT DỰ ÁN (EXECUTIVE SUMMARY)

DANH MỤC BẢNG BIỂU

DANH MỤC HÌNH VẼ

---


CHƯƠNG 1: GIỚI THIỆU TỔNG QUAN
1.1. Bối cảnh và Lý do chọn đề tài
    1.1.1. Tầm quan trọng của việc dự đoán sớm đột quỵ
    1.1.2. Vấn đề nghiên cứu
1.2. Mục tiêu dự án
    1.2.1. Mục tiêu chính
    1.2.2. Mục tiêu cụ thể
1.3. Phạm vi và Đối tượng nghiên cứu
1.4. Phương pháp tiếp cận
1.5. Cấu trúc báo cáo

CHƯƠNG 2: KHÁM PHÁ VÀ TIỀN XỬ LÝ DỮ LIỆU
2.1. Giới thiệu tập dữ liệu
    2.1.1. Nguồn gốc và mô tả
    2.1.2. Mô tả các biến
2.2. Khám phá dữ liệu sơ bộ (Exploratory Data Analysis - EDA)
    2.2.1. Phân tích thống kê mô tả
    2.2.2. Kiểm tra kiểu dữ liệu và thông tin chung
2.3. Làm sạch dữ liệu (Data Cleaning)
    2.3.1. Xử lý giá trị thiếu (Missing Values)
    2.3.2. Phân tích và xử lý giá trị ngoại lai (Outliers)
    2.3.3. Kiểm tra tính hợp lệ và logic của dữ liệu
2.4. Kỹ thuật tạo biến (Feature Engineering)
    2.4.1. Tạo các biến nhóm (Tuổi, BMI, Glucose)
    2.4.2. Tạo biến tổng hợp "Điểm nguy cơ"
2.5. Kiểm tra chất lượng dữ liệu sau xử lý
2.6. Lưu trữ dữ liệu đã xử lý

CHƯƠNG 3: PHÂN TÍCH THỐNG KÊ VÀ TRỰC QUAN HÓA
3.1. Phân tích biến mục tiêu (Stroke)
    3.1.1. Phân tích sự mất cân bằng của dữ liệu
3.2. Phân tích các biến định lượng
    3.2.1. Phân phối và thống kê mô tả (Tuổi, BMI, Mức Glucose)
    3.2.2. So sánh giữa hai nhóm có và không có đột quỵ (T-test)
3.3. Phân tích các biến định tính
    3.3.1. Phân phối và tỷ lệ đột quỵ theo từng nhóm
    3.3.2. Kiểm định mối quan hệ với đột quỵ (Chi-square test)
3.4. Phân tích tương quan (Correlation Analysis)
    3.4.1. Ma trận tương quan giữa các biến
    3.4.2. Trực quan hóa bằng Heatmap
3.5. Phân tích chuyên sâu
    3.5.1. Phân tích nguy cơ đột quỵ theo nhóm tuổi
    3.5.2. Phân tích các yếu tố nguy cơ phối hợp và điểm nguy cơ
3.6. Tổng kết các phát hiện quan trọng từ phân tích dữ liệu

CHƯƠNG 4: XÂY DỰNG VÀ ĐÁNH GIÁ MÔ HÌNH DỰ ĐOÁN
4.1. Chuẩn bị dữ liệu cho Machine Learning
    4.1.1. Lựa chọn biến và xác định tập features (X) và target (y)
    4.1.2. Phân chia tập dữ liệu (Training và Test set)
    4.1.3. Xây dựng quy trình tiền xử lý (Preprocessing Pipeline)
4.2. Xử lý mất cân bằng dữ liệu trên tập huấn luyện
    4.2.1. So sánh các phương pháp (SMOTE, Over-sampling, Under-sampling)
    4.2.2. Lựa chọn phương pháp tối ưu
4.3. Xây dựng và so sánh các mô hình Machine Learning
    4.3.1. Các thuật toán được lựa chọn
    4.3.2. Các chỉ số đánh giá (Metrics) và ý nghĩa
    4.3.3. Kết quả so sánh hiệu suất các mô hình
4.4. Lựa chọn và Tinh chỉnh mô hình hiệu quả nhất
    4.4.1. Tinh chỉnh siêu tham số (Hyperparameter Tuning)
    4.4.2. Đánh giá chi tiết mô hình cuối cùng trên tập kiểm tra (Confusion Matrix, ROC Curve, v.v.)
4.5. Diễn giải mô hình (Model Interpretation)
    4.5.1. Phân tích mức độ quan trọng của các biến (Feature Importance)
    4.5.2. Phân tích SHAP để giải thích các dự đoán cụ thể
4.6. Lưu trữ mô hình và các thành phần liên quan

CHƯƠNG 5: KẾT LUẬN VÀ ĐỀ XUẤT
5.1. Tóm tắt toàn bộ quá trình và kết quả đạt được
5.2. Các phát hiện chính và ý nghĩa thực tiễn
5.3. Hạn chế của dự án
5.4. Đề xuất cải thiện và hướng phát triển trong tương lai
    5.4.1. Về dữ liệu
    5.4.2. Về mô hình
    5.4.3. Về phương pháp đánh giá
5.5. Lộ trình ứng dụng vào thực tế (Roadmap)
    5.5.1. Giai đoạn 1: Xây dựng sản phẩm tối thiểu (Proof of Concept)
    5.5.2. Giai đoạn 2: Thử nghiệm và xác thực lâm sàng (Pilot & Validation)
    5.5.3. Giai đoạn 3: Mở rộng và triển khai (Scale-up)

TÀI LIỆU THAM KHẢO

PHỤ LỤC
Phụ lục A: Mô tả chi tiết các biến trong tập dữ liệu
Phụ lục B: Kết quả chi tiết của các kiểm định thống kê
Phụ lục C: Bảng so sánh hiệu suất chi tiết của các mô hình