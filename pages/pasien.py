import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from init import get_db_connection
from navigation import sidebar_0722
sidebar_0722()

def pasien_0722():
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT * FROM pasien')
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [desc[0] for desc in cursor_0722.description]
        cursor_0722.close()
        connection_0722.close()
        return pd.DataFrame(result_0722, columns=columns_0722)
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def display_pasien_0722():
    st.header('Data Pasien')
    data_0722 = pasien_0722()
    if not data_0722.empty:
        st.dataframe(data_0722, hide_index=True)
    else:
        st.write("No data available.")

def tambah_pasien_0722(id_pasien, nama_pasien, tanggal_lahir, jenis_kelamin, nomor_telpon_pasien, alamat_pasien):
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('INSERT INTO pasien (ID_pasien, nama_pasien, tanggal_lahir, jenis_kelamin, nomor_telpon_pasien, alamat_pasien) VALUES (%s,%s, %s, %s, %s, %s)', 
                       (id_pasien, nama_pasien, tanggal_lahir, jenis_kelamin, nomor_telpon_pasien, alamat_pasien))
        connection_0722.commit()
        cursor_0722.close()
        connection_0722.close()
        st.success(f'Pasien "{nama_pasien}" registered successfully!')

def register_pasien_0722():
    st.header('Register Pasien')
    id_pasien_0722 = st.text_input('ID Pasien')
    nama_pasien_0722 = st.text_input('Nama Pasien')
    tanggal_lahir_0722 = st.date_input('Tanggal Lahir')
    jenis_kelamin_0722 = st.selectbox('Jenis Kelamin', ("Laki-Laki", "Perempuan"))
    nomor_telpon_pasien_0722 = st.text_input('No Telpon')
    alamat_pasien_0722 = st.text_area('Alamat Pasien')

    if st.button('Register Pasien'):
        if id_pasien_0722 and nama_pasien_0722 and tanggal_lahir_0722 and jenis_kelamin_0722 and nomor_telpon_pasien_0722 and alamat_pasien_0722:
            tambah_pasien_0722(id_pasien_0722, nama_pasien_0722, tanggal_lahir_0722, jenis_kelamin_0722, nomor_telpon_pasien_0722, alamat_pasien_0722)
        else:
            st.error('Please fill out all fields.')

def delete_pasien_0722():
    st.header("Hapus Data Pasien")
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT ID_pasien FROM Pasien')
        daftar_pasien = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()

        id_pasien_0722 = st.selectbox("Pilih ID Pasien untuk Dihapus", options=[pasien[0] for pasien in daftar_pasien])

        if st.button("Hapus Pasien"):
            try:
                connection_0722 = get_db_connection()
                if connection_0722:
                    cursor_0722 = connection_0722.cursor()
                    cursor_0722.execute('DELETE FROM Dokter WHERE ID_pasien = %s', (id_pasien_0722,))
                    cursor_0722.execute('DELETE FROM Kamar WHERE ID_pasien = %s', (id_pasien_0722,))
                    cursor_0722.execute('DELETE FROM Pasien WHERE ID_pasien = %s', (id_pasien_0722,))
                    connection_0722.commit()
                    cursor_0722.close()
                    connection_0722.close()
                    st.success("Data pasien berhasil dihapus.")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                if connection_0722.is_connected():
                    cursor_0722.close()
                    connection_0722.close()
    else:
        st.error("Failed to connect to the database")

def edit_pasien_0722():
    st.header("Edit Data Pasien")

    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT ID_pasien, nama_pasien FROM Pasien')
        daftar_pasien = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        daftar_pasien = []

    if daftar_pasien:
        pasien_id_to_edit_0722 = st.selectbox("Pilih ID Pasien Untuk di Edit", options=[pasien[0] for pasien in daftar_pasien])

        connection_0722 = get_db_connection()
        if connection_0722:
            cursor_0722 = connection_0722.cursor()
            cursor_0722.execute('SELECT * FROM Pasien WHERE ID_pasien = %s', (pasien_id_to_edit_0722,))
            pasien_to_edit_0722 = cursor_0722.fetchone()
            cursor_0722.close()
            connection_0722.close()
        else:
            st.error("Failed to connect to the database")
            pasien_to_edit_0722 = None

        if pasien_to_edit_0722:
            st.write("")
            st.write(f"ID Pasien: {pasien_to_edit_0722[0]}")
            st.write(f"Nama Pasien: {pasien_to_edit_0722[1]}")
            st.write(f"Tanggal Lahir: {pasien_to_edit_0722[2]}")
            st.write(f"Jenis Kelamin: {pasien_to_edit_0722[3]}")
            st.write(f"Nomor Telepon: {pasien_to_edit_0722[4]}")
            st.write(f"Alamat: {pasien_to_edit_0722[5]}")
            st.write("---")

            edited_data_0722 = {
                "nama_pasien": st.text_input("Nama Pasien", value=pasien_to_edit_0722[1]),
                "tanggal_lahir": st.date_input("Tanggal Lahir", value=pasien_to_edit_0722[2]),
                "jenis_kelamin": st.selectbox("Jenis Kelamin", options=["Laki-laki", "Perempuan"], index=0 if pasien_to_edit_0722[3] == "Laki-laki" else 1),
                "nomor_telpon_pasien": st.text_input("Nomor Telepon", value=pasien_to_edit_0722[4]),
                "alamat_pasien": st.text_area("Alamat", value=pasien_to_edit_0722[5])
            }

            if st.button("Save"):
                connection_0722 = get_db_connection()
                if connection_0722:
                    cursor_0722 = connection_0722.cursor()
                    cursor_0722.execute('UPDATE Pasien SET nama_pasien = %s, tanggal_lahir = %s, jenis_kelamin = %s, nomor_telpon_pasien = %s, alamat_pasien = %s WHERE ID_pasien = %s', 
                                   (edited_data_0722["nama_pasien"], edited_data_0722["tanggal_lahir"], edited_data_0722["jenis_kelamin"], edited_data_0722["nomor_telpon_pasien"], edited_data_0722["alamat_pasien"], pasien_id_to_edit_0722))
                    connection_0722.commit()
                    cursor_0722.close()
                    connection_0722.close()
                    st.success("Changes saved successfully.")
                else:
                    st.error("Failed to save.")
def search_0722():
    st.header('Search Pasien')
    search_query_0722 = st.text_input('Masukkan Nama Pasien')

    if st.button('Search'):
        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute("SELECT * FROM pasien WHERE nama_pasien LIKE %s", ('%' + search_query_0722 + '%',))
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
    st.header('Filter Pasien Berdasarkan Jenis Kelamin')
    
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute("SELECT DISTINCT jenis_kelamin FROM pasien")
        jenis_kelamin = [row[0] for row in cursor_0722.fetchall()]
        cursor_0722.close()
        conn_0722.close()
    else:
        st.error("Failed to connect to the database")
        jenis_kelamin = []
    
    selected_gender = st.selectbox('Pilih Jenis Kelamin', options=jenis_kelamin)
    
    if st.button('Filter'):
        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute("SELECT * FROM pasien WHERE jenis_kelamin = %s", (selected_gender,))
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
    st.header('Visualisasi Data Pasien Berdasarkan Jenis Kelamin')

    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT jenis_kelamin FROM Pasien')
        jenis_kelamin = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        return
    
    df_0722 = pd.DataFrame(jenis_kelamin, columns=['jenis_kelamin'])

    gender_counts_0722 = df_0722['jenis_kelamin'].value_counts()

    fig, ax = plt.subplots(figsize=(14, 3.5))
    gender_counts_0722.plot(kind='bar', color=['lightgreen', 'pink'], ax=ax)
    ax.set_title('Data Pasien Berdasarkan Jenis Kelamin')
    ax.set_xlabel('Jenis Kelamin')
    ax.set_ylabel('Total')
    ax.set_xticks(range(len(gender_counts_0722)))
    ax.set_xticklabels(gender_counts_0722.index, rotation=0)

    st.pyplot(fig)


selected_0722 = option_menu(
    menu_title=None,
    options=["Pasien", "Register", "Delete", "Edit", "Search", "Filter"],
    icons=["hospital", "person-fill-add", "trash", "pencil", "search", "gender-ambiguous"],
    orientation="horizontal",
)

if selected_0722 == "Pasien":
    display_pasien_0722()
    visualisasi_data_0722()
elif selected_0722 == "Register":
    register_pasien_0722()
elif selected_0722 == "Delete":
    delete_pasien_0722()
elif selected_0722 == "Edit":
    edit_pasien_0722()
elif selected_0722 == "Search":
    search_0722()
elif selected_0722 == "Filter" :
    filter_0722()
