# Kelas: SI-47-07
# Kelompok: 22
# Anggota Kelompok:
# 1. Hafidz Nur Hilmi (102022330288)
# 2. Berkah Aryo Bima Sakti (102022300237)
# 3. Muhammad Fizry Alifta (102022300222)
# 4. Benediktus Mario Laksono (102022300270)
# 5. Faiz Dhya Muhammad Rahmantyo (102022300144)

import streamlit as st
import requests
from time import sleep
from init import get_db_connection
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(page_title="Hospital Alpro",page_icon=":hospital:", layout="wide")
lottie_load_0722 = load_lottieurl("https://lottie.host/8f4c085c-5342-4ace-b8b0-f1ed7af1c8a2/reggXvxZ4q.json")

def login_0722(username, password):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT username, password, role FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor_0722.fetchone()
        cursor_0722.close()
        connection_0722.close()
        if user:
            return {'username': user[0], 'role': user[2]}
        else:
            return None

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("HOSPITAL ALPRO 22 🏥")
        st.write("Please log in to continue.")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Log in", type="primary"):
            user_info = login_0722(username, password)
            if user_info:
                st.session_state.logged_in = True
                st.session_state.username = user_info['username']
                st.session_state.role = user_info['role']
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/pasien.py")  
            else:
                st.error("Incorrect username or password")
    with right_column:
        st_lottie(lottie_load_0722, height=375, key="coding", speed=0.75)
    st.write("---")
