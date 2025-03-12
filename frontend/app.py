
import streamlit as st
import requests

st.title("🎨 QuickDraw AI")

uploaded_file = st.file_uploader("Tải lên ảnh vẽ", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Ảnh đã tải lên", use_column_width=True)
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/predict/", files=files)

    if response.status_code == 200:
        result = response.json()
        st.write(f"🔍 Kết quả: {result['prediction']} (Độ tin cậy: {result['confidence']:.2f})")
    else:
        st.write("⚠️ Có lỗi xảy ra!")
