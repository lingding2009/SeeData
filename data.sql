/*
 Navicat Premium Data Transfer

 Source Server         : data
 Source Server Type    : MySQL
 Source Server Version : 80034
 Source Host           : localhost:3306
 Source Schema         : data

 Target Server Type    : MySQL
 Target Server Version : 80034
 File Encoding         : 65001

 Date: 30/08/2023 11:27:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for case
-- ----------------------------
DROP TABLE IF EXISTS `case`;
CREATE TABLE `case`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `price` decimal(10, 2) NULL DEFAULT NULL COMMENT 'Loss Price',
  `sex` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `job` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Occupation',
  `case_type` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Case Type',
  `case_area` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Case Nature',
  `content` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL COMMENT 'Case Process',
  `rep_time` datetime NULL DEFAULT NULL COMMENT 'Report Time',
  `is_end` int NULL DEFAULT NULL COMMENT 'Is the case closed? (1 means closed)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 671 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of case
-- ----------------------------
INSERT INTO `case` VALUES (1, 1689.00, 'F', 19, 'unemployed', 'Loss of goods', 'Burglary', '', '2023-08-03 00:05:46', 1);
INSERT INTO `case` VALUES (2, 1500.00, 'M', 31, 'unemployed', 'Loss of goods', 'looting', '', '2023-08-06 20:49:23', 0);
INSERT INTO `case` VALUES (3, 11000.00, 'M', 22, 'Enterprise employee', 'Violent crime', 'Hate crime', '', '2023-08-08 20:05:52', 1);
INSERT INTO `case` VALUES (4, 10000.00, 'F', 35, 'individual', 'Violent crime', '\nDomestic abuse', '', '2023-08-21 09:39:42', 1);
INSERT INTO `case` VALUES (5, 8000.00, 'M', 13, 'student', 'Cybercrimer', 'Public endangerment', '', '2023-08-23 23:30:17', 0);
INSERT INTO `case` VALUES (6, 8904.00, 'M', 36, 'individual', 'Cybercrimer', 'Public endangerment', '', '2023-08-05 03:07:37', 1);
INSERT INTO `case` VALUES (7, 690.00, 'M', 45, 'unemployed', 'Cybercrimer ', 'Hate crime', '', '2023-08-09 05:11:11', 0);
INSERT INTO `case` VALUES (8, 1400.00, 'M', 23, 'Enterprise employee', 'Fraud', 'SMS fraud', '', '2023-08-05 12:37:55', 1);
INSERT INTO `case` VALUES (9, 20000.00, 'M', 44, 'unemployed', 'Cybercrimer', 'Public endangerment', '', '2023-08-05 14:35:33', 1);
INSERT INTO `case` VALUES (10, 10000.00, 'F', 31, 'teacher', 'Fraud', 'Impersonate', 'aaa', '2023-08-22 04:30:15', 1);
INSERT INTO `case` VALUES (659, 13001.00, 'F', 29, 'student', 'Loss of goods', 'SMS fraud', '', '2023-08-08 02:36:32', 0);
INSERT INTO `case` VALUES (660, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-27 02:37:39', 0);
INSERT INTO `case` VALUES (661, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-10 19:01:47', 0);
INSERT INTO `case` VALUES (662, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-22 08:05:17', 0);
INSERT INTO `case` VALUES (664, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-17 02:25:54', 0);
INSERT INTO `case` VALUES (665, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-12 22:32:15', 0);
INSERT INTO `case` VALUES (666, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-01 20:29:18', 0);
INSERT INTO `case` VALUES (667, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-04 00:21:40', 0);
INSERT INTO `case` VALUES (668, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-04 22:31:21', 0);
INSERT INTO `case` VALUES (669, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-07-31 12:31:32', 0);
INSERT INTO `case` VALUES (670, 13001.00, 'F', 34, 'student', 'Loss of goods', 'Burglary', '', '2023-08-18 07:42:50', 0);

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES (12, 'Burglary');
INSERT INTO `category` VALUES (13, 'Hate crime');
INSERT INTO `category` VALUES (14, 'looting');
INSERT INTO `category` VALUES (15, 'Loss of goods');
INSERT INTO `category` VALUES (16, 'SMS fraud');
INSERT INTO `category` VALUES (17, ' Domestic abuse');
INSERT INTO `category` VALUES (18, 'ImpersonateImpersonate');

-- ----------------------------
-- Table structure for notice
-- ----------------------------
DROP TABLE IF EXISTS `notice`;
CREATE TABLE `notice`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Announcement',
  `title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Announcement Title',
  `content` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Announcement Content',
  `user_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Publisher',
  `create_time` datetime NULL DEFAULT NULL COMMENT 'Publication Time',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of notice
-- ----------------------------
INSERT INTO `notice` VALUES (9, 'Excel Form', 'Amonunt involved |  Gender |  age  |  job | Scope |  Type | Case Name | Time | Completion', 'Ding LI', '2023-08-15 22:54:28');

-- ----------------------------
-- Table structure for sys_version
-- ----------------------------
DROP TABLE IF EXISTS `sys_version`;
CREATE TABLE `sys_version`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'version',
  `sys_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'name',
  `sys_version` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'descriptive',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of sys_version
-- ----------------------------
INSERT INTO `sys_version` VALUES (1, 'Scope', 'Ex : Loss of goods');
INSERT INTO `sys_version` VALUES (2, 'job', 'Ex : student');
INSERT INTO `sys_version` VALUES (3, 'age ', 'Ex : 20');
INSERT INTO `sys_version` VALUES (5, 'gender', 'Ex : M/F   (male or female)');
INSERT INTO `sys_version` VALUES (6, 'Amonunt involved ', 'Ex : 1200');
INSERT INTO `sys_version` VALUES (7, 'Type', 'Ex : Burglary');
INSERT INTO `sys_version` VALUES (8, 'case ', 'Ex : get Burglary by a theif');
INSERT INTO `sys_version` VALUES (9, 'Time', 'Ex : 2023/07/21 04:24:19');
INSERT INTO `sys_version` VALUES (10, 'Completion', 'Ex : 0 for incomplete, 1 for complete');

-- ----------------------------
-- Table structure for type
-- ----------------------------
DROP TABLE IF EXISTS `type`;
CREATE TABLE `type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of type
-- ----------------------------
INSERT INTO `type` VALUES (1, 'Fraud');
INSERT INTO `type` VALUES (2, 'Cybercrimer');
INSERT INTO `type` VALUES (3, 'Loss of goods');
INSERT INTO `type` VALUES (9, 'Violent crime');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT ' ',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'User Name (Supplier Name)',
  `account` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'User Account',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'User Password',
  `company` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Company Name',
  `phone` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Phone Number',
  `mail` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Email',
  `type` int NULL DEFAULT NULL COMMENT '0 for Admin, 1 for Regular User',
  `status` int NULL DEFAULT NULL COMMENT '0 for Disabled, 1 for Enabled',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'administrator', 'admin', '123456', 'University of Glasgow', '18866666666', '123456789@gmail.com', 0, 1);
INSERT INTO `user` VALUES (9, 'qqq', 'qqq', 'qqq', 'University of Glasgow', '13736432855', 'xxxx@gmail.com', 1, 1);

SET FOREIGN_KEY_CHECKS = 1;
