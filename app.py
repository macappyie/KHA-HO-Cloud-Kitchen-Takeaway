import streamlit as st

st.set_page_config(page_title="KHA-HO Menu", layout="wide")

st.title("🍽️ KHA-HO Cloud Kitchen & Takeaway")

# Load HTML file
with open("kha-ho-menu.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=900, scrolling=True)

