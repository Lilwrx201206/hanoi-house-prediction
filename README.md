# 🏠 Hệ Thống Dự Đoán Giá Bất Động Sản Hà Nội (Hanoi House Price Prediction)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![ML Framework](https://img.shields.io/badge/framework-Scikit--Learn-orange)

Một ứng dụng **End-to-End Machine Learning** hoàn chỉnh từ bước thu thập dữ liệu (Web Scraping), xử lý dữ liệu nhiễu, huấn luyện thô diện rộng, tinh chỉnh siêu tham số cho đến đóng gói thuật toán và triển khai giao diện Web trực quan. Hệ thống đạt độ chính xác chốt hạ **85.47%** trên tập dữ liệu kiểm thử độc lập (Test set).

---

## 📈 Tóm Tắt Vòng Đời & Kết Quả Dự Án

### 1. Thử Nghiệm Mô Hình Diện Rộng (Baseline Evaluation)
Trong giai đoạn đầu, dữ liệu sau khi xử lý được đưa vào thử nghiệm đồng thời trên nhiều thuật toán khác nhau. Kết quả chấm điểm trên bộ dữ liệu **Validation** chứng minh sự vượt trội của nhóm thuật toán dựa trên cây quyết định (Tree-based) so với mô hình tuyến tính:

| Thứ hạng | Thuật toán | MAE (Sai số trung bình) | RMSE (Phạt lỗi nặng) | R2 Score (Độ chính xác) |
| :---: | :--- | :---: | :---: | :---: |
| 🏆 **1** | **Random Forest** | **14.867** | **36.514** | **87.90%** |
| 🥈 **2** | Gradient Boosting | 16.985 | 42.259 | 83.79% |
| 🥉 **3** | XGBoost | 17.446 | 48.355 | 78.77% |
| 4 | Linear Regression | 36.610 | 73.528 | 50.92% |

### 2. Tinh Chỉnh Siêu Tham Số & Đánh Giá Chốt Hạ
Sử dụng kỹ thuật `GridSearchCV` trên mô hình dẫn đầu **Random Forest** với 108 lượt thử nghiệm (fits), hệ thống đã tìm ra bộ cấu hình tối ưu nhất:
* Cấu hình tối ưu: `{'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 200}`

Khi mang mô hình này đi đánh giá lần đầu tiên trên bộ dữ liệu bí mật (**Test Set**), kết quả đạt được vô cùng ấn tượng và ổn định:
* **MAE (Sai số thực tế):** `15.935`
* **R2 Score (Độ chính xác thực tế):** **`85.47%`** (Lệch < 2% so với bộ Validation, chứng minh mô hình không bị hiện tượng học vẹt - Overfitting).

---

## 📂 Cấu Trúc Mã Nguồn Dự Án

```text
hanoi-house-prediction/
│
├── best_house_price_model.pkl  # Bộ não AI (Mô hình Random Forest đã tối ưu)
├── app.py                      # Mã nguồn ứng dụng Web (Streamlit + Folium Map)
├── requirements.txt            # Danh sách các thư viện cần thiết để chạy dự án
└── README.md                   # Tài liệu hướng dẫn này