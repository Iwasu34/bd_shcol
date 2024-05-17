-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 16, 2024 at 06:24 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `librarydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` bigint(20) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `Genre` varchar(50) NOT NULL,
  `Year` year(4) NOT NULL,
  `Pages` bigint(20) NOT NULL,
  `Description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `Title`, `Author`, `Genre`, `Year`, `Pages`, `Description`) VALUES
(2, 'Гарри', 'Джоан Роулинг', 'Фентази', 2019, 544, 'Гарри Поттер снова проводит лето в доме Дурслей. Третьекурсники в Хогвартсе могут посещать деревню магов Хогсмид'),
(3, 'Гарри', 'Джоан Роулинг', 'Фентази', 2019, 544, 'Гарри Поттер снова проводит лето в доме Дурслей. Третьекурсники в Хогвартсе могут посещать деревню магов Хогсмид'),
(4, 'вфывфыв', 'фывфы', 'фыв', 2022, 544, 'йцвфывцвфычямсчямуцфк');

-- --------------------------------------------------------

--
-- Table structure for table `fines`
--

CREATE TABLE `fines` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `LoanId` bigint(20) NOT NULL,
  `Amount` bigint(20) NOT NULL,
  `Paid` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `librarians`
--

CREATE TABLE `librarians` (
  `id` bigint(20) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `Lastname` varchar(20) NOT NULL,
  `Position` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `librarians`
--

INSERT INTO `librarians` (`id`, `FirstName`, `Lastname`, `Position`) VALUES
(1, 'Юлия', 'Иванова', 'Младший библиотекарь');

-- --------------------------------------------------------

--
-- Table structure for table `loans`
--

CREATE TABLE `loans` (
  `id` bigint(20) NOT NULL,
  `StudentId` bigint(20) NOT NULL,
  `BookId` bigint(20) NOT NULL,
  `LibrariansId` bigint(20) NOT NULL,
  `DateOut` date NOT NULL,
  `DateDue` date NOT NULL,
  `Returned` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `loans`
--

INSERT INTO `loans` (`id`, `StudentId`, `BookId`, `LibrariansId`, `DateOut`, `DateDue`, `Returned`) VALUES
(1, 1, 2, 1, '2024-05-12', '2024-05-22', 1),
(2, 5, 2, 1, '2024-05-12', '2024-05-22', 1),
(3, 5, 2, 1, '2024-05-12', '2024-05-22', 0);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Id` bigint(20) NOT NULL,
  `FirstName` varchar(20) DEFAULT NULL,
  `LastName` varchar(20) DEFAULT NULL,
  `Class` int(10) UNSIGNED NOT NULL,
  `Grade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Id`, `FirstName`, `LastName`, `Class`, `Grade`) VALUES
(1, 'dsad', 'dasdas', 1, 100),
(2, 'sadas', 'asds', 1, 100),
(3, 'asdsd', 'sdsds', 1, 100),
(4, 'dsad', 'asds', 3, 100),
(5, 'dsas', 'dsds', 4, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fines`
--
ALTER TABLE `fines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `librarians`
--
ALTER TABLE `librarians`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loans`
--
ALTER TABLE `loans`
  ADD PRIMARY KEY (`id`),
  ADD KEY `BookId` (`BookId`),
  ADD KEY `LibrariansId` (`LibrariansId`),
  ADD KEY `StudentId` (`StudentId`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `fines`
--
ALTER TABLE `fines`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `librarians`
--
ALTER TABLE `librarians`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `loans`
--
ALTER TABLE `loans`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `loans`
--
ALTER TABLE `loans`
  ADD CONSTRAINT `loans_ibfk_1` FOREIGN KEY (`BookId`) REFERENCES `books` (`id`),
  ADD CONSTRAINT `loans_ibfk_2` FOREIGN KEY (`LibrariansId`) REFERENCES `librarians` (`id`),
  ADD CONSTRAINT `loans_ibfk_3` FOREIGN KEY (`StudentId`) REFERENCES `students` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
