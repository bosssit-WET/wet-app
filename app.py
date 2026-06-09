import streamlit as st
import datetime

# --- ส่วนของการจัดการข้อความ (แยกไว้เผื่อทำ 2 ภาษา) ---
TEXTS = {
    "title": "WET: What Eat Today? 🥗",
    "tier_label": "Tier: 2 - Home Cook 🏆",
    "warning": "⚠️ 1 รายการใกล้หมดอายุ: ผักบุ้ง (หมดอายุพรุ่งนี้)",
    "btn_cook": "ทำเมนูจากผักบุ้งเลย",
    "header_add": "Add New Ingredient",
    "label_name": "ชื่อวัตถุดิบ",
    "label_qty": "จำนวน (กรัม)",
    "label_date": "วันหมดอายุ",
    "btn_add": "Add to Fridge",
    "header_menu": "Recipe Suggestions",
    "msg_suggestion": "เมนูแนะนำวันนี้:"
}

# --- UI ของ WET ---
st.set_page_config(page_title="WET App", page_icon="🥗")

st.title(TEXTS["title"])

# Sidebar (Tier)
st.sidebar.header("User Profile")
st.sidebar.write(TEXTS["tier_label"])
st.sidebar.progress(85)

# Alert Section
st.warning(TEXTS["warning"])
if st.button(TEXTS["btn_cook"]):
    st.success("AI แนะนำ: ผัดผักบุ้งไฟแดง!")

# Add Ingredient Section
st.subheader(TEXTS["header_add"])
name = st.text_input(TEXTS["label_name"])
qty = st.number_input(TEXTS["label_qty"], min_value=0)
date = st.date_input(TEXTS["label_date"])
if st.button(TEXTS["btn_add"]):
    st.balloons()
    st.write(f"เพิ่ม {name} เข้าตู้เย็นแล้ว!")

# Menu Section
st.subheader(TEXTS["header_menu"])
st.info(TEXTS["msg_suggestion"])
st.write("1. กะเพราหมูสับ (ใช้เวลา 6 นาที)")
st.write("2. ไข่เจียว (ใช้เวลา 4 นาที)")
