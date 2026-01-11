import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="Scan Komik Korea", layout="centered")

st.title("🇰🇷 Pemindai Komik Korea")
st.write("Unggah gambar komik untuk mengambil teksnya secara otomatis.")

# Fitur Upload Gambar
uploaded_file = st.file_uploader("Pilih Gambar Komik...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan Gambar
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar Berhasil Diunggah', use_container_width=True)
    
    with st.spinner('Sedang memproses teks Korea... Mohon tunggu.'):
        # Inisialisasi Reader EasyOCR
        reader = easyocr.Reader(['ko', 'en'])
        
        # Konversi gambar ke format yang dimengerti OCR
        img_array = np.array(image)
        results = reader.readtext(img_array, detail=0)
        
    st.success("Selesai!")
    st.subheader("Hasil Scan Teks:")
    
    if results:
        # Menampilkan teks dalam kotak yang bisa di-copy
        hasil_gabungan = "\n".join(results)
        st.text_area("Salin teks di sini:", value=hasil_gabungan, height=300)
    else:
        st.warning("Maaf, teks tidak terdeteksi pada gambar ini.")
