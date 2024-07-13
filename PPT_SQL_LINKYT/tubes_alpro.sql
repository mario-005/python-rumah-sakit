-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Jun 10, 2024 at 03:14 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tubes_alpro`
--

-- --------------------------------------------------------

--
-- Table structure for table `dokter`
--

CREATE TABLE `dokter` (
  `ID_dokter` int(11) NOT NULL,
  `ID_pasien` int(11) DEFAULT NULL,
  `nama_dokter` varchar(100) DEFAULT NULL,
  `spesialisasi` varchar(100) DEFAULT NULL,
  `tanggal_bergabung` date DEFAULT NULL,
  `nomor_telpon` varchar(15) DEFAULT NULL,
  `email_dokter` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dokter`
--

INSERT INTO `dokter` (`ID_dokter`, `ID_pasien`, `nama_dokter`, `spesialisasi`, `tanggal_bergabung`, `nomor_telpon`, `email_dokter`) VALUES
(21, 11, 'Dr. Ahmad', 'Spesialis Anak', '2010-01-01', '081212345678', 'ahmad@gmail.com'),
(22, 12, 'Dr. Budi', 'Spesialis Bedah', '2015-06-01', '081223456789', 'budi@gmail.com'),
(23, 13, 'Dr. Clara', 'Spesialis Kulit', '2018-09-15', '081234567890', 'clara@gmail.com'),
(24, 14, 'Dr. Dedi', 'Spesialis Jantung', '2020-02-20', '081789012345', 'dedi@gmail.com'),
(25, 15, 'Dr. Ellen', 'Spesialis Mata', '2019-07-07', '081890123456', 'ellen@gmail.com'),
(26, 16, 'Dr. Farhan', 'Spesialis Gigi', '2016-03-10', '081998877665', 'farhan@gmail.com'),
(27, 17, 'Dr. Grace', 'Spesialis THT', '2017-11-20', '081887766554', 'grace@gmail.com'),
(28, 18, 'Dr. Helen', 'Spesialis Neurologi', '2021-04-01', '081567890234', 'helen@gmail.com'),
(29, 19, 'Dr. Ismail', 'Spesialis Paru', '2013-02-14', '081678901345', 'ismail@gmail.com'),
(210, 110, 'Dr. Jenny', 'Spesialis Penyakit Dalam', '2014-12-11', '081789012456', 'jenny@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `kamar`
--

CREATE TABLE `kamar` (
  `ID_kamar` int(11) NOT NULL,
  `ID_pasien` int(11) DEFAULT NULL,
  `nama_kamar` varchar(50) DEFAULT NULL,
  `tipe_kamar` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kamar`
--

INSERT INTO `kamar` (`ID_kamar`, `ID_pasien`, `nama_kamar`, `tipe_kamar`) VALUES
(31, 11, 'Kamar 101', 'VIP'),
(32, 12, 'Kamar 102', 'Reguler'),
(33, 13, 'Kamar 103', 'VVIP'),
(34, 14, 'Kamar 104', 'VIP'),
(35, 15, 'Kamar 105', 'Reguler'),
(36, 16, 'Kamar 106', 'VIP'),
(37, 17, 'Kamar 107', 'VVIP'),
(38, 18, 'Kamar 108', 'Reguler'),
(39, 19, 'Kamar 109', 'VIP'),
(310, 110, 'Kamar 110', 'Reguler');

-- --------------------------------------------------------

--
-- Table structure for table `pasien`
--

CREATE TABLE `pasien` (
  `ID_pasien` int(11) NOT NULL,
  `nama_pasien` varchar(100) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(10) DEFAULT NULL,
  `nomor_telpon_pasien` varchar(15) DEFAULT NULL,
  `alamat_pasien` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pasien`
--

INSERT INTO `pasien` (`ID_pasien`, `nama_pasien`, `tanggal_lahir`, `jenis_kelamin`, `nomor_telpon_pasien`, `alamat_pasien`) VALUES
(11, 'Berkah Aryo', '1980-05-15', 'Laki-laki', '081234567890', 'Jl. Merdeka No.1'),
(12, 'Dewi Anggraini', '1990-07-20', 'Perempuan', '081298765432', 'Jl. Kemerdekaan No.2'),
(13, 'putri', '1985-03-22', 'Perempuan', '081345678901', 'Jl. Pancoran No.3'),
(14, 'Alif Fizry', '1978-11-12', 'Laki-laki', '081456789012', 'Jl. Menteng No.4'),
(15, 'Bima Sakti', '1982-04-05', 'Laki-laki', '081567890123', 'Jl. Sukarno No.5'),
(16, 'Mario Laksono', '1995-12-14', 'Laki-laki', '081678901234', 'Jl. Suharto No.6'),
(17, 'Meisya Ayu', '1988-08-08', 'Perempuan', '081789654321', 'Jl. Kebon Jeruk No.7'),
(18, 'Hilmi Putra', '1975-05-15', 'Laki-laki', '081234567891', 'Jl. Melati No.8'),
(19, 'Benediktus Mario', '1981-09-09', 'Laki-laki', '081234567892', 'Jl. Sudirman No.9'),
(110, 'Hafizh Nur', '1992-11-30', 'Laki-laki', '081345678912', 'Jl. Thamrin No.10'),
(111, 'faiz', '2024-06-10', 'Laki-Laki', '089465736', 'bojongsoang');

-- --------------------------------------------------------

--
-- Table structure for table `perawat`
--

CREATE TABLE `perawat` (
  `ID_perawat` int(11) NOT NULL,
  `nama_perawat` varchar(100) DEFAULT NULL,
  `jenis_kelamin` varchar(10) DEFAULT NULL,
  `usia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `perawat`
--

INSERT INTO `perawat` (`ID_perawat`, `nama_perawat`, `jenis_kelamin`, `usia`) VALUES
(41, 'Siti', 'Perempuan', 30),
(42, 'Rini', 'Perempuan', 28),
(43, 'Andi', 'Laki-laki', 32),
(44, 'Faisal', 'Laki-laki', 34),
(45, 'Gina', 'Perempuan', 29),
(46, 'Hilda', 'Perempuan', 26),
(47, 'Irma', 'Perempuan', 35),
(48, 'Joko', 'Laki-laki', 40),
(49, 'Karen', 'Perempuan', 27),
(410, 'Monica', 'Perempuan', 26);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(1, 'benediktus', 'password123', 'admin'),
(2, 'hafidz', 'password456', 'limited');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`ID_dokter`),
  ADD KEY `ID_pasien` (`ID_pasien`);

--
-- Indexes for table `kamar`
--
ALTER TABLE `kamar`
  ADD PRIMARY KEY (`ID_kamar`),
  ADD KEY `ID_pasien` (`ID_pasien`);

--
-- Indexes for table `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`ID_pasien`);

--
-- Indexes for table `perawat`
--
ALTER TABLE `perawat`
  ADD PRIMARY KEY (`ID_perawat`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dokter`
--
ALTER TABLE `dokter`
  ADD CONSTRAINT `dokter_ibfk_1` FOREIGN KEY (`ID_pasien`) REFERENCES `pasien` (`ID_pasien`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `kamar`
--
ALTER TABLE `kamar`
  ADD CONSTRAINT `kamar_ibfk_1` FOREIGN KEY (`ID_pasien`) REFERENCES `pasien` (`ID_pasien`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
