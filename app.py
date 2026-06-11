import streamlit as st
import google.generativeai as genai

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="WET: What Eat Today?", page_icon="🥗", layout="wide")

# ส่วนรับ API Key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("ใส่ Gemini API Key ของคุณที่นี่", type="password")

# ระบบ Session State
if 'points' not in st.session_state: st.session_state.points = 50
if 'fridge' not in st.session_state: st.session_state.fridge = []

# ระบบคำนวณ Tier
def get_tier_info(points):
    if points < 100: return "Train Cook", 3, "🐣"
    elif points < 200: return "Home Cook", 5, "🏆"
    else: return "Hero Cook", 10, "🌟"

tier_name, daily_limit, icon = get_tier_info(st.session_state.points)

# แสดงผล Sidebar
st.sidebar.title(f"{icon} {tier_name}")
st.sidebar.write(f"คะแนนสะสม: {st.session_state.points} แต้ม")
st.sidebar.progress(min(st.session_state.points / 200, 1.0))

# หน้าหลัก
st.title("WET: What Eat Today? 🥗")
tab1, tab2, tab3 = st.tabs(["Dashboard", "Add Ingredient", "Recipe AI"])

with tab1:
    st.write(f"สวัสดี {tier_name}! คุณมีสิทธิ์ใช้ AI แนะนำเมนูได้ {daily_limit} ครั้งต่อวัน")
    st.write("วัตถุดิบในตู้เย็น:", st.session_state.fridge)

with tab2:
    name = st.text_input("ชื่อวัตถุดิบ")
    if st.button("บันทึก"):
        st.session_state.fridge.append(name)
        st.session_state.points += 10
        st.success(f"เพิ่ม {name} แล้ว!")
        st.rerun()

with tab3:
    st.subheader("Recipe AI")
    if st.button("ให้ AI แนะนำเมนู"):
        if not api_key:
            st.error("กรุณาใส่ API Key ในแถบ Sidebar ก่อน!")
        else:
            try:
                # เริ่มการตั้งค่าการเชื่อมต่อใหม่
                genai.configure(api_key=api_key)
                # ใช้รุ่นที่เสถียรและเป็นมาตรฐานปัจจุบัน
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"ฉันมีวัตถุดิบเหล่านี้ในตู้เย็น: {st.session_state.fridge} ช่วยแนะนำ {daily_limit} เมนูอาหารที่ทำจากวัตถุดิบเหล่านี้"
                response = model.generate_content(prompt)
                
                st.write(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
                st.write("คำแนะนำ: ตรวจสอบว่า API Key ถูกต้อง และไม่ได้จำกัดสิทธิ์ใน Google Cloud Console")
