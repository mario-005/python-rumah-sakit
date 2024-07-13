import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from init import get_db_connection
from navigation import sidebar_0722

sidebar_0722()

def dokter_0722():
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('SELECT * FROM dokter')
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [desc[0] for desc in cursor_0722.description]
        data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
        cursor_0722.close()
        conn_0722.close()
        return data_0722
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def add_dokter_0722(ID_dokter, ID_pasien, nama_dokter, spesialisasi, tanggal_bergabung, nomor_telpon, email_dokter):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('INSERT INTO dokter (ID_dokter, ID_pasien, nama_dokter, spesialisasi, tanggal_bergabung, nomor_telpon, email_dokter) VALUES (%s,%s, %s, %s, %s, %s, %s)', (ID_dokter, ID_pasien, nama_dokter, spesialisasi, tanggal_bergabung, nomor_telpon, email_dokter))
        conn_0722.commit()
        cursor_0722.close()
        conn_0722.close()

def login_0722(username, password):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('SELECT username, password FROM users WHERE username = %s AND password = %s', (username, password))
        user_0722 = cursor_0722.fetchone()
        cursor_0722.close()
        conn_0722.close()
        if user_0722:
            return True
        else:
            return False

def search_dokter_0722(name):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        query = "SELECT * FROM dokter WHERE nama_dokter LIKE %s"
        cursor_0722.execute(query, ('%' + name + '%',))
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [col[0] for col in cursor_0722.description]
        data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
        cursor_0722.close()
        conn_0722.close()
        return data_0722
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()

def filter_dokter_0722(year):
    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        query = "SELECT * FROM dokter WHERE YEAR(tanggal_bergabung) >= %s"
        cursor_0722.execute(query, (year,))
        result_0722 = cursor_0722.fetchall()
        columns_0722 = [col[0] for col in cursor_0722.description]
        data_0722 = pd.DataFrame(result_0722, columns=columns_0722)
        cursor_0722.close()
        conn_0722.close()
        return data_0722
    else:
        st.error("Failed to connect to the database")
        return pd.DataFrame()


def data_0722():
    st.header('Data Dokter')
    data_0722 = dokter_0722()
    if not data_0722.empty:
        st.dataframe(data_0722, hide_index=True)
    else:
        st.write("No data available.")

def register_0722():
    st.header('Register Dokter')
    id_dokter_0722 = st.text_input('ID Dokter')
    id_pasien_0722 = st.text_input('ID Pasien')
    nama_dokter_0722 = st.text_input('Nama Dokter')
    spesialisasi_0722 = st.text_input('Spesialisasi')
    tanggal_bergabung_0722 = st.date_input('Tanggal Bergabung')
    nomor_telpon_dokter_0722 = st.text_input('No Telpon')
    email_dokter = st.text_input('Email')
    try:
        id_dokter_0722 = int(id_dokter_0722)
        id_pasien_0722 = int(id_pasien_0722)

        tanggal_bergabung_0722 = tanggal_bergabung_0722.strftime('%Y-%m-%d')

        if st.button('Register Dokter'):
            if id_dokter_0722 and id_pasien_0722 and nama_dokter_0722 and spesialisasi_0722 and tanggal_bergabung_0722 and nomor_telpon_dokter_0722 and email_dokter:
                add_dokter_0722(id_dokter_0722, id_pasien_0722, nama_dokter_0722, spesialisasi_0722, tanggal_bergabung_0722, nomor_telpon_dokter_0722, email_dokter)
                st.success(f'Dokter "{nama_dokter_0722}" registered successfully!')
            else:
                st.error('Please fill in all the fields.')
    except ValueError:
        st.error('ID Dokter and ID Pasien harus berupa angka.')
def delete_0722():
    st.header("Hapus Data Dokter")
    id_dokter_0722 = st.text_input('ID Dokter')

    if st.button("Hapus Dokter"):
        if id_dokter_0722:
            try:
                id_dokter_0722 = int(id_dokter_0722)  # Ensure ID is an integer
                conn_0722 = get_db_connection()
                if conn_0722:
                    cursor_0722 = conn_0722.cursor()
                    cursor_0722.execute('DELETE FROM dokter WHERE ID_dokter = %s', (id_dokter_0722,))
                    conn_0722.commit()
                    cursor_0722.close()
                    conn_0722.close()
                    st.success("Data dokter berhasil dihapus.")
            except ValueError:
                st.error("ID Dokter harus berupa angka.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("ID Dokter tidak boleh kosong.")
def edit_dokter_0722():
    st.header("Edit Data Dokter")

    conn_0722 = get_db_connection()
    if conn_0722:
        cursor_0722 = conn_0722.cursor()
        cursor_0722.execute('SELECT ID_dokter, nama_dokter FROM dokter')
        daftar_dokter_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        conn_0722.close()
    else:
        st.error("Failed to connect to the database")
        daftar_dokter_0722 = []

    if daftar_dokter_0722:
        dokter_id_to_edit_0722 = st.selectbox("Select Doctor to Edit", options=[doktor[0] for doktor in daftar_dokter_0722])

        conn_0722 = get_db_connection()
        if conn_0722:
            cursor_0722 = conn_0722.cursor()
            cursor_0722.execute('SELECT * FROM dokter WHERE ID_dokter = %s', (int(dokter_id_to_edit_0722),))
            dokter_to_edit_0722 = cursor_0722.fetchone()
            cursor_0722.close()
            conn_0722.close()
        else:
            st.error("Failed to connect to the database")
            dokter_to_edit_0722 = None

        if dokter_to_edit_0722:
            st.write("")
            st.write(f"ID Dokter: {dokter_to_edit_0722[0]}")
            st.write(f"ID Pasien: {dokter_to_edit_0722[1]}")
            st.write(f"Nama Dokter: {dokter_to_edit_0722[2]}")
            st.write(f"Spesialisasi: {dokter_to_edit_0722[3]}")
            st.write(f"Tanggal Bergabung: {dokter_to_edit_0722[4]}")
            st.write(f"Nomor Telepon: {dokter_to_edit_0722[5]}")
            st.write(f"Alamat Email: {dokter_to_edit_0722[6]}")
            st.write("---")

            edited_data_0722 = {
                "id_pasien": st.text_input("ID Pasien", value=dokter_to_edit_0722[1]),
                "nama_dokter": st.text_input("Nama Dokter", value=dokter_to_edit_0722[2]),
                "spesialisasi": st.text_input("Spesialisasi", value=dokter_to_edit_0722[3]),
                "tanggal_bergabung": st.date_input("Tanggal Bergabung", value=dokter_to_edit_0722[4]),
                "nomor_telpon": st.text_input("Nomor Telepon", value=dokter_to_edit_0722[5]),
                "email_dokter": st.text_input("Email", value=dokter_to_edit_0722[6])
            }

            if st.button("Save Changes"):
                conn_0722 = get_db_connection()
                if conn_0722:
                    cursor_0722 = conn_0722.cursor()
                    cursor_0722.execute('UPDATE dokter SET id_pasien = %s, nama_dokter = %s, spesialisasi = %s, tanggal_bergabung = %s, nomor_telpon = %s, email_dokter = %s WHERE ID_dokter = %s', 
                                        (edited_data_0722["id_pasien"], edited_data_0722["nama_dokter"], edited_data_0722["spesialisasi"], edited_data_0722["tanggal_bergabung"], edited_data_0722["nomor_telpon"], edited_data_0722["email_dokter"], int(dokter_id_to_edit_0722)))
                    conn_0722.commit()
                    cursor_0722.close()
                    conn_0722.close()
                    st.success("Changes saved successfully.")
                else:
                    st.error("Failed to save changes.")
def search_0722():
    st.header("Search Dokter")
    search_query = st.text_input("Masukkan Nama Dokter")
    
    if st.button("Search"):
        data_0722 = search_dokter_0722(search_query)
        if not data_0722.empty:
            st.dataframe(data_0722, hide_index=True)
        else:
            st.write("Tidak Menemukaan Data.")
def filter_0722():
    st.header("Filter Dokter Berdasarkan Tahun Bergabung")
    year = st.number_input('Masukkan Tahun Bergabung', max_value=2100, step=1)
    
    if st.button("Filter"):
        data_0722 = filter_dokter_0722(year)
        if not data_0722.empty:
            st.dataframe(data_0722, hide_index=True)
        else:
            st.write("Tidak Menemukaan Data.")

def visualisasi_data_0722():
    st.header('Visualisasi Data Dokter Berdasarkan Tahun Bergabung')

    # Fetch data
    connection_0722 = get_db_connection()
    if connection_0722:
        cursor_0722 = connection_0722.cursor()
        cursor_0722.execute('SELECT tanggal_bergabung FROM Dokter')
        tanggal_bergabung_0722 = cursor_0722.fetchall()
        cursor_0722.close()
        connection_0722.close()
    else:
        st.error("Failed to connect to the database")
        return
    
    df_0722 = pd.DataFrame(tanggal_bergabung_0722, columns=['tanggal_bergabung'])
    bins_0722 = pd.to_datetime(['2010-01-01', '2015-12-31', '2020-12-31', '2025-12-31'])
    labels_0722 = ['2010-2015', '2016-2020', '2021-2025']
    
    df_0722['range'] = pd.cut(pd.to_datetime(df_0722['tanggal_bergabung']), bins=bins_0722, labels=labels_0722, right=False)


    range_counts_0722 = df_0722['range'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(14, 3.5))
    range_counts_0722.plot(kind='bar', color=['blue', 'green', 'orange'], ax=ax)
    ax.set_title('Jumlah Dokter Berdasarkan Tahun Bergabung')
    ax.set_xlabel('Tahun Bergabung')
    ax.set_ylabel('Jumlah')
    ax.set_xticks(range(len(range_counts_0722)))
    ax.set_xticklabels(range_counts_0722.index, rotation=0)

    st.pyplot(fig)

selected_0722 = option_menu(
    menu_title=None,
    options=["Dokter", "Register", "Delete", "Edit", "Search", "Filter"],
    icons=["hospital", "person-fill-add", "trash", "pencil", "search", "calendar"],
    orientation="horizontal",
)

if selected_0722 == "Dokter":
    data_0722()
    visualisasi_data_0722()
if selected_0722 == "Register":
    register_0722()    
if selected_0722 == "Delete":
    delete_0722()
if selected_0722 == "Edit":
    edit_dokter_0722()    
if selected_0722 == "Search":
    search_0722()
if selected_0722 == "Filter":
    filter_0722()    
