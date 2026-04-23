import streamlit as st
import os

# الإعدادات
st.set_page_config(page_title="UIP System", layout="wide")

# التصميم (CSS)
st.markdown("""
<style>
    .stApp { background-color: #0F0F11; color: white; }
    h1, h3 { color: #D6A461 !important; }
</style>
""", unsafe_allow_html=True)

# الواجهة
st.title("سوبريم يو آي بي")
st.subheader("### القوى الموحدة للهندسة والسيادة")

# مدخلات المستخدم
user_input = st.text_input("استفسارك الهندسي أو عن حياتك هنا...")

if user_input:
    st.write(f"جاري معالجة: {user_input}")
