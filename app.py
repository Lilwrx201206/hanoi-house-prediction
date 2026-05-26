import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium

# 1. Cấu hình trang web
st.set_page_config(page_title="Dự đoán Giá Nhà Đất", page_icon="🏠", layout="centered")

st.title("🏠 Hệ Thống Dự Đoán Giá Bất Động Sản Nội Thành Hà Nội")
st.write("Nhập thông tin căn nhà bên dưới để mô hình AI tính toán giá trị dự kiến.")

# 2. Tải mô hình AI đã đóng gói lên
@st.cache_resource # Giúp lưu vào bộ nhớ cache, không bị tải lại mỗi lần bấm nút
def load_my_model():
    return joblib.load("model/best_house_price_model.pkl")

try:
    model = load_my_model()
except:
    st.error("❌ Không tìm thấy file 'best_house_price_model.pkl'. Hãy đảm bảo file mô hình nằm cùng thư mục với file app.py này!")
    st.stop()

# 3. Tạo form nhập liệu cho người dùng
st.subheader("📝 Thông tin thuộc tính")
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Diện tích (m²):", min_value=10.0, max_value=1000.0, value=50.0, step=1.0)
with col2:
    bedrooms = st.number_input("Số phòng ngủ:", min_value=1, max_value=20, value=3, step=1)

st.subheader("📍 Vị trí tọa độ")
st.write("Mẹo: Mở Google Maps để lấy tọa độ chính xác của khu vực.")
col3, col4 = st.columns(2)

with col3:
    latitude = st.number_input("Vĩ độ (Latitude):", min_value=8.0, max_value=24.0, value=21.025, format="%.6f")
with col4:
    longitude = st.number_input("Kinh độ (Longitude):", min_value=102.0, max_value=110.0, value=105.813, format="%.6f")

# 4. Hiển thị bản đồ trực quan vị trí đã chọn
st.write("Vị trí căn nhà trên bản đồ:")
m = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker([latitude, longitude], popup="Căn nhà cần dự đoán", icon=folium.Icon(color='red', icon='home')).add_to(m)
st_folium(m, height=300, width=700, returned_objects=[])

st.markdown("---")

# 5. Xử lý dự đoán khi người dùng bấm nút
if st.button("💰 ĐỒNG Ý DỰ ĐOÁN GIÁ", type="primary", use_container_width=True):
    # Tạo DataFrame đúng cấu trúc các cột lúc train mô hình
    input_data = pd.DataFrame([{
        'area': area,
        'bedrooms': bedrooms,
        'latitude': latitude,
        'longitude': longitude
    }])
    
    # Mô hình dự đoán
    prediction = model.predict(input_data)[0]
    
    # Hiển thị kết quả ra màn hình công phu
    st.success("🎉 Kết quả dự đoán thành công!")
    st.metric(label="GIÁ TRỊ ƯỚC TÍNH CỦA BẤT ĐỘNG SẢN", value=f"{prediction:.2f} Tỷ VNĐ") 
    # (Bạn có thể sửa chữ 'Tỷ VNĐ' thành đơn vị đúng của dữ liệu bạn cào về)