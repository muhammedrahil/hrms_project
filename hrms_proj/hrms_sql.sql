/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 10.4.24-MariaDB : Database - hrms
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hrms` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `hrms`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add branch',1,'add_branch'),
(2,'Can change branch',1,'change_branch'),
(3,'Can delete branch',1,'delete_branch'),
(4,'Can view branch',1,'view_branch'),
(5,'Can add category',2,'add_category'),
(6,'Can change category',2,'change_category'),
(7,'Can delete category',2,'delete_category'),
(8,'Can view category',2,'view_category'),
(9,'Can add company',3,'add_company'),
(10,'Can change company',3,'change_company'),
(11,'Can delete company',3,'delete_company'),
(12,'Can view company',3,'view_company'),
(13,'Can add employee',4,'add_employee'),
(14,'Can change employee',4,'change_employee'),
(15,'Can delete employee',4,'delete_employee'),
(16,'Can view employee',4,'view_employee'),
(17,'Can add log entry',5,'add_logentry'),
(18,'Can change log entry',5,'change_logentry'),
(19,'Can delete log entry',5,'delete_logentry'),
(20,'Can view log entry',5,'view_logentry'),
(21,'Can add permission',6,'add_permission'),
(22,'Can change permission',6,'change_permission'),
(23,'Can delete permission',6,'delete_permission'),
(24,'Can view permission',6,'view_permission'),
(25,'Can add group',7,'add_group'),
(26,'Can change group',7,'change_group'),
(27,'Can delete group',7,'delete_group'),
(28,'Can view group',7,'view_group'),
(29,'Can add user',8,'add_user'),
(30,'Can change user',8,'change_user'),
(31,'Can delete user',8,'delete_user'),
(32,'Can view user',8,'view_user'),
(33,'Can add content type',9,'add_contenttype'),
(34,'Can change content type',9,'change_contenttype'),
(35,'Can delete content type',9,'delete_contenttype'),
(36,'Can view content type',9,'view_contenttype'),
(37,'Can add session',10,'add_session'),
(38,'Can change session',10,'change_session'),
(39,'Can delete session',10,'delete_session'),
(40,'Can view session',10,'view_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$320000$43lWVhNQqKyiktly8z1qUg$qFLTAq+hpGLkzxLWHTlCsEFwQpq1YGkK6/JJa0hZBaM=','2022-07-16 08:47:05.785510',1,'hrmsproject','','','mrahil7510@gmail.com',1,1,'2022-07-15 11:32:11.126584'),
(2,'pbkdf2_sha256$320000$RUfBJFP1EO1U22a87biAFH$5FSgbE5QbEs6OpSzpa+c07ug6xEKwtks0RPO2FK2ONk=','2022-07-16 08:14:15.559904',0,'admin','','','',0,1,'2022-07-15 11:33:25.000000');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values 
(1,'2022-07-15 11:33:26.166529','2','admin',1,'[{\"added\": {}}]',8,1),
(2,'2022-07-15 11:33:36.430630','2','admin',2,'[]',8,1),
(3,'2022-07-16 08:47:39.955010','10','Employee object (10)',3,'',4,1),
(4,'2022-07-16 08:47:39.969056','9','Employee object (9)',3,'',4,1),
(5,'2022-07-16 08:47:39.970980','8','Employee object (8)',3,'',4,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(5,'admin','logentry'),
(7,'auth','group'),
(6,'auth','permission'),
(8,'auth','user'),
(9,'contenttypes','contenttype'),
(1,'home','branch'),
(2,'home','category'),
(3,'home','company'),
(4,'home','employee'),
(10,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-07-15 11:29:55.971876'),
(2,'auth','0001_initial','2022-07-15 11:29:56.134141'),
(3,'admin','0001_initial','2022-07-15 11:29:56.195641'),
(4,'admin','0002_logentry_remove_auto_add','2022-07-15 11:29:56.205890'),
(5,'admin','0003_logentry_add_action_flag_choices','2022-07-15 11:29:56.220952'),
(6,'contenttypes','0002_remove_content_type_name','2022-07-15 11:29:56.275107'),
(7,'auth','0002_alter_permission_name_max_length','2022-07-15 11:29:56.303619'),
(8,'auth','0003_alter_user_email_max_length','2022-07-15 11:29:56.319219'),
(9,'auth','0004_alter_user_username_opts','2022-07-15 11:29:56.328043'),
(10,'auth','0005_alter_user_last_login_null','2022-07-15 11:29:56.345011'),
(11,'auth','0006_require_contenttypes_0002','2022-07-15 11:29:56.346978'),
(12,'auth','0007_alter_validators_add_error_messages','2022-07-15 11:29:56.355937'),
(13,'auth','0008_alter_user_username_max_length','2022-07-15 11:29:56.368768'),
(14,'auth','0009_alter_user_last_name_max_length','2022-07-15 11:29:56.380650'),
(15,'auth','0010_alter_group_name_max_length','2022-07-15 11:29:56.393073'),
(16,'auth','0011_update_proxy_permissions','2022-07-15 11:29:56.401992'),
(17,'auth','0012_alter_user_first_name_max_length','2022-07-15 11:29:56.415636'),
(18,'home','0001_initial','2022-07-15 11:29:56.542323'),
(19,'sessions','0001_initial','2022-07-15 11:29:56.562011'),
(20,'home','0002_alter_employee_date_alter_employee_user','2022-07-15 11:40:45.926710');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('9b1t6d5c5iz5khr0ryk46b1c8zbgbzzl','.eJxVjEsOwiAUAO_C2hB-j4JL9z0DefykaiAp7cp4d0vShW5nJvMmDvetuL2n1S2RXAknl1_mMTxTHSI-sN4bDa1u6-LpSOhpO51bTK_b2f4NCvYytgoCqKBMFCoqBJAWpNDAQRxKej1pcyBk3vDMfI6T4ZxnZNIqabMhny-fUDYk:1oCYVk:zYv8TiF_ye8uqsP_9gCniuDy8QgF5DPjZeD8o6tiaV8','2022-07-30 03:30:32.984024'),
('bel3sl75yj8gvfn51vhhlddv1pj8g8oj','.eJxVjssOgjAQRf-la9PQx0Bx6d5vaKadqaBIDYWFMf67YFjo9pybk_sSHpe580vhyfckjkKJwy8LGG88boKuOF6yjHmcpz7IbSJ3W-Q5Ew-nffsX6LB0W9ZCBButI23JIoBpwegaFOhVmVA3tVsRVsGpVIVEjVNKJaxMa02b3Brl-2PIT2bP1M_fs_r9AWE2PZE:1oCO26:DSGctFHXzqIl-5Xf20BVcskVEtmifFgG1eaBOi7ObmM','2022-07-29 16:19:14.523390'),
('nwsjovvnnnjdazk98urz9p0z1dav9ngz','.eJxVjEsOwiAUAO_C2hB-j4JL9z0DefykaiAp7cp4d0vShW5nJvMmDvetuL2n1S2RXAknl1_mMTxTHSI-sN4bDa1u6-LpSOhpO51bTK_b2f4NCvYytgoCqKBMFCoqBJAWpNDAQRxKej1pcyBk3vDMfI6T4ZxnZNIqabMhny-fUDYk:1oCdS5:9KJxrPpucBcji49e7jmPfkKRUrVPd4b4Kl3VfzTNzeM','2022-07-30 08:47:05.795153'),
('qtpcefcs2gwranhtzd3tpwd2pfbpamvu','.eJxVjEEOwiAQRe_C2hAoU2Rcuu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERgzj9boHiI9Ud8J3qrcnY6rrMQe6KPGiXU-P0vB7u30GhXr41RrbBuIyDIgSIRtnEChyQzlaHrIzOKZgRkrYAjOg0u3jG6JBMzqN4fwDbpje4:1oCcKS:UkmDWqewCUSlwv2HIVXBTXo7RzFMmHWTauSUhfqbq9o','2022-07-30 07:35:08.064070');

/*Table structure for table `home_branch` */

DROP TABLE IF EXISTS `home_branch`;

CREATE TABLE `home_branch` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `branch` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `home_branch` */

/*Table structure for table `home_category` */

DROP TABLE IF EXISTS `home_category`;

CREATE TABLE `home_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `home_category` */

/*Table structure for table `home_company` */

DROP TABLE IF EXISTS `home_company`;

CREATE TABLE `home_company` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `home_company` */

/*Table structure for table `home_employee` */

DROP TABLE IF EXISTS `home_employee`;

CREATE TABLE `home_employee` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `upload_image` varchar(100) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(254) NOT NULL,
  `emp_id` varchar(30) NOT NULL,
  `uid` varchar(30) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `blood` varchar(20) NOT NULL,
  `mobail_no` int(11) NOT NULL,
  `passport_number` varchar(200) NOT NULL,
  `visa` varchar(255) NOT NULL,
  `emirates` varchar(255) NOT NULL,
  `passport_expiry` date NOT NULL,
  `visa_expiry` date NOT NULL,
  `emirates_expiry` date NOT NULL,
  `insurence` varchar(255) NOT NULL,
  `insurence_expiry` date NOT NULL,
  `insurance_copy` varchar(100) NOT NULL,
  `passport_copy` varchar(100) NOT NULL,
  `visa_copy` varchar(100) NOT NULL,
  `emirates_copy` varchar(100) NOT NULL,
  `other_document` varchar(100) NOT NULL,
  `notification_email` varchar(254) NOT NULL,
  `branch_id` bigint(20) DEFAULT NULL,
  `catogory_id` bigint(20) DEFAULT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `home_employee_branch_id_90516ad1_fk_home_branch_id` (`branch_id`),
  KEY `home_employee_catogory_id_3692c949_fk_home_category_id` (`catogory_id`),
  KEY `home_employee_company_id_abb8ee04_fk_home_company_id` (`company_id`),
  KEY `home_employee_user_id_742a783f` (`user_id`),
  CONSTRAINT `home_employee_branch_id_90516ad1_fk_home_branch_id` FOREIGN KEY (`branch_id`) REFERENCES `home_branch` (`id`),
  CONSTRAINT `home_employee_catogory_id_3692c949_fk_home_category_id` FOREIGN KEY (`catogory_id`) REFERENCES `home_category` (`id`),
  CONSTRAINT `home_employee_company_id_abb8ee04_fk_home_company_id` FOREIGN KEY (`company_id`) REFERENCES `home_company` (`id`),
  CONSTRAINT `home_employee_user_id_742a783f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `home_employee` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
