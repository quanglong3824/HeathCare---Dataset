# PHÂN TÍCH DỮ LIỆU ĐỘT QUỴ

## Giới thiệu
Dự án này tập trung vào việc phân tích dữ liệu liên quan đến bệnh đột quỵ, nhằm xây dựng mô hình dự đoán nguy cơ đột quỵ dựa trên các yếu tố nguy cơ.

## Cấu trúc dự án
```
PHAN_TICH_DOT_QUY/
│
├── 📂 data/                 # Chứa dữ liệu gốc và dữ liệu xử lý
│   ├── raw/                 # Dữ liệu gốc (CSV chưa đụng chạm)
│   ├── processed/           # Dữ liệu sau khi làm sạch, feature engineering
│   └── external/            # Nếu có dữ liệu bổ sung (WHO, CDC, ...)
│
├── 📂 notebooks/            # Jupyter Notebooks cho từng giai đoạn
│   ├── 01_exploration.ipynb # Khám phá dữ liệu, EDA
│   ├── 02_cleaning.ipynb    # Tiền xử lý dữ liệu
│   ├── 03_modeling.ipynb    # Huấn luyện mô hình
│   └── 04_visualization.ipynb # Vẽ biểu đồ trực quan
│
├── 📂 src/                  # Code Python tách riêng (tái sử dụng, sạch sẽ)
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── modeling.py
│   └── visualization.py
│
├── 📂 reports/              # Báo cáo & kết quả
│   ├── figures/             # Hình ảnh biểu đồ xuất ra
│   ├── tables/              # Bảng kết quả, thống kê
│   └── final_report.docx    # Báo cáo chính (hoặc PDF)
│
├── 📂 tests/                # Nếu có viết unit test cho code (optional)
│
├── requirements.txt         # Liệt kê thư viện cần thiết
├── README.md                # Giới thiệu dự án, cách chạy
└── .gitignore               # Nếu dùng Git, bỏ qua file nặng/không cần
```

## Cài đặt

```bash
pip install -r requirements.txt
```

## Sử dụng

1. Khám phá dữ liệu: Chạy notebook `notebooks/01_exploration.ipynb`
2. Tiền xử lý dữ liệu: Chạy notebook `notebooks/02_cleaning.ipynb`
3. Huấn luyện mô hình: Chạy notebook `notebooks/03_modeling.ipynb`
4. Trực quan hóa kết quả: Chạy notebook `notebooks/04_visualization.ipynb`

## Thư viện sử dụng
Xem chi tiết trong file `requirements.txt`