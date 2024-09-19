import streamlit as st
import sympy
import yaml
import io
from page.utils.Ascii_Art import *
from page.utils.imgEncode import *


@st.fragment
def frag_download():
    st.download_button(
        label="Generate Your Key",
        data=yaml_data,
        file_name="keys.yaml",
        mime="application/x-yaml", 
    )
def embed_values(cipher, e, n):
    # 假设 cipher, e, n 都是341位整数
    # 将它们合并为一个1024位整数
    embedded_number = (cipher << (341 * 2)) | (e << 341) | n
    return embedded_number

def extract_values(embedded_number):
    # 解析 cipher, e, n
    n = embedded_number & ((1 << 341) - 1)
    e = (embedded_number >> 341) & ((1 << 341) - 1)
    cipher = (embedded_number >> (341 * 2)) & ((1 << 341) - 1)
    return cipher, e, n



with open("static/example/violet.jpg","rb") as file:
    st.sidebar.download_button("Input Sample 1", data=file, file_name="sample1.jpg", mime="image/jpg")

with open("static/example/sonik.jpg","rb") as file:
    st.sidebar.download_button("Input Sample 2", data=file, file_name="sample2.jpg", mime="image/jpg")

with open("static/example/bacteria.png","rb") as file:
    st.sidebar.download_button("Input Sample 3", data=file, file_name="sample3.png", mime="image/png")

with open("static/example/yuzi.jpg","rb") as file:
    st.sidebar.download_button("Input Sample 4", data=file, file_name="sample4.jpg", mime="image/jpg")

with open("static/example/banana_cat.jpg","rb") as file:
    st.sidebar.download_button("Input Sample 5", data=file, file_name="sample5.jpg", mime="image/jpg")

with open("static/example/fulilian.jpg","rb") as file:
    st.sidebar.download_button("Input Sample 6", data=file, file_name="sample6.jpg", mime="image/jpg")

with open("static/example/emoji.png","rb") as file:
    st.sidebar.download_button("Input Sample 7", data=file, file_name="sample7.png", mime="image/png")

with open("static/example/botanic.png","rb") as file:
    st.sidebar.download_button("Input Sample 8", data=file, file_name="sample8.png", mime="image/png")



st.title("Pattern Generator")
st.markdown("##### On this page, you can obtain and use your key, select the appropriate image (note that different images may be good or bad, which is also a part of the fun of customizing the pattern), leave a comment, and get a unique pattern")
st.image("static/8.png",caption="page workflow")
st.divider()
st.subheader("Work Space")
option = st.selectbox(
    "Have you already held a key?",
    ("Yes", "No"),
    index=None,
    placeholder="Yes or No",
)

if option == "No":
    prime1 = sympy.randprime(748288838313422294120286634350736906063837462003712, 1496577676626844588240573268701473812127674924007424)
    prime2 = sympy.randprime(374144419156711147060143317175368453031918731001856, 748288838313422294120286634350736906063837462003712)
    
    while prime1 == prime2:
        prime2 = sympy.randprime(374144419156711147060143317175368453031918731001856, 748288838313422294120286634350736906063837462003712)
    n=prime1*prime2
    phi=(prime1-1)*(prime2-1)
    e=sympy.randprime(1,phi)
    d=sympy.mod_inverse(e,phi)
    data = {
    'n': n,
    'e': e,
    'd': d
    }
    yaml_data = yaml.dump(data)
    frag_download()

elif option == "Yes":
    uploaded_key = st.file_uploader("Upload your key in YAML file", type="yaml")
    if uploaded_key is not None:
        file_content = uploaded_key.read()
        try:
            data = yaml.safe_load(file_content)
            # 从 YAML 数据中提取 n, e, d
            n = data.get('n')
            e = data.get('e')
            d = data.get('d')
            # 显示提取的值
        except yaml.YAMLError as exc:
            st.error(f"Error reading YAML file: {exc}")
 
        uploaded_file = st.file_uploader("Upload a square image, preferably simple", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            str = st.text_input("Enter personalized words", placeholder="only ascii symbols allowed")
            if str != "":
                nstr = int.from_bytes(str.encode('utf-8'), 'big')
                if nstr > n:
                    st.error("The number is too large, please enter again")
                else:
                    cipher = pow(nstr, e, n)
                    embedded_number = embed_values(cipher, d, n)
                    pattern_image =create_square_pattern(embedded_number)         
                    colored_ascii_image, colored_ascii_image_chars, colored_ascii_image_colors = image_to_colored_ascii(uploaded_file, output_width, output_height)
                    base_image=colored_ascii_image_as_picture(colored_ascii_image_chars, colored_ascii_image_colors, colored_ascii_image_font, colored_ascii_image_font_size)
                    if base_image is not None and pattern_image is not None:
                            img=overlay_pattern_on_image(base_image, pattern_image, offset_x, offset_y)
                            with st.container(border=True):
                                st.image(img)
                            img_byte_arr = io.BytesIO()
                            img.save(img_byte_arr, format='PNG')
                            img_byte_arr = img_byte_arr.getvalue()
                            st.download_button(label="Download image", data=img_byte_arr, file_name="image.png", mime="image/png")

                   
