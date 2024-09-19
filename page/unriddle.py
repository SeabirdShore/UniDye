import streamlit as st
from page.utils.imgDecode import *
#from page.utils.imgEncode import *

def extract_values(embedded_number):
    # 解析 cipher, e, n
    n = embedded_number & ((1 << 341) - 1)
    e = (embedded_number >> 341) & ((1 << 341) - 1)
    cipher = (embedded_number >> (341 * 2)) & ((1 << 341) - 1)
    return cipher, e, n

st.title("Uncover Inside Story")
st.markdown("##### In this page, you can uncover the message hidden in the pattern")
st.image("static/10.png")
st.divider()
st.subheader("Work Space")
img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if img is not None:
    st.image(img)
    extracted_number= extract_number_from_image(img, offset_x, offset_y)
    cipher,d,n=extract_values(extracted_number)
    x = pow(cipher,d,n)
    x_bytes = x.to_bytes((x.bit_length() + 7) // 8, 'big')
    st.header(f"Hidden Message: {x_bytes.decode('utf-8')}")