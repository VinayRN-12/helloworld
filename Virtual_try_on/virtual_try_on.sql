/*
MySQL Data Transfer
Source Host: localhost
Source Database: virtual_try_on
Target Host: localhost
Target Database: virtual_try_on
Date: 28-04-2025 00:35:24
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for tbladmin
-- ----------------------------
DROP TABLE IF EXISTS `tbladmin`;
CREATE TABLE `tbladmin` (
  `id` bigint(20) NOT NULL auto_increment,
  `added_date` datetime NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) default NULL,
  `name` varchar(100) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `UK_c0r9atamxvbhjjvy5j8da1kam` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for tblcaptcha
-- ----------------------------
DROP TABLE IF EXISTS `tblcaptcha`;
CREATE TABLE `tblcaptcha` (
  `captcha` varchar(100) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for tblcart
-- ----------------------------
DROP TABLE IF EXISTS `tblcart`;
CREATE TABLE `tblcart` (
  `id` bigint(20) NOT NULL auto_increment,
  `discount_price` varchar(200) default NULL,
  `quantity` int(11) NOT NULL,
  `total_price` varchar(200) default NULL,
  `customer_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `mrp_price` varchar(200) default NULL,
  PRIMARY KEY  (`id`),
  KEY `CART_CUST_FK` (`customer_id`),
  KEY `CART_PROD_FK` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for tblcontact
-- ----------------------------
DROP TABLE IF EXISTS `tblcontact`;
CREATE TABLE `tblcontact` (
  `id` bigint(20) NOT NULL auto_increment,
  `contact_date` timestamp NULL default CURRENT_TIMESTAMP,
  `email` varchar(50) NOT NULL,
  `message` varchar(1000) NOT NULL,
  `name` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for tblcustomer
-- ----------------------------
DROP TABLE IF EXISTS `tblcustomer`;
CREATE TABLE `tblcustomer` (
  `id` int(11) default NULL,
  `address` varchar(255) NOT NULL,
  `added_date` timestamp NULL default CURRENT_TIMESTAMP,
  `email` varchar(100) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `phone` varchar(200) default NULL,
  `valid` varchar(50) default NULL,
  `pin_code` varchar(255) NOT NULL,
  UNIQUE KEY `UK_dwk6cx0afu8bs9o4t536v1j5v` (`email`),
  UNIQUE KEY `UK_o3uty20c6csmx5y4uk2tc5r4m` (`phone`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tblorders
-- ----------------------------
DROP TABLE IF EXISTS `tblorders`;
CREATE TABLE `tblorders` (
  `id` int(11) NOT NULL auto_increment,
  `order_no` int(11) default NULL,
  `customer_name` varchar(200) default NULL,
  `mobile_number` varchar(100) default NULL,
  `email_id` varchar(100) default NULL,
  `address` varchar(400) default NULL,
  `address_type` varchar(100) default NULL,
  `pincode` varchar(100) default NULL,
  `image` varchar(200) default NULL,
  `product_name` varchar(400) default NULL,
  `quantity` int(11) default NULL,
  `product_price` varchar(100) default NULL,
  `product_selling_price` varchar(100) default NULL,
  `product_total_price` varchar(100) default NULL,
  `order_status` varchar(100) default NULL,
  `order_date` timestamp NULL default CURRENT_TIMESTAMP,
  `payment_mode` varchar(100) default NULL,
  `payment_id` int(11) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for tblproduct
-- ----------------------------
DROP TABLE IF EXISTS `tblproduct`;
CREATE TABLE `tblproduct` (
  `id` bigint(20) NOT NULL auto_increment,
  `active` varchar(100) default NULL,
  `code` varchar(5) default NULL,
  `create_date` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `description` varchar(255) default NULL,
  `image` varchar(500) default NULL,
  `image_name` varchar(400) default NULL,
  `name` varchar(390) default NULL,
  `price` varchar(200) default NULL,
  `mrp_price` varchar(200) default NULL,
  `product_category` varchar(100) default NULL,
  `blue` int(5) default NULL,
  `green` int(5) default NULL,
  `red` varchar(5) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `UK_h3w5r1mx6d0e5c6um32dgyjej` (`code`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `tbladmin` VALUES ('1', '2023-06-16 00:46:08', 'admin@gmail.com', '123456', 'admin1');
INSERT INTO `tblcaptcha` VALUES ('13915');
INSERT INTO `tblcart` VALUES ('4', '100', '1', '100', '10994', '1', '120');
INSERT INTO `tblcart` VALUES ('9', '349', '1', '349', '10994', '3', '475');
INSERT INTO `tblcontact` VALUES ('5', '2023-06-18 01:14:06', 'sam@gmail.com', 'good', 'sam', 'review');
INSERT INTO `tblcustomer` VALUES ('12618', 'Bhandgaon, Ahmednagar', '2025-02-27 09:32:00', 'sagar@gmail.com', 'Male', 'Sagar', '123456', '8877665566', 'CR5', '414103');
INSERT INTO `tblcustomer` VALUES ('10755', 'Akurdi, Pune', '2025-02-27 09:32:21', 'shashi@gmail.com', 'Male', 'Shashi', '123456', '8822441177', '2UR', '411033');
INSERT INTO `tblcustomer` VALUES ('17279', 'Kharwandi, Newasa,Ahmednagar', '2025-02-27 09:33:02', 'arun@gmail.com', 'Male', 'Arun', '123456', '8800000000', 'WSM', '411055');
INSERT INTO `tblcustomer` VALUES ('14206', 'Kalkup Road, Bhalawani, Ahmednagar', '2025-04-05 18:51:00', 'kadam@gmail.com', 'Male', 'Kadam', '123456', '7700000000', 'IQV', '414103');
INSERT INTO `tblcustomer` VALUES ('12627', 'Gevrai, Beed.', '2025-04-05 18:46:41', 'govind@gmail.com', 'Male', 'Govind', '123456', '6600000000', '11G', '477502');
INSERT INTO `tblcustomer` VALUES ('10994', 'btm bangalore', '2025-04-18 00:29:10', 'sumit@gmail.com', 'Male', 'sumit', '123456', '9886832434', 'QOO', '560078');
INSERT INTO `tblcustomer` VALUES ('16195', 'BTM LAYOUT ', '2025-04-19 11:04:50', 'cosmetics@gmail.com', 'Male', 'cherry', '123456', '5500000000', 'LEF', '560076');
INSERT INTO `tblproduct` VALUES ('2', 'Active', 'JC9', '2023-12-18 18:58:05', '2 piece eye kit for captivating eye looks with an bold eyeliner and kajal, Ophthalmologist tested', 'C:/Users/Lenovo/Documents/2023-24/Eco_sentry/web/uploads/eye.jpg', 'eye.jpg', 'Maybelline New York', '375', '450', 'Eye liner', null, null, null);
INSERT INTO `tblproduct` VALUES ('3', 'Active', 'ATU', '2023-12-18 18:59:39', 'Gives volume to your lashes every day Light and easy to remove, its moisturizer keeps lashes smooth', 'C:/Users/Lenovo/Documents/2023-24/Eco_sentry/web/uploads/lakme.jpg', 'lakme.jpg', 'Lakme Eyeconic Curling Mascara', '349', '475', 'Masacra', null, null, null);
INSERT INTO `tblproduct` VALUES ('4', 'Active', '5AJ', '2023-12-18 19:00:55', 'SUGAR POP VOLUMIZING MASCARA volumizes, lengthens and adds extra definition to your lashes, letting your eyes do all the talking', 'C:/Users/Lenovo/Documents/2023-24/Eco_sentry/web/uploads/suggar.jpg', 'suggar.jpg', 'SUGAR POP Volumizing Mascara', '239', '299', 'Masacra', null, null, null);
INSERT INTO `tblproduct` VALUES ('5', 'Active', '1U3', '2023-12-18 19:02:36', '1) MINIMIZES PORE SIZE 2) EVENS SKIN TONE', 'C:/Users/Lenovo/Documents/2023-24/Eco_sentry/web/uploads/DERMA.jpg', 'DERMA.jpg', 'The Derma ', '526', '599', 'Face Primer', null, null, null);
INSERT INTO `tblproduct` VALUES ('6', 'Active', 'EZZ', '2023-12-18 19:04:11', 'Makes Pores Appear Smaller', 'C:/Users/Lenovo/Documents/2023-24/Eco_sentry/web/uploads/COLOBAR.jpg', 'COLOBAR.jpg', 'Colorbar ', '385', '550', 'Face Primer', null, null, null);
INSERT INTO `tblproduct` VALUES ('8', 'Active', 'YL9', '2023-12-19 14:01:16', 'Color-changing lip gloss - Renee Madness Lip Gloss is formulated in a way that it looks black but slowly changes color according to your lips? pH level, higher the pH level, deeper the color. ', 'C:/Users/Lenovo/Documents/2023-24/Virtual_try_on/web/uploads/LIP GLOSS.jpg', 'LIP GLOSS.jpg', 'RENEE Madness PH Lip Gloss', '399', '550', 'Lip Gloss', null, null, null);
INSERT INTO `tblproduct` VALUES ('9', 'Active', 'NKS', '2024-04-26 08:25:56', 'test lips', 'H:/2024_codes/Virtual_try_on/web/uploads/input2.png', 'input2.png', 'lips_test', '100', '120', 'lips', '120', '209', '78');
INSERT INTO `tblproduct` VALUES ('10', 'Active', '4AE', '2024-04-26 18:25:17', 'dfdsfds', 'H:/2024_codes/Virtual_try_on/web/uploads/pulse.png', 'pulse.png', 'fsffsd', '5555', '7687', 'Hair', '20', '44', '210');
