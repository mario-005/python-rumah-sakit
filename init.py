# Kelas: SI-47-07
# Kelompok: 22
# Anggota Kelompok:
# 1. Hafidz Nur Hilmi (102022330288)
# 2. Berkah Aryo Bima Sakti (102022300237)
# 3. Muhammad Fizry Alifta (102022300222)
# 4. Benediktus Mario Laksono (102022300270)
# 5. Faiz Dhya Muhammad Rahmantyo (102022300144)

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  
        database='tubes_alpro',
        port=3306
    )
    if connection.is_connected():
        return connection
    else:
        print("Failed to connect to the database")
        return None

def create_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            ''')
          
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pasien (
                    ID_pasien INT PRIMARY KEY,
                    nama_pasien VARCHAR(100),
                    tanggal_lahir DATE,
                    jenis_kelamin VARCHAR(10),
                    nomor_telpon_pasien VARCHAR(15),
                    alamat_pasien TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Dokter (
                    ID_dokter INT PRIMARY KEY,
                    ID_pasien INT,
                    nama_dokter VARCHAR(100),
                    spesialisasi VARCHAR(100),
                    tanggal_bergabung DATE,
                    nomor_telpon VARCHAR(15),
                    email_dokter VARCHAR(100),
                    FOREIGN KEY (ID_pasien) REFERENCES Pasien(ID_pasien) ON DELETE CASCADE ON UPDATE CASCADE

                    
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Kamar (
                    ID_kamar INT PRIMARY KEY,
                    ID_pasien INT,
                    nama_kamar VARCHAR(50),
                    tipe_kamar VARCHAR(50),
                    FOREIGN KEY (ID_pasien) REFERENCES Pasien(ID_pasien) ON DELETE CASCADE ON UPDATE CASCADE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Perawat (
                   ID_perawat INT PRIMARY KEY,
                   nama_perawat VARCHAR(100),
                   jenis_kelamin VARCHAR(10),
                   usia INT
                )
            ''')

            cursor.execute('''
                INSERT IGNORE INTO users (username, password, role) VALUES
                    ('benediktus', 'password123', 'admin'),
                    ('hafidz', 'password456', 'limited')
            ''')
            
            cursor.execute('''
                INSERT IGNORE INTO Pasien (ID_pasien, nama_pasien, tanggal_lahir, jenis_kelamin, 	nomor_telpon_pasien, alamat_pasien) VALUES
	                (11, 'Berkah Aryo', '1980-05-15', 'Laki-laki', '081234567890', 'Jl. Merdeka No.1'),
                    (12, 'Dewi Anggraini', '1990-07-20', 'Perempuan', '081298765432', 'Jl. Kemerdekaan No.2'),
                    (13, 'Indah Putri', '1985-03-22', 'Perempuan', '081345678901', 'Jl. Pancoran No.3'),
                    (14, 'Alif Fizry', '1978-11-12', 'Laki-laki', '081456789012', 'Jl. Menteng No.4'),
                    (15, 'Bima Sakti', '1982-04-05', 'Laki-laki', '081567890123', 'Jl. Sukarno No.5'),
                    (16, 'Mario Laksono', '1995-12-14', 'Laki-laki', '081678901234', 'Jl. Suharto No.6'),
                    (17, 'Meisya Ayu', '1988-08-08', 'Perempuan', '081789654321', 'Jl. Kebon Jeruk No.7'),
                    (18, 'Hilmi Putra', '1975-05-15', 'Laki-laki', '081234567891', 'Jl. Melati No.8'),
                    (19, 'Benediktus Mario', '1981-09-09', 'Laki-laki', '081234567892', 'Jl. Sudirman No.9'),
                    (110, 'Hafizh Nur', '1992-11-30', 'Laki-laki', '081345678912', 'Jl. Thamrin No.10')
            ''')
            cursor.execute('''
                INSERT IGNORE INTO Dokter (ID_Dokter, ID_Pasien, Nama_dokter, Spesialisasi, tanggal_bergabung, nomor_telpon, Email_dokter) VALUES
                    (21, 11, 'Dr. Ahmad', 'Spesialis Anak', '2010-01-01', '081212345678', 'ahmad@gmail.com'),
                    (22, 12, 'Dr. Budi', 'Spesialis Bedah', '2015-06-01', '081223456789', 'budi@gmail.com'),
                    (23, 13, 'Dr. Clara', 'Spesialis Kulit', '2018-09-15', '081234567890', 'clara@gmail.com'),
                    (24, 14, 'Dr. Dedi', 'Spesialis Jantung', '2020-02-20', '081789012345', 'dedi@gmail.com'),
                    (25, 15, 'Dr. Ellen', 'Spesialis Mata', '2019-07-07', '081890123456', 'ellen@gmail.com'),
                    (26, 16, 'Dr. Farhan', 'Spesialis Gigi', '2016-03-10', '081998877665', 'farhan@gmail.com'),
                    (27, 17, 'Dr. Grace', 'Spesialis THT', '2017-11-20', '081887766554', 'grace@gmail.com'),
                    (28, 18, 'Dr. Helen', 'Spesialis Neurologi', '2021-04-01', '081567890234', 'helen@gmail.com'),
                    (29, 19, 'Dr. Ismail', 'Spesialis Paru', '2013-02-14', '081678901345', 'ismail@gmail.com'),
                    (210, 110, 'Dr. Jenny', 'Spesialis Penyakit Dalam', '2014-12-11', '081789012456', 	'jenny@gmail.com')
            ''') 
            cursor.execute('''
                INSERT IGNORE INTO Kamar (ID_kamar, ID_pasien, nama_kamar, tipe_kamar) VALUES
                    (31, 11, 'Kamar 101', 'VIP'),
                    (32, 12, 'Kamar 102', 'Reguler'),
                    (33, 13, 'Kamar 103', 'VVIP'),
                    (34, 14, 'Kamar 104', 'VIP'),
                    (35, 15, 'Kamar 105', 'Reguler'),
                    (36, 16, 'Kamar 106', 'VIP'),
                    (37, 17, 'Kamar 107', 'VVIP'),
                    (38, 18, 'Kamar 108', 'Reguler'),
                    (39, 19, 'Kamar 109', 'VIP'),
                    (310, 110, 'Kamar 110', 'Reguler')
            ''') 
            cursor.execute('''
                INSERT IGNORE INTO Perawat (ID_Perawat, Nama_perawat, Jenis_kelamin, Usia) VALUES
                    (41, 'Siti', 'Perempuan', 30),
                    (42, 'Rini', 'Perempuan', 28),
                    (43, 'Andi', 'Laki-laki', 32),
                    (44, 'Faisal', 'Laki-laki', 34),
                    (45, 'Gina', 'Perempuan', 29),
                    (46, 'Hilda', 'Perempuan', 26),
                    (47, 'Irma', 'Perempuan', 35),
                    (48, 'Joko', 'Laki-laki', 40),
                    (49, 'Karen', 'Perempuan', 27),
                    (410, 'Monica', 'Perempuan', 26)
            ''')

            connection.commit()
            cursor.close()
            connection.close()
            print("Table created successfully.")
        except mysql.connector.Error as e:
            print("Error creating table:", e)
            if connection.is_connected():
                connection.rollback()
                connection.close()

create_table()
