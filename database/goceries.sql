-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2023 at 05:46 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `goceries`
--

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_ID` int(11) NOT NULL,
  `user_ID` int(10) NOT NULL,
  `order_total` int(11) NOT NULL,
  `order_tax` int(11) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `order_delivery_status` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_ID`, `user_ID`, `order_total`, `order_tax`, `order_date`, `order_delivery_status`) VALUES
(1680067271, 1, 23, 2, '2023-03-28 20:44:34', 'Processing Order');

-- --------------------------------------------------------

--
-- Table structure for table `orders_products_details`
--

CREATE TABLE `orders_products_details` (
  `order_product_details_ID` int(11) NOT NULL,
  `order_ID` int(11) NOT NULL,
  `product_ID` int(3) NOT NULL,
  `order_product_totalweight` decimal(10,2) NOT NULL,
  `order_product_totalquantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders_products_details`
--

INSERT INTO `orders_products_details` (`order_product_details_ID`, `order_ID`, `product_ID`, `order_product_totalweight`, `order_product_totalquantity`) VALUES
(1, 1680067271, 402, '9.00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_user_id` int(11) NOT NULL,
  `payment_fname` varchar(255) NOT NULL,
  `payment_lname` varchar(255) NOT NULL,
  `payment_email` varchar(255) NOT NULL,
  `payment_address` varchar(255) NOT NULL,
  `payment_city` varchar(255) NOT NULL,
  `payment_state` varchar(255) NOT NULL,
  `payment_zip` varchar(255) NOT NULL,
  `payment_cardholder` varchar(255) NOT NULL,
  `payment_ccnumber` varchar(255) NOT NULL,
  `payment_expmonth` varchar(255) NOT NULL,
  `payment_expyear` varchar(255) NOT NULL,
  `payment_cvv` varchar(255) NOT NULL,
  `payment_billingname` varchar(255) NOT NULL,
  `payment_billingemail` varchar(255) NOT NULL,
  `payment_billingaddress` varchar(255) NOT NULL,
  `payment_billingcity` varchar(255) NOT NULL,
  `payment_billingstate` varchar(255) NOT NULL,
  `payment_billingzip` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_user_id`, `payment_fname`, `payment_lname`, `payment_email`, `payment_address`, `payment_city`, `payment_state`, `payment_zip`, `payment_cardholder`, `payment_ccnumber`, `payment_expmonth`, `payment_expyear`, `payment_cvv`, `payment_billingname`, `payment_billingemail`, `payment_billingaddress`, `payment_billingcity`, `payment_billingstate`, `payment_billingzip`) VALUES
(1, 'migara', 'liyanage', 'migara1234@gmail.com', 'gfdgrefg', 'ferggreg', 'CA', '32442', 'boc', '4654654564564564', 'April', '2024', '645', 'migara liyanage', 'migara1234@gmail.com', 'gfdgrefg', 'ferggreg', 'CA', '32442');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_ID` int(3) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_category` varchar(45) NOT NULL,
  `product_price` decimal(10,2) NOT NULL,
  `product_weight` decimal(10,2) NOT NULL,
  `product_stock` int(5) NOT NULL,
  `product_description` varchar(2555) NOT NULL,
  `product_imagename` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_ID`, `product_name`, `product_category`, `product_price`, `product_weight`, `product_stock`, `product_description`, `product_imagename`) VALUES
(101, 'Organic Gala Apple', 'fruits', '0.76', '0.35', 200, 'Gala apples are high in fiber, vitamin C, and various antioxidants.', 'fruit-apple.png'),
(102, 'Banana', 'fruits', '0.31', '0.40', 200, 'Bananas contain a fair amount of fiber and several antioxidants.', 'fruit-banana.png'),
(103, 'Blueberries', 'fruits', '3.99', '0.38', 200, 'Blueberries are packed with antioxidants and phytoflavinoids; high in potassium and vitamin C.', 'fruit-blueberry.png'),
(104, 'Cantaloupe', 'fruits', '2.50', '2.00', 200, 'The water, antioxidants, vitamins, and minerals provide a variety of health benefits.', 'fruit-cantaloupe.png'),
(105, 'Peach', 'fruits', '1.81', '0.30', 200, 'Peaches are low in calories, and contain no saturated fats.', 'fruit-peach.png'),
(106, 'Strawberries', 'fruits', '4.50', '1.00', 200, 'They’re an excellent source of vitamin C and manganese and also contain decent amounts of folate and potassium.', 'fruit-strawberry.png'),
(201, 'Asparagus', 'vegetables', '3.01', '1.00', 200, 'Asparagus is low in calories and packed with essential vitamins, minerals and antioxidants.', 'vegetable-asparagus.png'),
(202, 'Green Beans', 'vegetables', '1.99', '1.00', 200, 'Beans provide protein, fiber, folate, iron, potassium and magnesium.', 'vegetable-beans.png'),
(203, 'Cabbage', 'vegetables', '2.28', '2.00', 200, 'Cabbage is a good source of potassium, folate, vitamin K, calcium, iron, vitamin A, and vitamin C.', 'vegetable-cabbage.png'),
(204, 'Carrot', 'vegetables', '0.35', '0.20', 200, 'Carrot is a particularly good source of beta carotene, fiber, vitamin K1, potassium, and antioxidants.', 'vegetable-carrot.png'),
(205, 'Green Bell Pepper', 'vegetables', '0.99', '0.40', 200, 'Peppers are packed with vitamins and low in calories; excellent source of vitamin A, vitamin C, and potassium.', 'vegetable-pepper.png'),
(206, 'Roma Tomato', 'vegetables', '0.37', '0.25', 200, 'Major dietary source of the antioxidant lycopene; great source of vitamin C, potassium, folate, and vitamin K.', 'vegetable-tomato.png'),
(301, 'Creamer', 'Dairy & Eggs', '4.49', '1.50', 200, 'Transform your everyday coffee into something extraordinary.', 'dairy-creamer.png'),
(302, 'Milk', 'Dairy & Eggs', '7.99', '4.20', 200, 'Good source of Vitamin D, Riboflavin, Vitamin B12, Calcium and Phosphorus.', 'dairy-milk.png'),
(303, 'Egg (18 ct)', 'Dairy & Eggs', '8.79', '2.50', 200, 'Eggs contain protein, healthy fats, vitamins A, D, E, choline, iron and folate.', 'dairy-vitalegg.jpg'),
(304, 'Oatmilk', 'Dairy & Eggs', '4.49', '3.00', 200, 'Oat milk is rich in fiber and essential vitamins, such as vitamin A, B12 and D.', 'dairy-oatmilk.png'),
(305, 'Egg (12 ct)', 'Dairy & Eggs', '3.99', '1.30', 200, 'Eggs contain protein, healthy fats, vitamins A, D, E, choline, iron and folate.', 'dairy-eggland.jpg'),
(306, 'Yogurt', 'Dairy & Eggs', '1.00', '0.33', 200, 'Yogurt is an excellent source of protein, calcium and potassium.', 'dairy-yogurt.png'),
(401, 'Apple Juice', 'beverages', '4.29', '3.40', 200, 'Apple juice contains minerals such as calcium, potassium, iron, manganese and magnesium.', 'beverage-applejuice.png'),
(402, 'Berry Seltzer', 'beverages', '20.69', '9.00', 199, '100% All Natural Sparkling Seltzer Water; low sugars; Splash of all-natural fruit flavor.', 'beverage-berryseltzer.png'),
(403, 'Citrus Seltzer', 'beverages', '20.69', '9.00', 200, '100% All Natural Sparkling Seltzer Water; low sugars; Splash of all-natural fruit flavor.', 'beverage-citrusseltzer.png'),
(404, 'Kombucha', 'beverages', '3.19', '1.00', 200, 'Fermented tea plus real, organic & raw ingredients – never concentrates or flavorings', 'beverage-kombucha.png'),
(405, 'Mint Tea', 'beverages', '8.69', '0.50', 200, 'Our tea bags are constructed of Abacá Hemp Fiber Paper. They are free of dyes, adhesive, glue and chlorine bleach.', 'beverage-minttea.png'),
(406, 'Peach Tea', 'beverages', '1.48', '1.06', 200, 'All Honest Tea Organic iced tea beverages are real brewed with Fair Trade Certified tea leaves, gluten Free, OU Kosher certified, and Non GMO.', 'beverage-peachtea.png');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_loginname` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_loginname`, `user_password`, `user_name`, `user_email`) VALUES
(1, 'stan123', '123', 'Stan', 's@gmail.com'),
(2, 'k123', 'abc', 'K', 'k@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_ID`);

--
-- Indexes for table `orders_products_details`
--
ALTER TABLE `orders_products_details`
  ADD PRIMARY KEY (`order_product_details_ID`),
  ADD KEY `FK_orderID` (`order_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders_products_details`
--
ALTER TABLE `orders_products_details`
  MODIFY `order_product_details_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders_products_details`
--
ALTER TABLE `orders_products_details`
  ADD CONSTRAINT `FK_orderID` FOREIGN KEY (`order_ID`) REFERENCES `orders` (`order_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
