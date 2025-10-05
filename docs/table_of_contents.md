# ĐỒ ÁN PHÂN TÍCH DỮ LIỆU VỀ ĐỘT QUỴ

## MỤC LỤC

### CHƯƠNG 1: GIỚI THIỆU
1. Lý do chọn đề tài
2. Mục tiêu của đề tài
3. Phạm vi nghiên cứu
4. Đối tượng nghiên cứu
5. Phương pháp nghiên cứu
6. Bố cục báo cáo

### CHƯƠNG 2: CƠ SỞ LÝ THUYẾT
1. Những kiến thức liên quan về bệnh đột quỵ
   - 1.1 Tổng quan về bệnh đột quỵ
   - 1.2 Những yếu tố ảnh hưởng đến bệnh đột quỵ
   - 1.3 Các phương pháp chẩn đoán
2. Phương pháp phân tích dữ liệu
   - 2.1 Tiền xử lý dữ liệu
   - 2.2 Khám phá dữ liệu
   - 2.3 Trực quan hóa dữ liệu
3. Một số kỹ thuật thống kê và mô hình hóa
   - 3.1 Kiểm định thống kê
   - 3.2 Mô hình Logistic Regression
   - 3.3 Mô hình Random Forest
   - 3.4 Mô hình K-Nearest Neighbor

### CHƯƠNG 3: PHÂN TÍCH DỮ LIỆU VÀ DỰ ĐOÁN KHẢ NĂNG MẮC BỆNH

#### 3.1 Mô tả tập dữ liệu
- 3.1.1 Nguồn gốc và cấu trúc dữ liệu
- 3.1.2 Các biến và ý nghĩa

#### 3.2 Tiền xử lý dữ liệu
- 3.2.1 Xử lý giá trị thiếu
- 3.2.2 Xử lý dữ liệu ngoại lai
- 3.2.3 Mã hóa dữ liệu phân loại

#### 3.3 Khám phá dữ liệu (EDA)
- 3.3.1 Thống kê mô tả
- 3.3.2 Phân tích tương quan
- 3.3.3 Phân tích phân phối dữ liệu

#### 3.4 Trực quan hóa dữ liệu
- 3.4.1 Biểu đồ phân phối
- 3.4.2 Ma trận tương quan
- 3.4.3 Biểu đồ so sánh nhóm

#### 3.5 Xây dựng mô hình dự đoán
- 3.5.1 Phân chia dữ liệu
- 3.5.2 Xây dựng mô hình Logistic Regression
- 3.5.3 Xây dựng mô hình Random Forest
- 3.5.4 Xây dựng mô hình K-Nearest-Neighbor

#### 3.6 Thực nghiệm, kết quả và thảo luận
- 3.6.1 So sánh độ nhạy, độ đặc hiệu, F1-score của các mô hình
- 3.6.2 Đánh giá, so sánh các mô hình sử dụng đường cong ROC và diện tích dưới đường cong AUC
- 3.6.3 Kết quả xây dựng các mô hình dự đoán

### CHƯƠNG 4: KẾT LUẬN
1. Tổng kết kết quả nghiên cứu
2. Hướng phát triển đề tài

### TÀI LIỆU THAM KHẢO

---

## CẤU TRÚC THƯ MỤC DỰ ÁN

```
HeathCare---Dataset/
├── docs/
│   ├── TABLE_OF_CONTENTS.md
│   └── README.md
├── python/
│   ├── 01_khamPhaVaLamSachDuLieu.ipynb
│   ├── 02_phanTichThongKeVaTrucQuanHoa.ipynb
│   ├── 03_xayDungMoHinhMachineLearning.ipynb
│   └── 04_ketLuanVaDeXuat.ipynb
├── healthcare-dataset-stroke-data.csv.xls
└── README.md
```

## MÔ TẢ DATASET

**Tên dataset:** Healthcare Dataset Stroke Data
**Số lượng mẫu:** 5,110 bản ghi
**Số lượng thuộc tính:** 12 thuộc tính

### Các thuộc tính trong dataset:

1. **id**: Mã định danh duy nhất cho mỗi bệnh nhân
2. **gender**: Giới tính (Male/Female/Other)
3. **age**: Tuổi của bệnh nhân
4. **hypertension**: Tình trạng tăng huyết áp (0: Không, 1: Có)
5. **heart_disease**: Bệnh tim (0: Không, 1: Có)
6. **ever_married**: Tình trạng hôn nhân (Yes/No)
7. **work_type**: Loại công việc (Private/Self-employed/Govt_job/children/Never_worked)
8. **Residence_type**: Loại nơi cư trú (Urban/Rural)
9. **avg_glucose_level**: Mức glucose trung bình trong máu
10. **bmi**: Chỉ số khối cơ thể (Body Mass Index)
11. **smoking_status**: Tình trạng hút thuốc (formerly smoked/never smoked/smokes/Unknown)
12. **stroke**: Biến mục tiêu - Tình trạng đột quỵ (0: Không, 1: Có)

### Mục tiêu nghiên cứu:
- Phân tích các yếu tố nguy cơ gây đột quỵ
- Xây dựng mô hình dự đoán khả năng mắc bệnh đột quỵ
- So sánh hiệu quả của các thuật toán machine learning khác nhau
- Đưa ra khuyến nghị về phòng ngừa đột quỵ