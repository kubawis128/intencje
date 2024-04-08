-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db1
-- Generation Time: Apr 08, 2024 at 09:27 AM
-- Server version: 10.10.2-MariaDB-1:10.10.2+maria~ubu2204
-- PHP Version: 8.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Pogrzeby`
--

-- --------------------------------------------------------

--
-- Table structure for table `Intencje`
--

CREATE TABLE `Intencje` (
  `id` int(11) NOT NULL,
  `od_kogo` tinytext NOT NULL,
  `kwota` float UNSIGNED NOT NULL,
  `id_pogrzebu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Parafie`
--

CREATE TABLE `Parafie` (
  `id` int(11) NOT NULL,
  `nazwa` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Pogrzeby`
--

CREATE TABLE `Pogrzeby` (
  `id` int(11) NOT NULL,
  `imię` tinytext NOT NULL,
  `nazwisko` tinytext NOT NULL,
  `data` datetime NOT NULL,
  `parafia_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `username` tinytext NOT NULL,
  `password` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Intencje`
--
ALTER TABLE `Intencje`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pogrzebu` (`id_pogrzebu`);

--
-- Indexes for table `Parafie`
--
ALTER TABLE `Parafie`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Pogrzeby`
--
ALTER TABLE `Pogrzeby`
  ADD PRIMARY KEY (`id`),
  ADD KEY `parafia_id` (`parafia_id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Intencje`
--
ALTER TABLE `Intencje`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Parafie`
--
ALTER TABLE `Parafie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Pogrzeby`
--
ALTER TABLE `Pogrzeby`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Intencje`
--
ALTER TABLE `Intencje`
  ADD CONSTRAINT `Intencje_ibfk_1` FOREIGN KEY (`id_pogrzebu`) REFERENCES `Pogrzeby` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `Pogrzeby`
--
ALTER TABLE `Pogrzeby`
  ADD CONSTRAINT `Pogrzeby_ibfk_1` FOREIGN KEY (`parafia_id`) REFERENCES `Parafie` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
