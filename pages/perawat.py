import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from init import get_db_connection
from navigation import sidebar_0722
sidebar_0722()

def fetch_perawat_0722():
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('SELECT * FROM perawat')
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [desc[0] for desc in cursor_0722.description]
        data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
        cursor_0722.close()
        conn_0722.close()
        return data_0722
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def add_perawat_0277(id_perawat, nama_perawat, jenis_kelamin, usia):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute(
            'INSERT INTO perawat(ID_perawat, nama_perawat, jenis_kelamin, usia) VALUES (%s, %s, %s, %s)', 
            (id_perawat, nama_perawat, jenis_kelamin, usia)
        )
        conn_0722.commit()
        cursor_0722.close()
        conn_0722.close()
        st.success(f'Perawat "{nama_perawat}" registered successfully!')

def login(username, password):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute(
            'SELECT username, password FROM users WHERE username = %s AND password = %s', 
            (username, password)
        )
        user_0722 = cursor_0722.fetchone()
        cursor_0722.close()
        conn_0722.close()
        return user_0722 is not None
    return False

def show_filtering_0722():
    st.header('Data Perawat')
    min_age_0722 = st.number_input("Usia Minimum", min_value=0, max_value=100)
    max_age_0722 = st.number_input("Usia Maksimum", min_value=0, max_value=100)
    
    data_0722 = fetch_perawat_0722()
    filtered_data_0722 = data_0722[(data_0722['usia'] >= min_age_0722) & (data_0722['usia'] <= max_age_0722)]
    if not filtered_data_0722.empty:
        st.dataframe(filtered_data_0722, hide_index=True)
    else:
        st.write("Tidak ada data tersedia.")

def show_searching_0722():
    st.header('Data Perawat')
    search_0722 = st.text_input("Search Based On ID_Perawat")
    data_0722 = fetch_perawat_0722()
    if search_0722:
        try:
            search_id_0722 = int(search_0722)
            searched_data_0722 = data_0722[data_0722['ID_perawat'] == search_id_0722]
            if not searched_data_0722.empty:
                st.dataframe(searched_data_0722, hide_index=True)
            else:
                st.write("Tidak ada data tersedia.")
        except ValueError:
            st.error("ID Perawat harus berupa angka.")

def show_perawat_0277():
    st.header('Data Perawat')
    data_0722 = fetch_perawat_0722()
    if not data_0722.empty:
        st.dataframe(data_0722, hide_index=True)
    else:
        st.write("No data available.")

def show_register_perawat_0722():
    st.header('Register Perawat')
    id_perawat_0722 = st.text_input('ID_perawat')
    nama_perawat_0722 = st.text_input('Nama Perawat')
    jenis_kelamin_0722= st.selectbox('Jenis Kelamin', ("Laki-Laki", "Perempuan"))
    usia_0722 = st.text_input('Usia')

    if st.button('Register Perawat'):
        if id_perawat_0722 and nama_perawat_0722 and jenis_kelamin_0722 and usia_0722:
            add_perawat_0277(id_perawat_0722, nama_perawat_0722, jenis_kelamin_0722, usia_0722)
        else:
            st.error('Harap masukan semua informasi')

def show_delete_perawat_0722():
    st.header("Hapus Data Perawat")
    id_perawat_0722 = st.text_input('ID Perawat')

    if st.button("Hapus Perawat"):
        if id_perawat_0722:
            try:
                id_perawat_0722 = int(id_perawat_0722)  # Ensure ID is an integer
                conn_0722 = get_db_connection()
                if conn_0722:
                    cursor_0722 = conn_0722.cursor()
                    cursor_0722.execute('DELETE FROM perawat WHERE ID_perawat = %s', (id_perawat_0722,))
                    conn_0722.commit()
                    cursor_0722.close()
                    conn_0722.close()
                    st.success("Data perawat berhasil dihapus.")
            except ValueError:
                st.error("ID Perawat harus berupa angka.")
            except Exception as e:
                st.error(f"Error: {e}")

def show_edit_perawat_0277():
    st.header("Edit Data Perawat")
    conn_0722= get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('SELECT ID_perawat, nama_perawat FROM perawat')
        daftar_perawat_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        conn_0722.close()
    else:
        st.error("Failed to connect to the database")
        return

    if daftar_perawat_0722:
        perawat_id_to_edit_0722 = st.selectbox("Select Perawat to Edit", options=[perawat[0] for perawat in daftar_perawat_0722])
        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute('SELECT * FROM perawat WHERE ID_perawat = %s', (perawat_id_to_edit_0722,))
            perawat_to_edit_0722 = cursor_0722.fetchone()
            cursor_0722.close()
            conn_0722.close()
        else:
            st.error("Failed to connect to the database")
            return

        if perawat_to_edit_0722:
            st.write("")
            st.write(f"ID Perawat: {perawat_to_edit_0722[0]}")
            st.write(f"Nama Perawat: {perawat_to_edit_0722[1]}")
            st.write(f"Jenis Kelamin: {perawat_to_edit_0722[2]}")
            st.write(f"Usia: {perawat_to_edit_0722[3]}")
            st.write("---")

            edited_data_0722 = {
                "nama_perawat": st.text_input("Nama Perawat", value=perawat_to_edit_0722[1]),
                "jenis_kelamin": st.selectbox("Jenis Kelamin", options=["Laki-laki", "Perempuan"], index=0 if perawat_to_edit_0722[2] == "Laki-laki" else 1),
                "usia": st.text_input("Usia", value=perawat_to_edit_0722[3])
            }

            if st.button("Simpan Perubahan"):
                conn_0722 = get_db_connection()
                if conn_0722:
                    cursor_0722 = conn_0722.cursor()
                    cursor_0722.execute(
                        'UPDATE perawat SET nama_perawat = %s, jenis_kelamin = %s, usia = %s WHERE ID_perawat = %s', 
                        (edited_data_0722["nama_perawat"], edited_data_0722["jenis_kelamin"], edited_data_0722["usia"], perawat_id_to_edit_0722)
                    )
                    conn_0722.commit()
                    cursor_0722.close()
                    conn_0722.close()
                    st.success("Perubahan berhasil disimpan.")
                else:
                    st.error("Gagal menyimpan perubahan")

def visualisasi_data_0277():
    st.header('Visualisasi Data Pasien Berdasarkan Umur per 10 Tahun')
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT usia FROM perawat')
        data_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        return
    data_0722 = fetch_perawat_0722()
    if not data_0722.empty:
        fig, ax = plt.subplots(figsize=(14, 3.5))
        ax.hist(data_0722['usia'], bins=range(20, 51, 10), edgecolor='black', color='skyblue')
        ax.set_title('Age Distribution of Perawat')
        ax.set_xlabel('Age')
        ax.set_ylabel('Count')
        ax.set_xticks(range(20, 51, 10))
        
        st.pyplot(fig)
    else:
        st.write("No data available.")


pilihan_0722 = option_menu(
    menu_title=None,
    options=["Perawat", "Register", "Delete", "Edit", "Searching", "Filtering"],
    icons=["people", "person-plus-fill", "trash", "pencil", "search", "card-checklist"],
    orientation="horizontal",
)

if pilihan_0722 == "Perawat":
    show_perawat_0277()
    visualisasi_data_0277()
elif pilihan_0722 == "Register":
    show_register_perawat_0722()
elif pilihan_0722 == "Delete":
    show_delete_perawat_0722()
elif pilihan_0722 == "Edit":
    show_edit_perawat_0277()
elif pilihan_0722 == "Searching":
    show_searching_0722()
elif pilihan_0722 == "Filtering":
    show_filtering_0722()
