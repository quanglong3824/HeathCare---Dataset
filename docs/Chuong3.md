# CHƯƠNG 3: PHÂN TÍCH THỐNG KÊ VÀ TRỰC QUAN HÓA

Sau khi dữ liệu đã được làm sạch và chuẩn bị ở Chương 2, chương này sẽ đi sâu vào việc phân tích và trực quan hóa để tìm ra những hiểu biết (insights) quan trọng. Mục tiêu là xác định các yếu tố có mối liên hệ mạnh mẽ với nguy cơ đột quỵ, làm nền tảng cho việc lựa chọn biến và xây dựng mô hình ở chương sau.

## 3.1. Phân tích biến mục tiêu (Stroke)

### 3.1.1. Phân tích sự mất cân bằng của dữ liệu

Như đã đề cập ở chương trước, biến mục tiêu `stroke` bị mất cân bằng nghiêm trọng. Phân tích trên tập dữ liệu đã xử lý (5,109 mẫu) cho thấy:

Không đột quỵ (0): 4,860 trường hợp (chiếm 95.1%)
Có đột quỵ (1): 249 trường hợp (chiếm 4.9%)

Trực quan hóa bằng biểu đồ thanh cho thấy sự chênh lệch rõ rệt này. Tình trạng mất cân bằng này là một thách thức lớn, đòi hỏi các kỹ thuật xử lý đặc biệt trong giai đoạn xây dựng mô hình để đảm bảo mô hình không bị thiên vị và có khả năng nhận diện đúng lớp thiểu số (có đột quỵ).

## 3.2. Phân tích các biến định lượng

### 3.2.1. Phân phối và thống kê mô tả (Tuổi, BMI, Mức Glucose)

Phân tích phân phối của các biến `age`, `avg_glucose_level`, và `bmi` cho thấy:

Tuổi (`age`): Phân phối của tuổi khá đồng đều, nhưng khi so sánh giữa hai nhóm, có thể thấy rõ nhóm bệnh nhân bị đột quỵ có độ tuổi trung bình cao hơn đáng kể so với nhóm không bị đột quỵ. Điều này cho thấy tuổi tác là một yếu tố nguy cơ quan trọng.
Mức Glucose (`avg_glucose_level`): Phân phối của biến này bị lệch phải. Nhóm bị đột quỵ có xu hướng có mức đường huyết trung bình cao hơn.
BMI (`bmi`): Phân phối của BMI cũng bị lệch phải. Mặc dù không rõ ràng như tuổi và mức glucose, nhóm bị đột quỵ dường như cũng có chỉ số BMI cao hơn một chút.

### 3.2.2. So sánh giữa hai nhóm có và không có đột quỵ (T-test)

Để kiểm định sự khác biệt về giá trị trung bình của các biến định lượng giữa hai nhóm, kiểm định T (T-test) độc lập đã được thực hiện:

Tuổi (`age`): Giá trị p-value rất nhỏ (gần bằng 0), cho thấy có sự khác biệt rất có ý nghĩa thống kê về độ tuổi trung bình giữa nhóm bị đột quỵ và không bị đột quỵ.
Mức Glucose (`avg_glucose_level`): Giá trị p-value cũng rất nhỏ, khẳng định rằng mức đường huyết trung bình ở nhóm bị đột quỵ cao hơn một cách có ý nghĩa thống kê.
BMI (`bmi`): Giá trị p-value lớn hơn so với hai biến trên nhưng vẫn đủ nhỏ để kết luận có sự khác biệt có ý nghĩa thống kê về BMI giữa hai nhóm.

Kết luận: Cả ba biến định lượng đều cho thấy sự khác biệt có ý nghĩa thống kê giữa nhóm có và không có đột quỵ, trong đó `age` và `avg_glucose_level` là hai yếu tố có sự khác biệt rõ rệt nhất.

## 3.3. Phân tích các biến định tính

### 3.3.1. Phân phối và tỷ lệ đột quỵ theo từng nhóm

Trực quan hóa tỷ lệ đột quỵ trong các nhóm của từng biến định tính mang lại nhiều thông tin giá trị:

Tăng huyết áp (`hypertension`): Tỷ lệ đột quỵ ở nhóm có tiền sử tăng huyết áp (khoảng 13%) cao hơn hẳn so với nhóm không có (khoảng 4%).
Bệnh tim (`heart_disease`): Tương tự, nhóm có tiền sử bệnh tim có tỷ lệ đột quỵ cao vượt trội (khoảng 17%) so với nhóm không có (khoảng 4%).
Tình trạng hôn nhân (`ever_married`): Những người đã từng kết hôn có tỷ lệ đột quỵ cao hơn.
Loại hình công việc (`work_type`): Nhóm người tự kinh doanh (`Self-employed`) có tỷ lệ đột quỵ cao hơn các nhóm khác.
Tình trạng hút thuốc (`smoking_status`): Nhóm "formerly smoked" (đã từng hút) và "smokes" (đang hút) có tỷ lệ đột quỵ cao hơn nhóm "never smoked" (chưa bao giờ hút).

### 3.3.2. Kiểm định mối quan hệ với đột quỵ (Chi-square test)

Kiểm định Chi-bình phương (Chi-square test) được sử dụng để xác định mối liên hệ thống kê giữa các biến định tính và biến mục tiêu `stroke`.

Kết quả: Tất cả các biến định tính được kiểm định (`gender`, `hypertension`, `heart_disease`, `ever_married`, `work_type`, `Residence_type`, `smoking_status`) đều có giá trị p-value rất nhỏ. Điều này khẳng định rằng tất cả các biến này đều có mối liên hệ có ý nghĩa thống kê với nguy cơ đột quỵ.

## 3.4. Phân tích tương quan (Correlation Analysis)

### 3.4.1. Ma trận tương quan giữa các biến

Phân tích tương quan được thực hiện giữa các biến số (bao gồm cả các biến nhị phân như `hypertension`, `heart_disease`).

### 3.4.2. Trực quan hóa bằng Heatmap

Ma trận tương quan được trực quan hóa bằng heatmap. Các cặp biến có tương quan đáng chú ý nhất bao gồm:

*   `age` và `ever_married`: Tương quan dương mạnh, điều này hợp lý vì người lớn tuổi thường đã kết hôn.
*   `age` và `stroke`: Tương quan dương, xác nhận lại tuổi là yếu tố nguy cơ.
*   `hypertension` và `age`: Tương quan dương, người lớn tuổi có xu hướng bị tăng huyết áp nhiều hơn.
*   `avg_glucose_level` và `stroke`: Tương quan dương.

Nhìn chung, không có hiện tượng đa cộng tuyến (multicollinearity) quá nghiêm trọng giữa các biến độc lập, điều này là một tín hiệu tốt cho việc xây dựng mô hình.

## 3.5. Phân tích chuyên sâu

### 3.5.1. Phân tích nguy cơ đột quỵ theo nhóm tuổi

Khi kết hợp phân tích `age` và `stroke`, biểu đồ phân phối cho thấy rõ ràng rằng tần suất đột quỵ tăng mạnh ở các nhóm tuổi cao, đặc biệt là từ 60 tuổi trở lên. Điều này nhấn mạnh tuổi tác là một trong những yếu tố dự báo quan trọng nhất.

### 3.5.2. Phân tích các yếu tố nguy cơ phối hợp và điểm nguy cơ

Phân tích biến `diemNguyCo` (tạo ở Chương 2) cho thấy những bệnh nhân có điểm nguy cơ cao hơn cũng có tỷ lệ đột quỵ cao hơn một cách rõ rệt. Điều này chứng tỏ việc kết hợp các yếu tố rủi ro vào một biến tổng hợp là một kỹ thuật tạo biến hiệu quả, giúp nắm bắt tốt hơn nguy cơ tổng thể của một bệnh nhân.

## 3.6. Tổng kết các phát hiện quan trọng từ phân tích dữ liệu

Qua quá trình phân tích, các yếu tố sau đây được xác định là có mối liên hệ mạnh mẽ và có ý nghĩa thống kê với nguy cơ đột quỵ:

1.  Các yếu tố nguy cơ hàng đầu:
    Tuổi (`age`): Yếu tố có ảnh hưởng rõ rệt nhất, tuổi càng cao nguy cơ càng lớn.
    Tiền sử bệnh lý: `hypertension` (tăng huyết áp) và `heart_disease` (bệnh tim) làm tăng đáng kể nguy cơ đột quỵ.
    Mức đường huyết (`avg_glucose_level`): Mức đường huyết cao là một chỉ báo nguy cơ quan trọng.

2.  Các yếu tố ảnh hưởng khác:
    *   `ever_married`, `work_type`, `smoking_status`, và `bmi` cũng cho thấy mối liên hệ có ý nghĩa, mặc dù mức độ ảnh hưởng có thể không mạnh bằng các yếu tố trên.

3.  Vấn đề cần lưu ý cho mô hình hóa:
    *   Sự mất cân bằng nghiêm trọng của biến mục tiêu `stroke` là thách thức chính cần được giải quyết.

Những phát hiện này sẽ là kim chỉ nam cho việc lựa chọn các biến đầu vào và thiết kế các chiến lược mô hình hóa trong chương tiếp theo.