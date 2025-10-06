# CHƯƠNG 5: KẾT LUẬN VÀ ĐỀ XUẤT

Chương cuối cùng này sẽ tóm tắt lại toàn bộ quá trình thực hiện dự án, tổng hợp các kết quả và phát hiện quan trọng, đồng thời đưa ra những hạn chế của nghiên cứu và các đề xuất cho những hướng phát triển trong tương lai.

## 5.1. Tóm tắt toàn bộ quá trình và kết quả đạt được

Dự án "Phân tích dữ liệu và Dự đoán nguy cơ đột quỵ" đã được thực hiện một cách có hệ thống qua các giai đoạn chính của một quy trình khoa học dữ liệu:

1.  Thu thập và Khám phá dữ liệu:Bắt đầu với tập dữ liệu gồm 5,110 mẫu, tiến hành khám phá để hiểu cấu trúc, xác định các vấn đề về chất lượng như giá trị thiếu, dữ liệu không hợp lệ.
2.  Tiền xử lý dữ liệu:Thực hiện các kỹ thuật làm sạch, xử lý giá trị thiếu ở cột `bmi` bằng giá trị trung vị, loại bỏ các mẫu không nhất quán, và tạo ra các biến mới (`nhomTuoi`, `nhomBMI`, `nhomGlucose`, `diemNguyCo`) để làm giàu thông tin.
3.  Phân tích Thống kê và Trực quan hóa:Phân tích sâu các mối quan hệ giữa các biến và nguy cơ đột quỵ. Các kiểm định thống kê (T-test, Chi-square) và trực quan hóa đã xác nhận các yếu tố nguy cơ chính như tuổi tác, tăng huyết áp, bệnh tim và mức đường huyết cao.
4.  Xây dựng và Đánh giá mô hình:Xây dựng một quy trình tiền xử lý tự động, xử lý vấn đề mất cân bằng dữ liệu bằng kỹ thuật SMOTE, và so sánh hiệu suất của 7 thuật toán học máy khác nhau. Mô hình LightGBMđã được lựa chọn là mô hình tốt nhất và được tinh chỉnh siêu tham số để tối ưu hóa hiệu suất.

Kết quả chính:Mô hình LightGBM cuối cùng đã cho thấy khả năng dự đoán tốt trên tập dữ liệu kiểm tra, với sự cân bằng hợp lý giữa việc phát hiện các ca bệnh và giảm thiểu dự đoán sai. Các yếu tố quan trọng nhất mà mô hình dựa vào để đưa ra dự đoán là `age`, `avg_glucose_level`, và `bmi`, hoàn toàn phù hợp với các phân tích trước đó.

## 5.2. Các phát hiện chính và ý nghĩa thực tiễn

Qua toàn bộ dự án, chúng ta có thể rút ra những phát hiện có ý nghĩa sau:
  Các yếu tố nguy cơ không thể bỏ qua:Tuổi tác, tiền sử tăng huyết áp và bệnh tim là những yếu tố có ảnh hưởng mạnh mẽ nhất đến nguy cơ đột quỵ. Đây là những thông tin quan trọng cho việc truyền thông và giáo dục sức khỏe cộng đồng.  Tầm quan trọng của chỉ số sức khỏe:Mức đường huyết và chỉ số BMI cũng là những yếu tố dự báo quan trọng. Điều này nhấn mạnh vai trò của việc duy trì một lối sống lành mạnh, kiểm soát cân nặng và đường huyết trong việc phòng ngừa đột quỵ.  Khả năng ứng dụng của Machine Learning:Dự án đã chứng minh rằng các mô hình học máy, đặc biệt là các thuật toán ensemble như LightGBM, có tiềm năng lớn trong việc xây dựng các công cụ hỗ trợ sàng lọc và cảnh báo sớm nguy cơ đột quỵ. Một công cụ như vậy có thể giúp các bác sĩ nhanh chóng xác định những bệnh nhân cần được quan tâm đặc biệt.

## 5.3. Hạn chế của dự án

Mặc dù đã đạt được những kết quả tích cực, dự án vẫn có một số hạn chế cần được nhìn nhận:
  Hạn chế về dữ liệu:
  Kích thước mẫu:Tập dữ liệu tương đối nhỏ, đặc biệt là số lượng ca bệnh đột quỵ (chỉ 249 ca), có thể hạn chế khả năng tổng quát hóa của mô hình.
  Số lượng biến:Tập dữ liệu thiếu một số thông tin y tế quan trọng khác có thể ảnh hưởng đến nguy cơ đột quỵ như mức cholesterol, tiền sử gia đình, chế độ ăn uống, mức độ hoạt động thể chất, v.v.
  Dữ liệu tự báo cáo:Tình trạng hút thuốc có thể không hoàn toàn chính xác do dựa trên sự tự khai báo của bệnh nhân.  Hạn chế về mô hình:
  SMOTE:Mặc dù SMOTE giúp cân bằng dữ liệu, các mẫu tổng hợp được tạo ra có thể không hoàn toàn phản ánh thực tế, có khả năng gây ra một số vùng quyết định không tối ưu.
  Tính tổng quát:Mô hình được xây dựng trên một tập dữ liệu cụ thể và có thể cần được kiểm định và hiệu chỉnh lại trên các tập dữ liệu từ các quần thể dân số khác nhau trước khi có thể áp dụng rộng rãi.

## 5.4. Đề xuất cải thiện và hướng phát triển trong tương lai

Để khắc phục các hạn chế và nâng cao giá trị của dự án, các hướng phát triển sau đây được đề xuất:

 5.4.1. Về dữ liệu
  Thu thập thêm dữ liệu:Kết hợp với các nguồn dữ liệu khác hoặc thu thập dữ liệu từ các bệnh viện để có một tập dữ liệu lớn hơn, đa dạng hơn và chứa nhiều thông tin y tế chi tiết hơn.  Sử dụng dữ liệu theo thời gian (Longitudinal Data):Phân tích dữ liệu sức khỏe của bệnh nhân được thu thập qua nhiều thời điểm khác nhau có thể giúp phát hiện các xu hướng và yếu tố nguy cơ một cách chính xác hơn.

 5.4.2. Về mô hình
  Thử nghiệm các kỹ thuật xử lý mất cân bằng khác:So sánh hiệu quả của SMOTE với các phương pháp khác như ADASYN, Tomek Links, hoặc các phương pháp kết hợp over-sampling và under-sampling.  Sử dụng các kiến trúc mô hình tiên tiến hơn:Khám phá các mô hình Deep Learning (Mạng nơ-ron sâu) nếu có tập dữ liệu đủ lớn, vì chúng có thể tự động học các mối quan hệ phức tạp mà không cần tạo biến thủ công.  Xây dựng mô hình diễn giải được (Interpretable Models):Tập trung vào các mô hình vốn có tính diễn giải cao hoặc áp dụng sâu hơn các kỹ thuật như LIME, SHAP để xây dựng niềm tin cho người dùng cuối (bác sĩ, bệnh nhân).

 5.4.3. Về phương pháp đánh giá
  Kiểm định chéo lồng nhau (Nested Cross-Validation):Sử dụng phương pháp này để có được một ước tính khách quan hơn về hiệu suất của mô hình trên dữ liệu hoàn toàn mới.  Phân tích chi phí - lợi ích:Đánh giá mô hình không chỉ dựa trên các chỉ số kỹ thuật mà còn dựa trên chi phí của việc dự đoán sai (ví dụ: chi phí của việc bỏ sót một ca bệnh so với chi phí của việc chẩn đoán nhầm).

## 5.5. Lộ trình ứng dụng vào thực tế (Roadmap)

Để đưa kết quả của dự án vào ứng dụng thực tế, một lộ trình gồm các giai đoạn sau được đề xuất:

 5.5.1. Giai đoạn 1: Xây dựng sản phẩm tối thiểu (Proof of Concept)
  Phát triển một giao diện web hoặc ứng dụng đơn giản cho phép người dùng (bác sĩ) nhập thông tin của bệnh nhân và nhận lại kết quả dự đoán nguy cơ đột quỵ cùng với diễn giải về các yếu tố ảnh hưởng chính.

 5.5.2. Giai đoạn 2: Thử nghiệm và xác thực lâm sàng (Pilot & Validation)
  Hợp tác với các chuyên gia y tế và bệnh viện để thử nghiệm công cụ trong một môi trường có kiểm soát.  Thu thập phản hồi từ các bác sĩ và so sánh kết quả dự đoán của mô hình với chẩn đoán thực tế để đánh giá hiệu quả và độ tin cậy.

 5.5.3. Giai đoạn 3: Mở rộng và triển khai (Scale-up)
  Dựa trên kết quả xác thực, cải tiến và hoàn thiện sản phẩm.
- Mở rộng và Tích hợp (Scale-up & Integration): Tích hợp công cụ vào các hệ thống quản lý bệnh án điện tử (EMR) để trở thành một công cụ hỗ trợ quyết định lâm sàng hữu ích cho các bác sĩ trong công việc hàng ngày.

---

## Tài liệu tham khảo (Dành cho Lập trình viên)

Dưới đây là danh sách các tài liệu, thư viện và bài viết hữu ích cho các lập trình viên muốn tìm hiểu sâu hơn về quá trình phân tích dữ liệu bằng Python được sử dụng trong dự án này.

 1. Các thư viện Python chính

Đây là các thư viện mã nguồn mở đã được sử dụng. Việc tham khảo tài liệu gốc (chủ yếu bằng tiếng Anh) là kỹ năng quan trọng để nắm bắt thông tin chính xác và đầy đủ nhất.

Pandas: Thư viện nền tảng cho việc xử lý và phân tích dữ liệu dạng bảng (như đọc file CSV, làm sạch, biến đổi dữ liệu).
    *   [Trang tài liệu chính thức của Pandas](https://pandas.pydata.org/docs/)
Scikit-learn: Thư viện toàn diện cho các tác vụ học máy (xây dựng mô hình, đánh giá, tiền xử lý).
    *   [Trang tài liệu chính thức của Scikit-learn](https://scikit-learn.org/stable/documentation.html)
Matplotlib & Seaborn: Các thư viện mạnh mẽ để trực quan hóa dữ liệu, từ biểu đồ cơ bản đến phức tạp.
    *   [Trang tài liệu chính thức của Matplotlib](https://matplotlib.org/stable/contents.html)
    *   [Trang tài liệu chính thức của Seaborn](https://seaborn.pydata.org/)

 2. Hướng dẫn và Bài viết tiếng Việt

Các bài viết sau cung cấp hướng dẫn chi tiết bằng tiếng Việt về cách sử dụng Pandas để làm việc với dữ liệu.

TopDev (2020). *Phân tách dữ liệu với DataFrame trong Python*.
    Nội dung: Hướng dẫn các thao tác cơ bản với DataFrame của Pandas, từ việc đọc file CSV đến các bước phân tích ban đầu. Rất phù hợp cho người mới bắt đầu.
Nguyễn Văn Hiếu. *Thư viện Pandas trong Python*.
    Nội dung: Giới thiệu tổng quan về thư viện Pandas, các tính năng chính và ví dụ minh họa về các thao tác xử lý dữ liệu phổ biến.
ViMentor. *Đọc và ghi tệp CSV trong Python bằng mô-đun csv & Pandas*.
    Nội dung: So sánh hai cách tiếp cận để làm việc với file CSV trong Python, giúp hiểu rõ hơn về ưu điểm của việc sử dụng Pandas.

 3. Cộng đồng học tập

Facebook Groups: Các nhóm như "Python Việt Nam", "Machine Learning Cơ Bản" là nơi có cộng đồng lớn, sẵn sàng trao đổi và giải đáp các thắc mắc trong quá trình học và làm dự án.
Stack Overflow: Mặc dù là trang tiếng Anh, đây là nguồn tài nguyên không thể thiếu để tìm kiếm giải pháp cho các lỗi và vấn đề kỹ thuật cụ thể.