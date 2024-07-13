# Kelas: SI-47-07
# Kelompok: 22
# Anggota Kelompok:
# 1. Hafidz Nur Hilmi (102022330288)
# 2. Berkah Aryo Bima Sakti (102022300237)
# 3. Muhammad Fizry Alifta (102022300222)
# 4. Benediktus Mario Laksono (102022300270)
# 5. Faiz Dhya Muhammad Rahmantyo (102022300144)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from init import get_db_connection
from navigation import sidebar_0722
sidebar_0722()

def fetch_kamar_0722():
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT * FROM Kamar')
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [desc[0] for desc in cursor_0722.description]
        cursor_0722.close()
        connection_0722.close()
        return pd.DataFrame(result_0722, columns=columns_0722)
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def display_kamar_0722():
    st.header('Data Kamar')
    data_0722 = fetch_kamar_0722()
    if not data_0722.empty:
        st.dataframe(data_0722, hide_index=True)
    else:
        st.write("No data available.")

def add_kamar_0722(id_kamar, id_pasien, nama_kamar, tipe_kamar):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('INSERT INTO kamar (id_kamar, id_pasien, nama_kamar, tipe_kamar) VALUES (%s,%s, %s, %s)', 
                       (id_kamar, id_pasien, nama_kamar, tipe_kamar))
        connection_0722.commit()
        cursor_0722.close()
        connection_0722.close()
        st.success(f'Kamar "{id_kamar}" registered successfully!')

def register_kamar_0722():
    st.header('Register Kamar')
    id_kamar_0722 = st.text_input('ID Kamar')
    id_pasien_0722 = st.text_input('ID Pasien')
    nama_kamar_0722 = st.text_input('Nama Kamar')
    tipe_kamar_0722 = st.selectbox('Tipe Kamar', ['VVIP', 'VIP', 'Reguler'])

    if st.button('Register Kamar'):
        if id_kamar_0722 and id_pasien_0722 and nama_kamar_0722 and tipe_kamar_0722:
            add_kamar_0722(id_kamar_0722, id_pasien_0722, nama_kamar_0722, tipe_kamar_0722)
        else:
            st.error('Please fill out all fields.')

def delete_kamar_0722():
    st.header("Hapus Data Kamar")
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT id_kamar FROM Kamar')
        daftar_kamar_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()

        id_kamar_0722 = st.selectbox("Pilih Kamar untuk Dihapus", options=[Kamar[0] for Kamar in daftar_kamar_0722])

        if st.button("Hapus Kamar"):
            try:
                connection_0722 = get_db_connection()
                if connection_0722:
                    cursor_0722 = connection_0722.cursor()
                    cursor_0722.execute('DELETE FROM Kamar WHERE id_kamar = %s', (id_kamar_0722,))
                    connection_0722.commit()
                    cursor_0722.close()
                    connection_0722.close()
                    st.success("Data kamar berhasil dihapus.")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                if connection_0722.is_connected():
                    cursor_0722.close()
                    connection_0722.close()
    else:
        st.error("Failed to connect to the database")

def edit_kamar_0722():
    st.header("Edit Data Kamar")

    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT id_kamar, nama_kamar FROM Kamar')
        daftar_kamar_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        daftar_kamar_0722 = []

    if daftar_kamar_0722:
        kamar_id_to_edit_0722 = st.selectbox("Select Kamar to Edit", options=[kamar[0] for kamar in daftar_kamar_0722])

        connection_0722 = get_db_connection()
        if connection_0722:
            cursor_0722 = connection_0722.cursor()
            cursor_0722.execute('SELECT * FROM Kamar WHERE id_kamar = %s', (kamar_id_to_edit_0722,))
            kamar_to_edit_0722 = cursor_0722.fetchone()
            cursor_0722.close()
            connection_0722.close()
        else:
            st.error("Failed to connect to the database")
            kamar_to_edit_0722 = None

        if kamar_to_edit_0722:
            st.write("")
            st.write(f"ID Kamar: {kamar_to_edit_0722[0]}")
            st.write(f"ID Pasien: {kamar_to_edit_0722[1]}")
            st.write(f"Nama Kamar: {kamar_to_edit_0722[2]}")
            st.write(f"Tipe Kamar: {kamar_to_edit_0722[3]}")
            st.write("---")
            
            edited_data_0722 = {
                "id_pasien": st.text_input("ID Pasien", value=kamar_to_edit_0722[1]),
                "nama_kamar": st.text_input("Nama Kamar", value=kamar_to_edit_0722[2]),
                "tipe_kamar": st.selectbox("Tipe Kamar", ['VVIP', 'VIP', 'Reguler'], index=['VVIP', 'VIP', 'Reguler'].index(kamar_to_edit_0722[3])),
            }

            if st.button("Save Changes"):
                connection_0722 = get_db_connection()
                if connection_0722:
                    cursor_0722 = connection_0722.cursor()
                    cursor_0722.execute(
                    'UPDATE Kamar SET id_pasien = %s, nama_kamar = %s, tipe_kamar = %s WHERE id_kamar = %s',
                    (edited_data_0722["id_pasien"], edited_data_0722["nama_kamar"], edited_data_0722["tipe_kamar"], kamar_id_to_edit_0722)
                    )
                    connection_0722.commit()
                    st.success("Changes saved successfully.")
                else:
                    st.error("Failed to save changes.")
def search_0722():
    st.header('Search Kamar')
    search_query_0722 = st.text_input('Masukkan Nama Kamar')

    if st.button('Search'):
        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute("SELECT * FROM kamar WHERE nama_kamar LIKE %s", ('%' + search_query_0722 + '%',))
            result_0722 = cursor_0722.fetchall()
            columns_0722 = [desc[0] for desc in cursor_0722.description]
            data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
            cursor_0722.close()
            conn_0722.close()
            
            if not data_0722.empty:
                st.dataframe(data_0722, hide_index=True)
            else:
                st.write("Tidak Menemukan Data.")
        else:
            st.error("Erorr!!!")
def filter_0722():
    st.header('Filter kamar Berdasarkan Tipe Kamar')
    
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute("SELECT DISTINCT tipe_kamar FROM kamar")
        tipe_kamar_0722 = [row[0] for row in cursor_0722.fetchall()]
        cursor_0722.close()
        conn_0722.close()
    else:
        st.error("Failed to connect to the database")
        tipe_kamar_0722 = []
    
    selected_type = st.selectbox('Pilih Tipe Kamar', options=tipe_kamar_0722)
    
    if st.button('Filter'):
        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute("SELECT * FROM kamar WHERE tipe_kamar = %s", (selected_type,))
            result_0722 = cursor_0722.fetchall()
            columns_0722 = [desc[0] for desc in cursor_0722.description]
            data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
            cursor_0722.close()
            conn_0722.close()
            
            if not data_0722.empty:
                st.dataframe(data_0722, hide_index=True)
            else:
                st.write("Tidak Menemukan Data")
        else:
            st.error("Error!!!!")
            
def visualisasi_data_0722():
    st.header('Visualisasi Data Kamar Berdasarkan Tipe Kamar')

    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT tipe_kamar FROM Kamar')
        tipe_kamar_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        return
    
    df_0722 = pd.DataFrame(tipe_kamar_0722, columns=['tipe_kamar'])

    gender_counts_0722 = df_0722['tipe_kamar'].value_counts()

    fig, ax = plt.subplots(figsize=(14, 3.5))
    gender_counts_0722.plot(kind='bar', color=['skyblue', 'green', 'blue'], ax=ax)
    ax.set_title('Visualisasi Data Kamar')
    ax.set_xlabel('Room Type')
    ax.set_ylabel('Count')
    ax.set_xticks(range(len(gender_counts_0722)))
    ax.set_xticklabels(gender_counts_0722.index, rotation=0)

    st.pyplot(fig)


selected_0722 = option_menu(
    menu_title=None,
    options=["Kamar", "Register", "Delete", "Edit", "Search", "Filter"],
    icons=["hospital", "building-add", "trash", "pencil", "search", "building"],
    orientation="horizontal",
)

if selected_0722 == "Kamar":
    display_kamar_0722()
    visualisasi_data_0722()
elif selected_0722 == "Register":
    register_kamar_0722()
elif selected_0722 == "Delete":
    delete_kamar_0722()
elif selected_0722 == "Edit":
    edit_kamar_0722()
elif selected_0722 == "Search":
    search_0722()
elif selected_0722 == "Filter" :
    filter_0722()
