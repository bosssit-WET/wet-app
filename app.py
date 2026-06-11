import streamlit as st
import datetime

# --- การตั้งค่าหน้าจอ ---
st.set_page_config(page_title="WET: What Eat Today?", page_icon="🥗", layout="wide")

# --- ระบบจำลองข้อมูล (ในอนาคตเชื่อม Database) ---
if 'points' not in st.session_state: st.session_state.points = 50  # เริ่มต้นที่ 50 แต้ม
if 'fridge' not in st.session_state: st.session_state.fridge = []

# --- ฟังก์ชันคำนวณ Tier ---
def get_tier_info(points):
    if points < 100:
        return "Train Cook", 3, "🐣"
    elif points < 200:
        return "Home Cook", 5, "🏆"
    else:
        return "Hero Cook", 10, "🌟"

tier_name, daily_limit, icon = get_tier_info(st.session_state.points)

# --- แถบ Sidebar (แสดงสถานะ) ---
st.sidebar.title(f"{icon} {tier_name}")
st.sidebar.write(f"คะแนนสะสม: {st.session_state.points} แต้ม")
st.sidebar.progress(min(st.session_state.points / 200, 1.0))
st.sidebar.info(f"โควต้าเมนู AI: {daily_limit} เมนู/วัน")

# --- หน้าหลัก (Dashboard) ---
st.title("WET: What Eat Today? 🥗")
tab1, tab2, tab3 = st.tabs(["Dashboard", "Add Ingredient", "Recipe AI"])

with tab1:
    st.subheader("สถานะตู้เย็น")
    if not st.session_state.fridge:
        st.write("ตู้เย็นว่างเปล่า เริ่มเพิ่มวัตถุดิบกันเลย!")
    else:
        st.write(st.session_state.fridge)

with tab2:
    st.subheader("เพิ่มวัตถุดิบ")
    name = st.text_input("ชื่อวัตถุดิบ")
    qty = st.number_input("จำนวน (กรัม)", min_value=0)
    expiry = st.date_input("วันหมดอายุ")
    if st.button("บันทึกเข้าตู้เย็น"):
        st.session_state.fridge.append({"name": name, "qty": qty, "expiry": expiry})
        st.session_state.points += 10 # ได้แต้มจากการเพิ่มของ
        st.balloons()
        st.success(f"เพิ่ม {name} เรียบร้อย! ได้รับ 10 แต้ม")

with tab3:
    st.subheader("เมนูแนะนำอัจฉริยะ")
    st.write(f"สิทธิ์ของคุณคือ: {daily_limit} เมนู/วัน")
    
    if st.button("ให้ AI แนะนำเมนู"):
        if not st.session_state.fridge:
            st.error("กรุณาเพิ่มวัตถุดิบก่อนนะครับ!")
        else:
            st.write(f"--- แนะนำ {daily_limit} เมนูพิเศษสำหรับ {tier_name} ---")
            # ในอนาคตจะเชื่อม Gemini API ตรงนี้
            for i in range(1, daily_limit + 1):
                st.write(f"{i}. เมนูอร่อยจากวัตถุดิบในตู้เย็น")
