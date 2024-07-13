# Kelas: SI-47-07
# Kelompok: 22
# Anggota Kelompok:
# 1. Hafidz Nur Hilmi (102022330288)
# 2. Berkah Aryo Bima Sakti (102022300237)
# 3. Muhammad Fizry Alifta (102022300222)
# 4. Benediktus Mario Laksono (102022300270)
# 5. Faiz Dhya Muhammad Rahmantyo (102022300144)

import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

def current_page_0722():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]

def sidebar_0722():
    st.set_page_config(page_title="Alpro Hospital", page_icon=":hospital:", layout="wide")
    with st.sidebar:
        st.title("🏥 ALPRO HOSPITAL")                

        if st.session_state.get("logged_in", False):
            role_0722 = st.session_state.get("role", "limited")

            if role_0722 == "admin":
                st.write("Role : Admin ")
                st.write("")
                st.page_link("pages/pasien.py", label=" Pasien", icon="👦🏻")
                st.page_link("pages/dokter.py", label=" Dokter", icon="👨🏻‍⚕️")
                st.page_link("pages/perawat.py", label=" Perawat", icon="👩🏻‍⚕️")
                st.page_link("pages/kamar.py", label=" Kamar", icon="🛏️")
                st.page_link("pages/users.py", label=" Users", icon="🧔🏻")
            elif role_0722 == "limited":
                st.markdown("Role : Limited ")
                st.write("")
                st.page_link("pages/pasien.py", label=" Pasien", icon="👦🏻")
                st.page_link("pages/dokter.py", label=" Dokter", icon="👨🏻‍⚕️")
            
            st.write("")
            st.write("")

            if st.button("Log out"):
                logout_0722()

        elif current_page_0722() != "app":
            st.switch_page("app.py")

def logout_0722():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.info("Logged out!")
    sleep(0.5)
    st.switch_page("app.py")
