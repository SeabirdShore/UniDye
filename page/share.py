import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io

# Azure Blob Storage 配置
AZURE_CONNECTION_STRING = ''
AZURE_CONTAINER_NAME = ''

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

def upload_to_blob(file, container_name, blob_name):
    try:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file)
        st.success("Image uploaded successfully")
        return True
    except Exception as e:
        st.error(f"Image uploading failed {e}")
        return False

# 上传图片到 Azure Blob Storage
@st.fragment
def upload_chunk():
    str = st.text_input("Enter Access Key")
    if str:
        if str==AZURE_CONTAINER_NAME:
            with st.popover("Upload by clicking here"):
                uploaded_file = st.file_uploader("Upload a processed image",type=["jpg", "jpeg", "png"])
                if uploaded_file:
                    upload_to_blob(uploaded_file, AZURE_CONTAINER_NAME, uploaded_file.name)
        else:
            st.error("Stop hacking, we are research project!")

# 从 Azure Blob Storage 获取所有图片
def get_images_from_blob(container_name):
    try:
        blob_list = container_client.list_blobs()
        return [blob.name for blob in blob_list]
    except Exception as e:
        st.error(f"获取图片失败: {e}")
        return []

# 显示图片墙
def display_image_wall(blob_names, container_name):
    cols = st.columns(3)
    for i, blob_name in enumerate(blob_names):
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob().readall()
        img = Image.open(io.BytesIO(blob_data))
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        with cols[i % 3]:
            st.image(img, use_column_width=True)
            st.download_button(label="Download", data=img_byte_arr, file_name=f"image{i}.png", mime="image/png")

@st.fragment
def show_image_wall():
    on = st.toggle("Activate Image Wall")
    if on:
        blob_names = get_images_from_blob(AZURE_CONTAINER_NAME)
        if blob_names:
            display_image_wall(blob_names, AZURE_CONTAINER_NAME)
        else:
            st.write("Wall is empty, go upload some pictures!")

st.title("Pattern Gallery")

st.markdown("##### In this page, you can see the patterns created by our community. You can also upload your own patterns to share with others!")
st.image("static/9.png",use_column_width=True)
upload_chunk()
st.divider()
show_image_wall()




