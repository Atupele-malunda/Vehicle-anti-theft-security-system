-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2023 at 12:05 PM
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
-- Database: `details`
--

-- --------------------------------------------------------

--
-- Table structure for table `add`
--

CREATE TABLE `add` (
  `var` int(11) NOT NULL,
  `tr` int(11) NOT NULL,
  `kr` int(11) NOT NULL,
  `til` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `id` int(11) NOT NULL,
  `Licence plate` varchar(20) NOT NULL,
  `Owner` int(20) NOT NULL,
  `Color` varchar(20) NOT NULL,
  `Make` varchar(20) NOT NULL,
  `Model` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`id`, `Licence plate`, `Owner`, `Color`, `Make`, `Model`) VALUES
(1, 'MH20DY2363', 1, 'Maroon', 'Benz', 'C200');

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `Occupation` varchar(100) NOT NULL,
  `Religion` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Marital status` varchar(100) NOT NULL,
  `Person Id` varchar(100) NOT NULL,
  `Firstname` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `Home address` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone no` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`Occupation`, `Religion`, `Gender`, `Marital status`, `Person Id`, `Firstname`, `Surname`, `Home address`, `Email`, `Phone no`, `photo`) VALUES
('Programmer', 'Muslim', 'Male', 'Single', 'M', 'CNCM', 'MXMXM', 'MMMM', 'hsj@gmail.com', 'MXMX', 'NO');

-- --------------------------------------------------------

--
-- Table structure for table `intel`
--

CREATE TABLE `intel` (
  `id` int(11) NOT NULL,
  `Gender` varchar(100) DEFAULT NULL,
  `FirstName` varchar(100) DEFAULT NULL,
  `LastName` varchar(100) DEFAULT NULL,
  `Nationality` varchar(100) DEFAULT NULL,
  `Occupation` varchar(100) DEFAULT NULL,
  `HomeAddress` varchar(100) DEFAULT NULL,
  `PhoneNo` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Photo` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `intel`
--

INSERT INTO `intel` (`id`, `Gender`, `FirstName`, `LastName`, `Nationality`, `Occupation`, `HomeAddress`, `PhoneNo`, `Email`, `Photo`) VALUES
(1, 'Male', 'Atupele', 'Malunda', 'Malawian', 'Programmer', 'Blantyre', '0999096620', 'atupelemalunda@gmail.com', ''),
(2, 'Male', 'kenny', 'kwitonda', 'rwandies', 'area25', 'networkadminstrator', '997575865', 'kennykwitonda@gmial.com', ''),
(3, 'Male', 'tingo', 'chilopa', 'malawian', 'mangochi', 'programmer', '9998765544', 'ti@gmail.com', ''),
(4, 'Male', 'Musaa', 'Bakili', 'MAlawian', 'Teacher', 'MAngochi', '9998755454', 'musa@gmail.com', ''),
(5, 'Male', 'Mwayi', 'Banda', 'Malawian', 'NetworkEngineer', 'mzuzu', '9998766554', 'mwayi@gmail.com', '');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `name`, `Email`, `Address`) VALUES
(1, 'MacDonald Maigwa', 'mmaigwa@jedsy.com', 'Area 25');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `securityQ` varchar(100) NOT NULL,
  `securityA` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `pass`) VALUES
('Atupele', 'Malunda', '0999096620', 'atupelemalunda@gmail.com', 'Your Dad\'s Name', 'Henry', 'admin@1234'),
('kenny', 'kwitonda', '0999765423', 'keenny@gmail.com', 'Your Mom\'s name', 'Mary', 'kenny@1234'),
('Mwayi', 'Banda', '088776532', 'mwayi@gmail.com', 'Your Mom\'s name', 'emily', 'mwayi@123'),
('Ralez', 'gowo', '988844883', 'goowo@gmail.com', 'Your Mom\'s name', 'jane', 'gowo@444');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Owner` (`Owner`);

--
-- Indexes for table `intel`
--
ALTER TABLE `intel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `intel`
--
ALTER TABLE `intel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `car_ibfk_1` FOREIGN KEY (`Owner`) REFERENCES `profile` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
