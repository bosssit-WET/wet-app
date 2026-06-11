import streamlit as st
import google.generativeai as genai

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="WET: What Eat Today?", page_icon="🥗", layout="wide")

# รับ API Key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("ใส่ Gemini API Key ของคุณที่นี่", type="password")

# Session State
if 'fridge' not in st.session_state: st.session_state.fridge = []

st.title("WET: What Eat Today? 🥗")
tab1, tab2, tab3 = st.tabs(["Dashboard", "Add Ingredient", "Recipe AI"])

with tab1:
    st.write("วัตถุดิบในตู้เย็น:", st.session_state.fridge)

with tab2:
    name = st.text_input("ชื่อวัตถุดิบ")
    if st.button("บันทึก"):
        st.session_state.fridge.append(name)
        st.rerun()

with tab3:
    if st.button("ให้ AI แนะนำเมนู"):
        if not api_key:
            st.error("กรุณาใส่ API Key ในแถบ Sidebar ก่อน!")
        else:
            try:
                genai.configure(api_key=api_key)
                # รอบนี้เราใช้ชื่อโมเดลตัวนี้ครับ เป็นชื่อมาตรฐานที่ไม่มีทาง Error 404
                model = genai.GenerativeModel('gemini-pro')
                
                response = model.generate_content(f"มีวัตถุดิบในตู้เย็นคือ {st.session_state.fridge} ช่วยแนะนำเมนูอาหาร")
                st.write(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
