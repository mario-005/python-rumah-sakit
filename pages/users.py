import streamlit as st
import pandas as pd
from init import get_db_connection
from streamlit_option_menu import option_menu
from navigation import sidebar_0722

def fetch_data_0722():
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT * FROM users')  
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [desc[0] for desc in cursor_0722.description]
        data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
        cursor_0722.close()
        connection_0722.close()
        return data_0722
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def add_user_0722(username_0722, password_0722, role_0722='limited'):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('INSERT INTO users (username, password, role) VALUES (%s, %s, %s)', (username_0722, password_0722, role_0722))  # Tambahkan "0722" di sini
        connection_0722.commit()
        cursor_0722.close()
        connection_0722.close()
        st.success(f'User "{username_0722}" registered successfully!')

def delete_user_0722(username_0722):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('DELETE FROM users WHERE username = %s', (username_0722,))  
        connection_0722.commit()
        cursor_0722.close()
        connection_0722.close()
        st.success(f'User "{username_0722}" deleted successfully!')

def edit_user_0722(old_username_0722, new_password_0722, new_role_0722):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('UPDATE users SET password = %s, role = %s WHERE username = %s',
                       (new_password_0722, new_role_0722, old_username_0722))  
        connection_0722.commit()
        cursor_0722.close()
        connection_0722.close()
        st.success(f'User "{old_username_0722}" updated successfully!')

def register_user_section_0722():
    st.header('Register New User')
    user_username_0722 = st.text_input('Username')
    user_password_0722 = st.text_input('Password', type='password')
    user_role_0722 = st.selectbox('Role', ("admin", "limited"))
    if st.button('Register User'):
        if user_username_0722 and user_password_0722 and user_role_0722:
            add_user_0722(user_username_0722, user_password_0722, user_role_0722)
        else:
            st.error('Please enter both username and password.')

def delete_user_section_0722():
    st.header('Delete User')
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT username FROM users')  
        user_username_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
        user_username = st.selectbox("Pilih Username untuk Dihapus", options=[user_username[0] for user_username in user_username_0722])
    if st.button('Delete User'):
        if user_username:
            delete_user_0722(user_username)
        else:
            st.error('Please enter a username.')

def edit_user_section_0722():
    st.header('Edit User')
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT username FROM users')  
        user_username_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
        old_username_0722 = st.selectbox("Pilih Username untuk Diedit", options=[old_username_0722[0] for old_username_0722 in user_username_0722])
        new_password_0722 = st.text_input('New Password', type='password')
        new_role_0722 = st.selectbox('New Role', ("admin", "limited"))
    if st.button('Update User'):
        if old_username_0722 and new_password_0722 and new_role_0722:
            edit_user_0722(old_username_0722, new_password_0722, new_role_0722)
        else:
            st.error('Please fill in all fields.')

def users_data_section_0722():
    st.title('Data User')
    data_0722 = fetch_data_0722()
    if not data_0722.empty:
        st.dataframe(data_0722, hide_index=True)
    else:
        st.write("No data available.")

sidebar_0722()
pilihan_0722 = option_menu(
    menu_title=None,
    options=["Register", "Delete", "Edit", "Users"],
    icons=["person-plus-fill", "trash", "pencil", "card-checklist"],
    orientation="horizontal",
)

if pilihan_0722 == "Register":
    register_user_section_0722()
elif pilihan_0722 == "Users":
    users_data_section_0722()
elif pilihan_0722 == "Delete":
    delete_user_section_0722()
elif pilihan_0722 == "Edit":
    edit_user_section_0722()
