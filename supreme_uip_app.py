import streamlit as st
import os

# إعداد الصفحة
st.set_page_config(page_title="SUPREME UIP", layout="wide")

# التنسيق السيادي
st.markdown("""
<style>
    .stApp { background-color: #0F0F11; color: #E2E4E8; }
    h1, h3 { color: #D6A461 !important; text-align: center; }
    .stButton > button { background-color: #D6A461; color: #0F0F11; width: 100%; font-weight: bold; border-radius: 10px; }
    .stTextInput > div > div > input { border: 2px solid #D6A461; background-color: #1A1A1E; color: white; }
</style>
""", unsafe_allow_html=True)

# عرض الشعار
if os.path.exists("logo.png"):
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        st.image("logo.png", width=200)
else:
    st.error("خطأ: لم يتم العثور على الشعار.")

st.title("SUPREME UIP")
st.markdown("### العقل الموحد للهندسة والسيادة")

# منطق التحليل
query = st.text_input(">> اطرح تحديك الهندسي أو حياتك هنا...")
if st.button("تحليل موحد"):
    if query:
        st.write(f"--- تحليل: {query} ---")
        st.info("☀️ [خارجي]: تحليل الطاقة والمادة")
        st.info("📷 [خارجي]: الملاحظة والأنماط")
        st.info("⚡ [خارجي]: الكفاءة والقدرة")
        st.info("🧠 [داخلي]: العقل الاستراتيجي والمنطق")
        st.success("القرار السيادي: يتم التنفيذ بأعلى معايير الجودة.")
