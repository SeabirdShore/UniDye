import streamlit as st
from page.utils.components import footer_style, footer

home_page=st.Page("page/home.py",title="Home")
sign_page=st.Page("page/sign.py",title="Signature")
share_page=st.Page("page/share.py",title="Community")
unriddle_page=st.Page("page/unriddle.py",title="Uncover")

pg=st.navigation([home_page,sign_page,share_page,unriddle_page])
st.set_page_config(page_title="UniDye",page_icon="static/3-1.png")

pg.run()

st.divider()
st.markdown(footer, unsafe_allow_html=True)