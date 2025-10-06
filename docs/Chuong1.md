# CHƯƠNG 1: GIỚI THIỆU TỔNG QUAN

## 1.1. Bối cảnh và Lý do chọn đề tài

### 1.1.1. Tầm quan trọng của việc dự đoán sớm đột quỵ

Đột quỵ, hay tai biến mạch máu não, là một trong những nguyên nhân gây tử vong và tàn tật hàng đầu trên toàn thế giới. Theo Tổ chức Y tế Thế giới (WHO), mỗi năm có hàng triệu người bị đột quỵ, và một phần lớn trong số đó phải gánh chịu những di chứng nặng nề, ảnh hưởng nghiêm trọng đến chất lượng cuộc sống của bản thân và gia đình. Gánh nặng kinh tế - xã hội do đột quỵ gây ra là vô cùng lớn, bao gồm chi phí điều trị, chăm sóc dài hạn và mất mát về năng suất lao động.

Trong bối cảnh đó, việc phát hiện và dự đoán sớm nguy cơ đột quỵ đóng một vai trò cực kỳ quan trọng. Nếu các yếu tố nguy cơ có thể được xác định và một cá nhân được cảnh báo sớm về khả năng mắc bệnh, các biện pháp can thiệp y tế và thay đổi lối sống có thể được áp dụng kịp thời. Điều này không chỉ giúp giảm thiểu tỷ lệ mắc bệnh mà còn có thể cứu sống hàng triệu người và giảm bớt gánh nặng cho hệ thống y tế.

### 1.1.2. Vấn đề nghiên cứu

Sự phát triển của khoa học dữ liệu và học máy đã mở ra những cơ hội mới trong việc phân tích dữ liệu y tế phức tạp. Bằng cách khai thác thông tin từ hồ sơ bệnh án, các đặc điểm nhân khẩu học và lối sống của bệnh nhân, chúng ta có thể xây dựng các mô hình dự đoán có khả năng xác định các cá nhân có nguy cơ cao.

Vấn đề nghiên cứu của dự án này là: "Làm thế nào để ứng dụng các kỹ thuật phân tích dữ liệu và học máy trên tập dữ liệu về sức khỏe để xác định các yếu tố nguy cơ chính và xây dựng một mô hình dự đoán chính xác khả năng bị đột quỵ của một cá nhân?"

Dự án sẽ tập trung vào việc phân tích sâu một tập dữ liệu công khai về đột quỵ để trả lời câu hỏi này, từ đó cung cấp những hiểu biết có giá trị và một công cụ hỗ trợ tiềm năng cho ngành y tế.

## 1.2. Mục tiêu dự án

Dựa trên vấn đề nghiên cứu đã nêu, dự án đặt ra các mục tiêu chính và mục tiêu cụ thể như sau:

### 1.2.1. Mục tiêu chính

   Phân tích và xác định các yếu tố nhân khẩu học, y tế và lối sống có ảnh hưởng mạnh mẽ nhất đến nguy cơ đột quỵ.
   Xây dựng và đánh giá một mô hình học máy có khả năng dự đoán nguy cơ đột quỵ với độ chính xác và độ tin cậy cao.
   Đưa ra các khuyến nghị dựa trên dữ liệu nhằm hỗ trợ việc phòng ngừa và tầm soát sớm đột quỵ trong cộng đồng.

### 1.2.2. Mục tiêu cụ thể

   Thực hiện khám phá và làm sạch tập dữ liệu `healthcare-dataset-stroke-data`.
   Áp dụng các kỹ thuật trực quan hóa và kiểm định thống kê để tìm ra các mối quan hệ có ý nghĩa giữa các biến và biến mục tiêu (đột quỵ).
   So sánh hiệu suất của nhiều thuật toán học máy khác nhau (ví dụ: Logistic Regression, Random Forest, Gradient Boosting, v.v.) để chọn ra mô hình tốt nhất.
   Xử lý vấn đề mất cân bằng dữ liệu, một thách thức phổ biến trong các bài toán y tế.
   Đánh giá chi tiết mô hình được chọn bằng các chỉ số phù hợp như F1-Score, ROC-AUC, Sensitivity và Specificity.
   Diễn giải mô hình để hiểu rõ cách các yếu tố đầu vào tác động đến kết quả dự đoán.

## 1.3. Phạm vi và Đối tượng nghiên cứu

   Phạm vi dữ liệu: Dự án sử dụng tập dữ liệu "Healthcare Dataset Stroke Data" từ Kaggle, bao gồm 5,110 mẫu bệnh nhân với 11 biến độc lập và 1 biến mục tiêu.
   Phạm vi bài toán: Đây là một bài toán phân loại nhị phân (Binary Classification), trong đó mục tiêu là dự đoán một bệnh nhân có bị đột quỵ (1) hay không (0).
   Đối tượng nghiên cứu: Các bệnh nhân trong tập dữ liệu được cung cấp. Kết quả và mô hình của dự án hướng đến việc hỗ trợ các chuyên gia y tế, bác sĩ trong việc chẩn đoán và tư vấn cho bệnh nhân.

## 1.4. Phương pháp tiếp cận

Dự án được thực hiện theo một quy trình khoa học dữ liệu chuẩn, bao gồm các giai đoạn chính sau:

1.  Khám phá dữ liệu (Exploratory Data Analysis - EDA): Tìm hiểu sâu về cấu trúc, phân phối và các đặc điểm của dữ liệu.
2.  Tiền xử lý dữ liệu và Kỹ thuật tạo biến (Data Preprocessing & Feature Engineering): Làm sạch dữ liệu, xử lý các giá trị thiếu, và tạo ra các biến mới có ý nghĩa hơn.
3.  Phát triển mô hình học máy (Machine Learning Model Development): Huấn luyện nhiều mô hình khác nhau trên dữ liệu đã xử lý.
4.  Đánh giá và Lựa chọn mô hình (Model Evaluation & Selection): Sử dụng các chỉ số đánh giá phù hợp để chọn ra mô hình có hiệu suất tốt nhất.
5.  Tổng hợp kết quả và Đề xuất (Insights & Recommendations): Rút ra các kết luận quan trọng từ phân tích và đề xuất các hướng hành động thực tế.

## 1.5. Cấu trúc báo cáo

Báo cáo được tổ chức thành 5 chương chính:
   Chương 1 - Giới thiệu tổng quan: Trình bày bối cảnh, mục tiêu, phạm vi và phương pháp luận của dự án.
   Chương 2 - Khám phá và Tiền xử lý dữ liệu: Mô tả chi tiết về tập dữ liệu và các bước làm sạch, chuẩn bị dữ liệu.
   Chương 3 - Phân tích Thống kê và Trực quan hóa: Đi sâu vào phân tích các mối quan hệ trong dữ liệu để tìm ra các yếu tố nguy cơ.
   Chương 4 - Xây dựng và Đánh giá mô hình dự đoán: Trình bày quá trình xây dựng, so sánh và lựa chọn mô hình học máy.
   Chương 5 - Kết luận và Đề xuất: Tóm tắt các kết quả chính, nêu bật các hạn chế và đề xuất các hướng phát triển trong tương lai.