-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: sosangspace-db.cz7mxx5dglpt.ap-northeast-2.rds.amazonaws.com    Database: sosangspace
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add photo',7,'add_photo'),(26,'Can change photo',7,'change_photo'),(27,'Can delete photo',7,'delete_photo'),(28,'Can view photo',7,'view_photo'),(29,'Can add item',8,'add_item'),(30,'Can change item',8,'change_item'),(31,'Can delete item',8,'delete_item'),(32,'Can view item',8,'view_item'),(33,'Can add wishlist',9,'add_wishlist'),(34,'Can change wishlist',9,'change_wishlist'),(35,'Can delete wishlist',9,'delete_wishlist'),(36,'Can view wishlist',9,'view_wishlist'),(37,'Can add task result',10,'add_taskresult'),(38,'Can change task result',10,'change_taskresult'),(39,'Can delete task result',10,'delete_taskresult'),(40,'Can view task result',10,'view_taskresult'),(41,'Can add chord counter',11,'add_chordcounter'),(42,'Can change chord counter',11,'change_chordcounter'),(43,'Can delete chord counter',11,'delete_chordcounter'),(44,'Can view chord counter',11,'view_chordcounter'),(45,'Can add group result',12,'add_groupresult'),(46,'Can change group result',12,'change_groupresult'),(47,'Can delete group result',12,'delete_groupresult'),(48,'Can view group result',12,'view_groupresult'),(49,'Can add item stats daily',13,'add_itemstatsdaily'),(50,'Can change item stats daily',13,'change_itemstatsdaily'),(51,'Can delete item stats daily',13,'delete_itemstatsdaily'),(52,'Can view item stats daily',13,'view_itemstatsdaily'),(53,'Can add search category',14,'add_searchcategory'),(54,'Can change search category',14,'change_searchcategory'),(55,'Can delete search category',14,'delete_searchcategory'),(56,'Can view search category',14,'view_searchcategory'),(57,'Can add search stats',15,'add_searchstats'),(58,'Can change search stats',15,'change_searchstats'),(59,'Can delete search stats',15,'delete_searchstats'),(60,'Can view search stats',15,'view_searchstats'),(61,'Can add search used years',16,'add_searchusedyears'),(62,'Can change search used years',16,'change_searchusedyears'),(63,'Can delete search used years',16,'delete_searchusedyears'),(64,'Can view search used years',16,'view_searchusedyears'),(65,'Can add search location',17,'add_searchlocation'),(66,'Can change search location',17,'change_searchlocation'),(67,'Can delete search location',17,'delete_searchlocation'),(68,'Can view search location',17,'view_searchlocation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$MTApvCOUtrYHn1gxwrWPdJ$XGW70mMlFDf6SSAP8nCs+itMVXM7/xOx+9yzMv5T6P0=','2023-08-16 04:11:55.127154',1,'woohoocheezy','','','',1,1,'2023-07-05 00:17:41.233374');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-07-05 00:20:44.000345','1','Photo object (1)',2,'[]',7,1),(2,'2023-07-05 00:21:05.304486','1','Photo object (1)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(3,'2023-07-05 00:23:10.446964','1','Photo object (1)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(4,'2023-07-05 00:24:05.267651','2','Photo object (2)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(5,'2023-07-05 00:24:35.805965','3','Photo object (3)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(6,'2023-07-05 00:25:27.783294','4','Photo object (4)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(7,'2023-07-05 00:26:54.071675','7','Photo object (7)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(8,'2023-07-05 00:27:25.027660','8','Photo object (8)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(9,'2023-07-05 00:28:13.384948','9','Photo object (9)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(10,'2023-07-05 00:29:31.594518','12','Photo object (12)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(11,'2023-07-05 00:29:47.588425','13','Photo object (13)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(12,'2023-07-05 00:30:03.897331','14','Photo object (14)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(13,'2023-07-05 01:12:30.350896','1','Item object (1)',2,'[{\"changed\": {\"fields\": [\"Description\", \"Location\"]}}]',8,1),(14,'2023-07-05 01:12:38.697041','2','Item object (2)',2,'[{\"changed\": {\"fields\": [\"Description\", \"Location\"]}}]',8,1),(15,'2023-07-05 01:12:50.208272','3','Item object (3)',2,'[{\"changed\": {\"fields\": [\"Description\", \"Location\"]}}]',8,1),(16,'2023-07-05 02:05:40.465233','4','Photo object (4)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(17,'2023-07-05 02:06:18.960710','5','Photo object (5)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(18,'2023-07-05 02:06:51.394395','6','Photo object (6)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(19,'2023-07-05 02:14:06.484033','10','Photo object (10)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(20,'2023-07-05 02:14:32.578797','11','Photo object (11)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(21,'2023-07-05 02:18:48.214981','15','Photo object (15)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(22,'2023-07-05 02:19:08.384086','16','Photo object (16)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(23,'2023-07-05 02:20:38.821520','15','Photo object (15)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(24,'2023-07-05 02:20:46.926673','16','Photo object (16)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(25,'2023-07-26 09:18:59.553606','2','Item object (2)',2,'[{\"changed\": {\"fields\": [\"Category\"]}}]',8,1),(26,'2023-07-26 09:19:16.769781','14','Item object (14)',2,'[{\"changed\": {\"fields\": [\"Description\", \"Category\"]}}]',8,1),(27,'2023-07-26 09:19:25.344780','7','Item object (7)',2,'[{\"changed\": {\"fields\": [\"Description\", \"Category\"]}}]',8,1),(28,'2023-08-02 01:24:26.657343','16','Item object (16)',3,'',8,1),(29,'2023-08-02 01:24:26.666434','17','Item object (17)',3,'',8,1),(30,'2023-08-02 01:24:26.674488','18','Item object (18)',3,'',8,1),(31,'2023-08-02 01:24:26.682428','19','Item object (19)',3,'',8,1),(32,'2023-08-02 01:24:26.690790','20','Item object (20)',3,'',8,1),(33,'2023-08-02 01:24:26.698942','21','Item object (21)',3,'',8,1),(34,'2023-08-02 01:24:26.706359','22','Item object (22)',3,'',8,1),(35,'2023-08-02 01:24:26.712688','23','Item object (23)',3,'',8,1),(36,'2023-08-02 01:24:26.718409','24','Item object (24)',3,'',8,1),(37,'2023-08-02 01:24:26.725421','25','Item object (25)',3,'',8,1),(38,'2023-08-17 04:15:23.549712','137','Photo object (137)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(39,'2023-08-17 04:15:44.455958','141','Photo object (141)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(40,'2023-08-17 04:16:48.702473','139','Photo object (139)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(41,'2023-08-17 04:19:16.146794','143','Photo object (143)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(42,'2023-08-17 04:19:55.420305','144','Photo object (144)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(43,'2023-08-17 04:20:13.648110','145','Photo object (145)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(44,'2023-08-17 04:22:42.230545','148','Photo object (148)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(45,'2023-08-17 04:23:11.952032','149','Photo object (149)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(46,'2023-08-17 04:23:30.607293','150','Photo object (150)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(47,'2023-08-17 04:23:42.365338','151','Photo object (151)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(48,'2023-08-17 04:25:17.681666','153','Photo object (153)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(49,'2023-08-17 04:25:29.510842','154','Photo object (154)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(50,'2023-08-17 04:25:41.485532','155','Photo object (155)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(51,'2023-08-17 04:38:05.694436','158','Photo object (158)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(52,'2023-08-17 04:38:21.306296','157','Photo object (157)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(53,'2023-08-17 04:38:33.475665','161','Photo object (161)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(54,'2023-08-17 04:41:54.177251','158','Photo object (158)',2,'[]',7,1),(55,'2023-08-17 04:42:22.832248','159','Photo object (159)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(56,'2023-08-17 04:42:56.515486','159','Photo object (159)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(57,'2023-08-17 04:44:13.951483','163','Photo object (163)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(58,'2023-08-17 04:44:22.168012','165','Photo object (165)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(59,'2023-08-17 04:45:54.194166','168','Photo object (168)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(60,'2023-08-17 04:46:10.678599','170','Photo object (170)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(61,'2023-08-17 04:48:29.590306','183','Photo object (183)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(62,'2023-08-17 04:48:39.988650','185','Photo object (185)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(63,'2023-08-17 04:50:02.086804','188','Photo object (188)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(64,'2023-08-17 04:50:10.585473','190','Photo object (190)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(65,'2023-08-17 04:52:00.246618','193','Photo object (193)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(66,'2023-08-17 04:52:17.836146','194','Photo object (194)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1),(67,'2023-08-17 04:52:30.735197','196','Photo object (196)',2,'[{\"changed\": {\"fields\": [\"File\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_results_chordcounter`
--

DROP TABLE IF EXISTS `django_celery_results_chordcounter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_results_chordcounter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) NOT NULL,
  `sub_tasks` longtext NOT NULL,
  `count` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  CONSTRAINT `django_celery_results_chordcounter_chk_1` CHECK ((`count` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_results_chordcounter`
--

LOCK TABLES `django_celery_results_chordcounter` WRITE;
/*!40000 ALTER TABLE `django_celery_results_chordcounter` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_results_chordcounter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_results_groupresult`
--

DROP TABLE IF EXISTS `django_celery_results_groupresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_results_groupresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  KEY `django_cele_date_cr_bd6c1d_idx` (`date_created`),
  KEY `django_cele_date_do_caae0e_idx` (`date_done`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_results_groupresult`
--

LOCK TABLES `django_celery_results_groupresult` WRITE;
/*!40000 ALTER TABLE `django_celery_results_groupresult` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_results_groupresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_results_taskresult`
--

DROP TABLE IF EXISTS `django_celery_results_taskresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_results_taskresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext,
  `meta` longtext,
  `task_args` longtext,
  `task_kwargs` longtext,
  `task_name` varchar(255) DEFAULT NULL,
  `worker` varchar(100) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `periodic_task_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `django_cele_task_na_08aec9_idx` (`task_name`),
  KEY `django_cele_status_9b6201_idx` (`status`),
  KEY `django_cele_worker_d54dd8_idx` (`worker`),
  KEY `django_cele_date_cr_f04a50_idx` (`date_created`),
  KEY `django_cele_date_do_f59aad_idx` (`date_done`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_results_taskresult`
--

LOCK TABLES `django_celery_results_taskresult` WRITE;
/*!40000 ALTER TABLE `django_celery_results_taskresult` DISABLE KEYS */;
INSERT INTO `django_celery_results_taskresult` VALUES (93,'aa3069c7-a302-4dc1-b429-184eec9e0b53','SUCCESS','application/json','utf-8','null','2023-08-21 02:00:02.671171',NULL,'{\"children\": []}',NULL,NULL,NULL,NULL,'2023-08-21 02:00:02.670923',NULL),(94,'e7a0c00d-6765-4f83-a699-4eef66158251','SUCCESS','application/json','utf-8','null','2023-08-21 19:00:03.465367',NULL,'{\"children\": []}',NULL,NULL,NULL,NULL,'2023-08-21 19:00:03.465287',NULL),(95,'675da108-1d71-477b-911e-209efb3c05e9','SUCCESS','application/json','utf-8','null','2023-08-22 02:00:03.152509',NULL,'{\"children\": []}',NULL,NULL,NULL,NULL,'2023-08-22 02:00:03.152254',NULL);
/*!40000 ALTER TABLE `django_celery_results_taskresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'django_celery_results','chordcounter'),(12,'django_celery_results','groupresult'),(10,'django_celery_results','taskresult'),(8,'items','item'),(7,'photos','photo'),(6,'sessions','session'),(13,'stats','itemstatsdaily'),(14,'stats','searchcategory'),(17,'stats','searchlocation'),(15,'stats','searchstats'),(16,'stats','searchusedyears'),(9,'wishlists','wishlist');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-07-03 07:07:07.644720'),(2,'auth','0001_initial','2023-07-03 07:07:08.621312'),(3,'admin','0001_initial','2023-07-03 07:07:08.863240'),(4,'admin','0002_logentry_remove_auto_add','2023-07-03 07:07:08.886269'),(5,'admin','0003_logentry_add_action_flag_choices','2023-07-03 07:07:08.908182'),(6,'contenttypes','0002_remove_content_type_name','2023-07-03 07:07:09.042413'),(7,'auth','0002_alter_permission_name_max_length','2023-07-03 07:07:09.145275'),(8,'auth','0003_alter_user_email_max_length','2023-07-03 07:07:09.190166'),(9,'auth','0004_alter_user_username_opts','2023-07-03 07:07:09.208768'),(10,'auth','0005_alter_user_last_login_null','2023-07-03 07:07:09.297290'),(11,'auth','0006_require_contenttypes_0002','2023-07-03 07:07:09.309578'),(12,'auth','0007_alter_validators_add_error_messages','2023-07-03 07:07:09.327753'),(13,'auth','0008_alter_user_username_max_length','2023-07-03 07:07:09.432630'),(14,'auth','0009_alter_user_last_name_max_length','2023-07-03 07:07:09.525324'),(15,'auth','0010_alter_group_name_max_length','2023-07-03 07:07:09.563061'),(16,'auth','0011_update_proxy_permissions','2023-07-03 07:07:09.590095'),(17,'auth','0012_alter_user_first_name_max_length','2023-07-03 07:07:09.690220'),(18,'django_celery_results','0001_initial','2023-07-03 07:07:09.791349'),(19,'django_celery_results','0002_add_task_name_args_kwargs','2023-07-03 07:07:09.894165'),(20,'django_celery_results','0003_auto_20181106_1101','2023-07-03 07:07:09.907531'),(21,'django_celery_results','0004_auto_20190516_0412','2023-07-03 07:07:10.036645'),(22,'django_celery_results','0005_taskresult_worker','2023-07-03 07:07:10.113041'),(23,'django_celery_results','0006_taskresult_date_created','2023-07-03 07:07:10.233235'),(24,'django_celery_results','0007_remove_taskresult_hidden','2023-07-03 07:07:10.333956'),(25,'django_celery_results','0008_chordcounter','2023-07-03 07:07:10.392161'),(26,'django_celery_results','0009_groupresult','2023-07-03 07:07:10.924398'),(27,'django_celery_results','0010_remove_duplicate_indices','2023-07-03 07:07:10.951195'),(28,'django_celery_results','0011_taskresult_periodic_task_name','2023-07-03 07:07:10.992458'),(29,'items','0001_initial','2023-07-03 07:07:11.043823'),(30,'items','0002_item_is_liked_item_item_name','2023-07-03 07:07:11.146796'),(31,'items','0003_rename_user_id_item_user_id_remove_item_location_and_more','2023-07-03 07:07:11.337960'),(32,'items','0004_alter_item_category','2023-07-03 07:07:11.352889'),(33,'items','0005_alter_item_category','2023-07-03 07:07:11.368827'),(34,'items','0006_item_location_alter_item_used_years','2023-07-03 07:07:11.413285'),(35,'items','0007_alter_item_user_id','2023-07-03 07:07:11.603355'),(36,'items','0008_remove_item_is_liked','2023-07-03 07:07:11.643117'),(37,'items','0009_item_is_deleted','2023-07-03 07:07:11.700507'),(38,'items','0010_item_buy_user_id','2023-07-03 07:07:11.788547'),(39,'items','0011_alter_item_buy_user_id','2023-07-03 07:07:11.868245'),(40,'items','0012_alter_item_dday_date_alter_item_manufactured_date_and_more','2023-07-03 07:07:12.212027'),(41,'photos','0001_initial','2023-07-03 07:07:12.342746'),(42,'photos','0002_alter_photo_item','2023-07-03 07:07:12.359114'),(43,'sessions','0001_initial','2023-07-03 07:07:12.448226'),(44,'wishlists','0001_initial','2023-07-03 07:07:12.709045'),(45,'items','0013_alter_item_category_alter_item_warranty_date','2023-07-26 09:01:02.797870'),(46,'items','0014_alter_item_dday_date_alter_item_warranty_date','2023-08-02 01:29:09.154460'),(47,'stats','0001_initial','2023-08-02 05:07:52.474107');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('13se09e38y9q38kmfxtuo6sk8v4rz2az','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qOoFR:lB4FM-Y2goC_Q1UmZb0iSIOFjEfDDstVhdMEVY8yObc','2023-08-09 23:48:53.518034'),('7jtgadf3q1p3fklt7s39ghs3csuhifux','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qW7sx:icCBOnzq9rfMQZ4icRM6NEMWZz_U9hWpJISC__-nqvI','2023-08-30 04:11:55.141047'),('9gpuhijxl2xim90m061iha6x62clnbef','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qSoP2:j1lLzBkyXuxMVHOqGNLnr48ezgg9978XnlwhZvBX95s','2023-08-21 00:47:20.403176'),('fgbl6kumwlj1d0465rjvsc3vbpjni163','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qOafA:JWJ78EFTXXugb6cWeoIcZhlan6bSaEKRqepVtW41l1g','2023-08-09 09:18:32.976583'),('ftst4pgvqq6r6qvjni6n81lnvjmz89vo','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qOYGQ:UoY0NwUzwmIDrknnOrZmIjCiibL8NgQL2yQ4BFEhV7U','2023-08-09 06:44:50.385433'),('isgdgxvzqfs8j8ywzhliglknckx014nw','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qQecC:knWj7f1CkmQJFK3b1irdVyOaY9Y4gGhtEqpaatjRZQM','2023-08-15 01:56:00.754704'),('l05lim5i1liyz2wz1y683ifnl0im954e','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qTXkN:4oVu1O1_0j7saH6d2AbXKsJnuU6Y4d_kEiYUmyy4XlU','2023-08-23 01:12:23.293870'),('o4ut1sn9q739r9mbpznlb9svhewan40s','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qGuii:lxsTQBrlYDMlTGjIL1iAfyoX_mEKIkLTAaQQXcL8HFQ','2023-07-19 05:06:28.024499'),('v3dc5knn2xp68lxiwc86obn55shtvepo','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qGvBM:7IrHLu0SuKqtcV936kbdMpsuxMbE90xgSxUB5qDUwbU','2023-07-19 05:36:04.974353'),('wp5x338bv9xn71y3381ki0b3l7fbwctj','.eJxVjEEOwiAQRe_C2pCClAGX7nsGMsyAVA1NSrsy3l1JutDtf-_9lwi4byXsLa1hZnERSpx-t4j0SLUDvmO9LZKWuq1zlF2RB21yWjg9r4f7d1CwlW8NSJi9IhodGGAgB4PPOqPHhDHqs_LsGHGwIxKrrthsmI0Fr8Bq8f4ACUI4dA:1qR0YV:JB5EfcR5A007Bo8cAFGKo-CFm1k2w7hU6lrkX7NSano','2023-08-16 01:21:39.557394');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items_item`
--

DROP TABLE IF EXISTS `items_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items_item` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` longtext NOT NULL,
  `is_negotiable` tinyint(1) NOT NULL,
  `is_sold` tinyint(1) NOT NULL,
  `price` int unsigned NOT NULL,
  `used_years` varchar(20) NOT NULL,
  `manufactured_date` date NOT NULL,
  `warranty_date` date DEFAULT NULL,
  `description` longtext NOT NULL,
  `category` varchar(25) NOT NULL,
  `dday_date` date DEFAULT NULL,
  `item_name` varchar(20) NOT NULL,
  `location` varchar(10) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `buy_user_id` longtext,
  PRIMARY KEY (`id`),
  CONSTRAINT `items_item_chk_2` CHECK ((`price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items_item`
--

LOCK TABLES `items_item` WRITE;
/*!40000 ALTER TABLE `items_item` DISABLE KEYS */;
INSERT INTO `items_item` VALUES (1,'2023-07-04 18:42:21.017684','2023-07-26 09:01:02.748718','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',1,0,600000,'1년~2년','2021-02-10','2022-02-10','모델명 :CWS-1242RF\r\n45박스형 직냉식\r\n냉동 1/2\r\n제품중량 : 150kg\r\n기후등급 4\r\n스테인리스\r\n더 궁금한 내용 있으시면 채팅 주세요~~ 네고도 가능합니다','냉장고/냉동고','2023-07-22','우성 업소용 냉장고','중구',0,''),(2,'2023-07-04 18:54:45.629484','2023-07-26 09:18:59.545649','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',1,0,800000,'2년~3년','2020-04-11','2021-04-11','생산량은 55kg이고 저장량은 22kg입니다^^\r\n이태리 브레마사에서 만든거예요 공냉식으로 냉각합니다~','제빙기','2023-08-09','브레마 제빙기','중구',0,''),(3,'2023-07-04 19:02:34.567357','2023-07-05 01:12:50.203087','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',0,0,450000,'1년~2년','2021-04-21','2022-04-21','전기사양 220v/60Hz\r\n사용 온도는 2-8도에요!\r\n\r\n카운터 900 모델이고 a/s 3개월가능해요~','쇼케이스','2023-07-26','그랜드우성 쇼케이스','중구',0,''),(4,'2023-07-05 08:57:33.202798','2023-07-05 10:38:18.629735','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,800000,'2년~3년','2020-03-05','2021-03-05','음료 보관용으로 사용했고 2년 정도 사용했습니다! 상태 깔끔하고 작동 잘 되는 거 확인했습니다!\n용량: 752리터\n온도 범위: 1~8도\n\n직거래는 중구 황학동에서 가능하고 배송 시 용달비용 추가될 것 같습니다','쇼케이스','2023-08-20','SKIPIO 음료 냉장고','중구',1,''),(5,'2023-07-05 09:19:57.915776','2023-07-05 10:29:27.722042','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,1100000,'2년~3년','2020-04-05','2021-04-05','2년 정도 사용하고 창고에 보관 중입니다. 작동 잘 되는 거 확인했습니다!\n\n용량 510리터\n온도 범위 -30도 ~ -18도\n\n직거래는 중구 황학동에서 가능하고 배송 요청 시 용달 비용 추가로 발생합니다!','쇼케이스','2023-08-20','우성 냉동용 쇼케이스','중구',1,''),(6,'2023-07-05 09:28:47.112568','2023-07-05 09:28:47.112627','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,1000000,'2년~3년','2020-04-11','2021-04-11','냉동 쇼케이스 2대 판매합니다. 둘 다 2년 정도 사용했고 현재는 창고에 있습니다. 작동 잘 되는 거 확인했습니다! 2개 일괄 구매하시면 180에 드리겠습니다\n\n용량 501리터\n온도 범위 -25도 ~ -15도\n\n직거래는 중구 황학동에서 가능하고 배송 필요하시면 용달 비용 추가됩니다!','쇼케이스','2023-07-30','SKIPIO 냉동쇼케이스','중구',0,''),(7,'2023-07-05 09:38:55.610079','2023-07-26 09:19:25.336790','D439KIogxNfyaUOvmklBnw8ysJX2',0,0,350000,'2년~3년','2019-05-18','2020-05-18','브레마 제빙기 50kg입니다. 구매한 지 3년 정도 돼서 저렴하게 올립니다. 카페에서 사용했고 실제로 많이들 쓰시는 모델입니다. 작동 잘 되는 거 확인했습니다!\r\n\r\n상태: 상\r\n\r\n직거래는 중구 황학동에서 가능하고 배송 필요할 경우 운송비 추가됩니다~\r\n저렴하게 올리는 거라 네고는 사양하겠습니다..','제빙기','2023-07-25','브레마 제빙기 50kg','중구',0,''),(8,'2023-07-05 09:53:42.132944','2023-07-26 09:01:02.752237','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,700000,'2년~3년','2019-07-05','2020-07-27','위 2칸은 냉장, 아래 2칸은 냉동고입니다. 3년 정도 사용한 거 같고 외관 상태는 깔끔하나 내부 긁힘 등을 감안해서 저렴하게 내놓습니다! 곧 가게를 비워야해서 빠르게 판매해봅니다~\n\n직거래 장소는 중구 황학동인데 용달 가져오셔야 합니다! 배송 원하시면 용달비 추가됩니다~','냉장고/냉동고','2023-07-21','우성 냉장,냉동고45박스','중구',1,''),(9,'2023-07-05 10:00:26.825146','2023-07-26 09:01:02.755740','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,600000,'2년~3년','2019-05-28','2020-05-28','위 2칸은 냉장, 아래 2칸은 냉동입니다. 3년 정도 사용했고 외관 상태는 깔끔하나 내부 긁힘 등을 감안해서 저렴하게 내놓습니다! 곧 가게 비워야해서 빠르게 판매해봅니다~\n\n직거래는 중구 황학동에서 합니다. 오실 때 용달 가져오셔야 해요! 배송 필요하시면 운송비 추가로 들어요~','냉장고/냉동고','2023-07-20','우성 냉장/냉동고45박스','중구',0,''),(10,'2023-07-05 10:08:24.549718','2023-07-26 09:01:02.760400','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,500000,'2년~3년','2020-09-13','2021-09-13','올냉장이고 상태 깔끔합니다. 가게를 곧 비워야해서 빠르게 판매해봐요~\n\n직거래 위치는 중구 황학동이고 용달 필요합니다!','냉장고/냉동고','2023-07-20','우성 냉장고 올냉장','중구',0,''),(11,'2023-07-05 10:26:52.867400','2023-07-05 10:26:52.867641','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,600000,'1년~2년','2021-04-23','2022-04-23','제품명: 은성 4단 쇼케이스\n상태: 최상\n온도 범위: 5도~8도\n\n사용한 지 1년 정도 됐고 상태 깔끔합니다! 2대 같은 모델으로 일괄 구매 시 100만원에 드릴게요~\n\n직거래 장소는 중구 황학동이고 용달 필요합니다! 배송 요청 시 용달비 추가 발생됩니다~','쇼케이스','2023-08-26','4단 쇼케이스','중구',0,''),(12,'2023-07-05 10:37:16.278667','2023-08-13 02:02:15.070531','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,700000,'2년~3년','2020-11-07','2021-11-07','2년 정도 사용했고 현재는 창고에 있습니다. 작동 잘 되는 거 확인했습니다!\n\n용량 510리터\n온도 범위 -18도 ~ -30도\n\n직거래 장소는 중구 황학동이고 용달 필요합니다! 배송 요청하시면 용달비 추가됩니다~','쇼케이스','2023-08-24','우성 수직냉동 쇼케이스','중구',0,''),(13,'2023-07-05 10:43:55.793697','2023-08-09 11:06:28.833267','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,550000,'2년~3년','2020-11-09','2021-11-09','음료 보관용으로 2년 정도 사용했습니다.\n\n용량 752리터\n온도 범위 1~8도\n\n직거래는 중구 황학동에서 하고 용달 필요합니다! 배송 필요하시면 용달비 추가 발생해요~','쇼케이스','2023-08-24','스키피오 음료 쇼케이스','중구',0,''),(14,'2023-07-11 01:07:36.514609','2023-07-26 09:19:16.759824','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,25000,'1년 이하','2022-09-07','2023-03-07','[책상, 데스커 컴퓨터 책상] 11개\r\n- 1400x700, 1200×700\r\n- 2022년 9월 구매\r\n- 상태 매우 좋은편, 가방걸이 달려있음\r\n- 8만원\r\n\r\n[시디즈, T50라이트 블랙쉘 사무용의자, 다크그레이] 11개\r\n- 2022년 9월 구매\r\n- 상태 매우 좋은편\r\n- 16.5만원\r\n\r\n[데스커 수납형 모니터받침대 1000폭] 11개\r\n- 2022년 9월 구매\r\n- 상태 매우 좋은편\r\n- 2.5만원\r\n\r\n[데스커 3단 슬림서랍 (잠금장치형) DSAP1303A] 11개\r\n- 2022년 9월 구매\r\n- 상태 매우 좋은편\r\n- 6만원\r\n\r\n사무실에서 사용하던 가구 처분합니다!\r\n주소: 서울특별시 송파구 방이동 59-14 3층\r\n이곳으로 가지러 오시면 됩니다\r\n책상은 조립 분해해드립니다!','가구','2023-07-31','사무용품 정리','송파구',0,''),(15,'2023-07-11 01:14:22.682224','2023-07-11 01:14:22.683605','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,280000,'1년~2년','2021-09-14','2022-09-14','제품명: 음료 쇼케이스 4단\n제조일자: 2021.09.14(실사용 1년)\n상태: 최상\n\n과일 보관용으로 구매했던 음료 쇼케이스입니다. 세밀한 온도조절이 필요하다보니 15만원 상당의 온도조절기를 추가로 부착했습니다.\n배송은 별도이며 직거래 위치는 신당동입니다~','쇼케이스','2023-07-31','음료 쇼케이스','중구',0,''),(26,'2023-08-02 02:00:26.883312','2023-08-02 02:01:19.521261','YffrXPieCvgV2cQAn2HPkFTyhMJ3',0,0,333,'1년~2년','2023-08-02','2023-08-02','벽돌 좋아요','가스레인지/인덕션','2023-08-17','벽돌 팝니다','성북구',1,''),(27,'2023-08-09 15:08:00.800185','2023-08-09 15:08:00.800627','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,2300000,'2년~3년','2020-06-04','2021-06-04','제품명: 크리콤 런치케이스 고효율형\n현재 세종시 집현동에 있는 창고에 있습니다!\n배송가능하지만 배송비 별도입니다~','쇼케이스','2023-08-31','마트 쇼케이스','관악구',0,''),(28,'2023-08-09 15:30:19.039121','2023-08-09 15:30:19.039302','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,700000,'2년~3년','2021-06-10','2022-06-10','제품명: 캐리어 442L 6단 쇼케이스\n온도: -24 ~ -18\n슈퍼에서 아이스크림 및 냉동식품 보관용으로 사용하던 냉동 쇼케이스입니다!\n현재 세종시 집현동에 있는 창고에 보관 중입니다!\n배송 가능하나 배송비는 별도입니다!','쇼케이스','2023-08-31','냉동 쇼케이스','관악구',0,''),(29,'2023-08-09 15:32:59.684752','2023-08-09 15:32:59.684838','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,120000,'2년~3년','2021-06-02','2022-06-02','단면 900*450*1400 4개\n양면 900*450*1400 8개\n단면 900*450*1800 6개\n\n가격: 양면 개당 17만, 단면 개당 12만\n세종시 집현동에 있는 창고에 보관 중입니다!\n배송비는 별도이지만 전체 구매하시면 배송비 제가 부담하겠습니다!','가구','2023-08-31','마트 진열대','관악구',0,''),(30,'2023-08-09 15:37:09.401668','2023-08-09 15:37:09.401810','D439KIogxNfyaUOvmklBnw8ysJX2',0,0,500000,'2년~3년','2022-10-14','2023-01-14','제품명: 포스뱅크(카드단말기1대, 서명패드1대, 용기프린터기2대, 키보드, 마우스, 돈통)\n\n택배도 가능합니다!','기타','2023-09-30','포스뱅크 포스기','도봉구',0,''),(31,'2023-08-09 15:41:04.424959','2023-08-09 15:41:04.425017','D439KIogxNfyaUOvmklBnw8ysJX2',0,0,130000,'1년~2년','2022-11-06','2022-11-06','제품명: 깡통테이블 8개 (수저통내장)\n지금 경기도 양주에 있는 창고에 있습니다!\n직거래 장소: 옥정로196 파스텔시티 121호\n용달 있으면 배송도 가능합니다','가구','2023-09-30','깡통 테이블 8개','도봉구',0,''),(32,'2023-08-09 15:47:41.053910','2023-08-09 15:47:41.054059','D439KIogxNfyaUOvmklBnw8ysJX2',0,0,200000,'1년~2년','2021-10-28','2022-04-24','직거래만 가능합니다~\n직거래 장소: 송파구 삼전로 4길 14-1 입니다!\n위 장소로 찾으러 와주시면 됩니다!!','가구','2023-08-25','시디즈 T50 화이트쉘 메쉬의자','송파구',0,''),(33,'2023-08-09 15:57:27.559286','2023-08-09 15:57:27.559338','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,200000,'4년~5년','2018-11-10','2019-11-10','카페 폐업해서 정리합니다\n\n직거래 장소: 동탄 오산로 86-11','커피머신','2023-08-31','피오렌자또 F64e 그라인더','서초구',0,''),(34,'2023-08-09 16:00:49.703115','2023-08-09 16:08:37.086261','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,450000,'4년~5년','2018-11-10','2019-11-10','제품명: 우성 3도어 테이블 냉장고\n직거래 장소: 동탄 오산로 86-11\n배송비 별도로 배송가능합니다!','냉장고/냉동고','2023-08-31','냉장/냉동고','서초구',0,''),(35,'2023-08-09 16:02:54.324262','2023-08-09 16:02:54.324316','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,1500000,'4년~5년','2018-11-10','2018-11-10','직거래 장소: 동탄 오산로 86-11\n배송비 별도로 배송 가능합니다!','커피머신','2023-08-31','프로맥 그린미 플러스 커피머신 2그룹','서초구',0,''),(36,'2023-08-09 16:04:47.299952','2023-08-09 16:04:47.300069','D439KIogxNfyaUOvmklBnw8ysJX2',0,0,200000,'4년~5년','2018-11-10','2019-11-10','제품명: 진성 js1bw 전자동 핫워터 디스펜서\n직거래 장소: 동탄 오산로 86-11\n배송 가능하나 배송비 별도입니다!','기타','2023-08-31','진성 온수기','서초구',0,''),(37,'2023-08-09 16:08:09.956649','2023-08-09 16:08:09.956703','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,450000,'4년~5년','2018-09-16','2019-09-16','제품명: 카이저 제빙기 110kg(imk-3121)\n직거래 장소: 동탄 오산로 86-11\n배송가능하나 배송비 별도입니다!','제빙기','2023-08-31','카이저 제빙기 110kg','서초구',0,''),(38,'2023-08-09 16:11:12.441023','2023-08-09 16:11:12.441075','D439KIogxNfyaUOvmklBnw8ysJX2',1,0,200000,'4년~5년','2018-11-10','2019-11-10','제품명: 다이아 R&F 제과 쇼케이스 UKGS-1200\n직거래 장소: 동탄 오산로 86-11\n배송가능하나 배송비 별도입니다!','쇼케이스','2023-08-31','제과 쇼케이스 1200','서초구',0,''),(39,'2023-08-10 12:41:39.589156','2023-08-10 12:41:39.589332','Y3K1mkgOedQWwRd9dW6PiZzsLM62',1,0,700000,'2년~3년','2023-08-10','2023-08-10','3년정도사용\n키친모아 울트힌 파워 크린 불판세척기\n천호역 국민은행 직거래 직접운반\n제조날짜 보증날짜 미확인','세척기','2023-08-25','불판세척기','강동구',0,'');
/*!40000 ALTER TABLE `items_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photos_photo`
--

DROP TABLE IF EXISTS `photos_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photos_photo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `file` varchar(200) NOT NULL,
  `item_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `photos_photo_item_id_5ca1bbdd_fk_items_item_id` (`item_id`),
  CONSTRAINT `photos_photo_item_id_5ca1bbdd_fk_items_item_id` FOREIGN KEY (`item_id`) REFERENCES `items_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photos_photo`
--

LOCK TABLES `photos_photo` WRITE;
/*!40000 ALTER TABLE `photos_photo` DISABLE KEYS */;
INSERT INTO `photos_photo` VALUES (1,'2023-07-04 18:42:21.080146','2023-07-05 00:23:10.438082','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9cdb62ff-540f-4c9e-09ee-4587de20b400/public',1),(2,'2023-07-04 18:42:21.093800','2023-07-05 00:24:05.262637','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ddce0333-f37a-4c88-e3ed-9a65a5ca6e00/public',1),(3,'2023-07-04 18:42:21.097912','2023-07-05 00:24:35.801388','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/59ed0d4e-54d3-4855-b36a-4bd69ca36c00/public',1),(4,'2023-07-04 18:42:21.102110','2023-07-05 02:05:40.460667','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/a6a17c75-668d-4312-82ff-496fb473ea00/public',1),(5,'2023-07-04 18:42:21.106259','2023-07-05 02:06:18.950526','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/810d1d6b-0618-45c0-c41c-a9a5ec889700/public',1),(6,'2023-07-04 18:42:21.110151','2023-07-05 02:06:51.384124','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d77f0d7c-f6c9-43d5-dcbe-7a55b3278200/public',1),(7,'2023-07-04 18:54:45.682194','2023-07-05 00:26:54.067979','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0f7ec53f-50fb-436b-3c65-1552cdb96200/public',2),(8,'2023-07-04 18:54:45.687189','2023-07-05 00:27:25.023220','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/df2f5920-eae4-4776-7678-8946e3fd7200/public',2),(9,'2023-07-04 18:54:45.691730','2023-07-05 00:28:13.381437','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/739847e9-800e-4a64-5794-d91306be2300/public',2),(10,'2023-07-04 18:54:45.696135','2023-07-05 02:14:06.479072','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0ad21712-646c-4d96-606d-ac33c8233f00/public',2),(11,'2023-07-04 18:54:45.700574','2023-07-05 02:14:32.574928','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0eb9fd40-0ecf-4eba-e194-b18ac0d21b00/public',2),(12,'2023-07-04 19:02:34.617423','2023-07-05 00:29:31.591174','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/147a51ee-6195-42d4-7ee8-2283f4386500/public',3),(13,'2023-07-04 19:02:34.621342','2023-07-05 00:29:47.584585','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2f60d040-22a6-4ff6-4093-ec49ae272500/public',3),(14,'2023-07-04 19:02:34.625005','2023-07-05 00:30:03.892749','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4baef2a9-2e24-4852-e6a9-5d995a499e00/public',3),(15,'2023-07-04 19:02:34.628854','2023-07-05 02:20:38.816803','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/22ec60dd-f83a-45d3-9743-d7e357224b00/public',3),(16,'2023-07-04 19:02:34.632506','2023-07-05 02:20:46.923001','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/073384a7-353a-4d49-fc45-397596ea0500/public',3),(17,'2023-07-05 08:57:33.265293','2023-07-05 08:57:33.265343','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/bd23d410-fc67-4b8a-c828-8a2531403c00/public',4),(18,'2023-07-05 08:57:33.273083','2023-07-05 08:57:33.273134','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c5d53366-1f1c-4c36-3b1f-00ec0f2c5300/public',4),(19,'2023-07-05 08:57:33.277800','2023-07-05 08:57:33.277842','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/dff7200d-b68a-4302-8c30-86c9cd47c800/public',4),(20,'2023-07-05 08:57:33.282601','2023-07-05 08:57:33.282644','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0e633be6-3014-4ba1-65ec-4932f6e2ac00/public',4),(21,'2023-07-05 08:57:33.287209','2023-07-05 08:57:33.287251','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/01c6b5af-2739-401f-efa9-a731e8821d00/public',4),(22,'2023-07-05 09:19:57.967046','2023-07-05 09:19:57.967093','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/dff61596-e67e-4b53-4ea4-ba04c9978e00/public',5),(23,'2023-07-05 09:19:57.971770','2023-07-05 09:19:57.971812','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/16110d44-6529-453e-3265-da1e2b211200/public',5),(24,'2023-07-05 09:19:57.976222','2023-07-05 09:19:57.976265','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/734ebc0c-8d2f-47ae-cf29-71dc8b3c2300/public',5),(25,'2023-07-05 09:19:57.980828','2023-07-05 09:19:57.980871','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/3287b3df-1203-4a91-7164-87529947f900/public',5),(26,'2023-07-05 09:19:57.985619','2023-07-05 09:19:57.985663','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/8c36f9a5-ed10-4370-57c7-8657800fc000/public',5),(27,'2023-07-05 09:28:47.164708','2023-07-05 09:28:47.164757','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c30c1dc1-5c58-4dd0-f2df-3ad1db75c300/public',6),(28,'2023-07-05 09:28:47.169572','2023-07-05 09:28:47.169615','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/1d447668-9eca-43d0-2e79-7a055cc06600/public',6),(29,'2023-07-05 09:28:47.174140','2023-07-05 09:28:47.174182','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/bad59fa9-0111-4347-5e7f-48f907c15d00/public',6),(30,'2023-07-05 09:28:47.178593','2023-07-05 09:28:47.178641','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/dbbb5756-c729-4f5c-3d48-37c3d97e3800/public',6),(31,'2023-07-05 09:28:47.183157','2023-07-05 09:28:47.183197','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c50155fe-cf28-4755-a4e4-58d761d27200/public',6),(32,'2023-07-05 09:38:55.663766','2023-07-05 09:38:55.663824','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/75a5bcf6-679b-45cf-35cf-a463f6340800/public',7),(33,'2023-07-05 09:38:55.668174','2023-07-05 09:38:55.668234','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6de335c7-3e85-482a-f77a-044832929300/public',7),(34,'2023-07-05 09:38:55.672127','2023-07-05 09:38:55.672207','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/bfe90a87-4ef8-4992-360a-c8449d146400/public',7),(35,'2023-07-05 09:38:55.676157','2023-07-05 09:38:55.676200','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/48c0579f-a065-4e65-9151-e58291429b00/public',7),(36,'2023-07-05 09:38:55.679998','2023-07-05 09:38:55.680042','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/dbdc7ae1-3425-430e-6578-2acf4a74b200/public',7),(37,'2023-07-05 09:53:42.138471','2023-07-05 09:53:42.138518','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/aa5adf27-4e80-4731-b987-58ca124d0f00/public',8),(38,'2023-07-05 09:53:42.143407','2023-07-05 09:53:42.143448','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/b6b632c9-847d-45a5-db11-8ed9f8aa3100/public',8),(39,'2023-07-05 09:53:42.148201','2023-07-05 09:53:42.148243','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d6926389-0a4b-4d85-d859-7220513b3a00/public',8),(40,'2023-07-05 09:53:42.152985','2023-07-05 09:53:42.153063','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7ae20eb1-1263-428f-9d4a-53ea60990300/public',8),(41,'2023-07-05 09:53:42.157778','2023-07-05 09:53:42.157816','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/faf8a0c4-8a38-4f66-1afa-a93ab3c8a100/public',8),(42,'2023-07-05 10:00:26.829528','2023-07-05 10:00:26.829573','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/326404aa-5a4e-4655-ba5e-40cdc85bf400/public',9),(43,'2023-07-05 10:00:26.833524','2023-07-05 10:00:26.833568','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/71f4e401-29f4-4869-19c3-4578e03e4400/public',9),(44,'2023-07-05 10:00:26.837172','2023-07-05 10:00:26.837214','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7f77cf26-b12b-466c-9bb2-f3b69f3e5600/public',9),(45,'2023-07-05 10:00:26.840894','2023-07-05 10:00:26.840936','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9d5335cb-3887-4a58-ff84-dcb3c96cbd00/public',9),(46,'2023-07-05 10:00:26.844572','2023-07-05 10:00:26.844612','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/af6c085d-662b-4ad4-f7cf-86ca011a3a00/public',9),(47,'2023-07-05 10:08:24.554527','2023-07-05 10:08:24.554570','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cef5566c-eeed-4eaa-8391-a38dfe963000/public',10),(48,'2023-07-05 10:08:24.559116','2023-07-05 10:08:24.559161','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c7882e34-0f71-4958-d0c9-f3f7b524a400/public',10),(49,'2023-07-05 10:08:24.563768','2023-07-05 10:08:24.563812','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/aa4e6301-c8b3-4e94-c7af-ccbf5a923300/public',10),(50,'2023-07-05 10:08:24.568225','2023-07-05 10:08:24.568270','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/eea60303-1bd8-4367-0630-cd800e3dbf00/public',10),(51,'2023-07-05 10:08:24.572892','2023-07-05 10:08:24.572939','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2acdf11e-50da-4df6-e425-d167da111100/public',10),(52,'2023-07-05 10:08:24.577564','2023-07-05 10:08:24.577608','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4b987784-f324-4ace-0a03-b1eecba2d500/public',10),(53,'2023-07-05 10:26:52.874494','2023-07-05 10:26:52.874541','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/fcae769b-9132-4b09-5534-676eca68de00/public',11),(54,'2023-07-05 10:26:52.879532','2023-07-05 10:26:52.879575','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/134ea97e-2237-4396-1cc1-d3e32922d100/public',11),(55,'2023-07-05 10:26:52.885173','2023-07-05 10:26:52.885223','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c5560f8d-09f7-47b0-da30-aa8c703de500/public',11),(56,'2023-07-05 10:26:52.889928','2023-07-05 10:26:52.889972','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/f1612e33-fbe3-40ea-7aa4-46009aef2b00/public',11),(57,'2023-07-05 10:26:52.894780','2023-07-05 10:26:52.894825','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9539e97d-31f7-44a3-2341-883795d22700/public',11),(58,'2023-07-05 10:26:52.899465','2023-07-05 10:26:52.899508','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6155c5c0-02f3-48c8-7f02-cc29b048d700/public',11),(59,'2023-07-05 10:26:52.904003','2023-07-05 10:26:52.904044','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0c9f81ab-9aa6-4a19-9573-6bbe7453a100/public',11),(60,'2023-07-05 10:37:16.283299','2023-07-05 10:37:16.283341','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5cd4798b-5510-48f1-a07d-27c424094e00/public',12),(61,'2023-07-05 10:37:16.287588','2023-07-05 10:37:16.287631','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/b207f6b4-211c-4306-f20e-f69b5e6a1700/public',12),(62,'2023-07-05 10:37:16.291466','2023-07-05 10:37:16.291507','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/28928996-8ecb-4988-61e5-d5f29d3aa700/public',12),(63,'2023-07-05 10:37:16.295266','2023-07-05 10:37:16.295311','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5654c040-0885-40ca-1912-8815079a9800/public',12),(64,'2023-07-05 10:37:16.299086','2023-07-05 10:37:16.299127','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2450fef3-6319-439d-401d-e8019850ec00/public',12),(65,'2023-07-05 10:43:55.845781','2023-07-05 10:43:55.845826','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d7ca5ce2-95ad-4f8f-f25d-15577ed5f600/public',13),(66,'2023-07-05 10:43:55.850600','2023-07-05 10:43:55.850644','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/12a4168a-e066-43da-fb5e-2a8b78ac3500/public',13),(67,'2023-07-05 10:43:55.855335','2023-07-05 10:43:55.855380','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7c541ad4-2b30-442c-a2d6-2e38e5489b00/public',13),(68,'2023-07-05 10:43:55.859885','2023-07-05 10:43:55.859941','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9ad7b498-a9ca-49fc-3db2-3a1b8665e100/public',13),(69,'2023-07-05 10:43:55.864359','2023-07-05 10:43:55.864402','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4dd29540-265a-4d4e-05bb-90af1d354f00/public',13),(70,'2023-07-11 01:07:36.574810','2023-07-11 01:07:36.574868','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/b201919a-90c8-4b45-42ae-cb3a9968f500/public',14),(71,'2023-07-11 01:07:36.581787','2023-07-11 01:07:36.581842','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/1b3e1ebf-1ac7-471c-90f4-09592b551d00/public',14),(72,'2023-07-11 01:07:36.586819','2023-07-11 01:07:36.586871','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/83994065-4b37-4b27-8b7a-b9ebd885f500/public',14),(73,'2023-07-11 01:07:36.590603','2023-07-11 01:07:36.590641','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/592de38c-1a95-4b0e-4f90-34127ae6b400/public',14),(74,'2023-07-11 01:07:36.594230','2023-07-11 01:07:36.594265','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6755f58f-4fd5-4448-6998-41eae2997900/public',14),(75,'2023-07-11 01:07:36.597796','2023-07-11 01:07:36.597832','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/25d203af-2c88-40e4-c772-66582fd97e00/public',14),(76,'2023-07-11 01:14:22.733635','2023-07-11 01:14:22.733677','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d5408d79-211a-43c9-205d-cab1689d4b00/public',15),(77,'2023-07-11 01:14:22.737814','2023-07-11 01:14:22.737855','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5ccb0bd2-4313-422b-d2f5-93f29b497000/public',15),(78,'2023-07-11 01:14:22.741424','2023-07-11 01:14:22.741465','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0763e32b-a838-45a5-72b4-3bad9d884f00/public',15),(79,'2023-07-11 01:14:22.745828','2023-07-11 01:14:22.745959','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cfaff799-adda-4e57-3d41-f1c84cbc4f00/public',15),(80,'2023-07-11 01:14:22.749564','2023-07-11 01:14:22.749601','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/828a9d9d-fc3a-4cfa-880b-a5a899502e00/public',15),(81,'2023-08-01 15:39:34.710924','2023-08-01 15:39:34.710984','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c981e3f1-9cbf-447c-6554-0631e99bdf00/public',NULL),(82,'2023-08-01 15:39:34.719133','2023-08-01 15:39:34.719176','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/b24e510f-c780-4edf-fd25-649d10111d00/public',NULL),(83,'2023-08-01 15:39:34.724293','2023-08-01 15:39:34.724335','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2af6f227-551e-45eb-a31e-54f55ba87700/public',NULL),(84,'2023-08-01 15:39:34.728932','2023-08-01 15:39:34.728973','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/32b2547b-afde-4007-8f42-fdb02fa8c600/public',NULL),(85,'2023-08-01 15:39:34.733456','2023-08-01 15:39:34.733501','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/99deac26-ec20-444f-627e-e0b68a6e8f00/public',NULL),(86,'2023-08-01 15:39:34.738583','2023-08-01 15:39:34.738627','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c156bae7-2ece-46ba-8768-bb6364b02b00/public',NULL),(87,'2023-08-01 15:39:47.689630','2023-08-01 15:39:47.689676','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/83a95d25-1d28-4d5b-6743-772d45936d00/public',NULL),(88,'2023-08-01 15:39:47.694835','2023-08-01 15:39:47.694877','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/169b311b-031d-4c1c-f21a-723960426100/public',NULL),(89,'2023-08-01 15:39:47.699613','2023-08-01 15:39:47.699654','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5c82a2e8-295d-43ef-a43c-0e1364e5cf00/public',NULL),(90,'2023-08-01 15:39:47.703974','2023-08-01 15:39:47.704017','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5ebb5317-a3a8-4244-afc8-84ef8382d300/public',NULL),(91,'2023-08-01 15:39:47.709069','2023-08-01 15:39:47.709121','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/730477fd-24af-4705-975e-a5e256f88100/public',NULL),(92,'2023-08-01 15:40:01.799153','2023-08-01 15:40:01.799199','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2e159754-065d-4106-2a7f-d211c23af000/public',NULL),(93,'2023-08-01 15:40:01.805924','2023-08-01 15:40:01.805969','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/e6eee492-cc7c-44b6-06a8-17739ce5a600/public',NULL),(94,'2023-08-01 15:40:01.811027','2023-08-01 15:40:01.811072','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7bc36d81-dde7-4ebb-5cf2-d171a91f4800/public',NULL),(95,'2023-08-01 15:40:01.817140','2023-08-01 15:40:01.817185','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/66859cda-2c5a-4a07-a4e0-edea46947100/public',NULL),(96,'2023-08-01 15:40:01.822738','2023-08-01 15:40:01.822780','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/445ca190-97dd-4b7a-186b-8ea82d6ca300/public',NULL),(97,'2023-08-01 15:40:20.108441','2023-08-01 15:40:20.108514','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/1f2ccc8c-3df9-4928-8bd8-58700cc35500/public',NULL),(98,'2023-08-01 15:40:20.113850','2023-08-01 15:40:20.113914','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4c2f2642-b3a7-4439-8b86-c21ccc7ba200/public',NULL),(99,'2023-08-01 15:40:20.118827','2023-08-01 15:40:20.118872','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/86d80a83-6a8a-470e-93ef-b6d5da3a6400/public',NULL),(100,'2023-08-01 15:40:20.123256','2023-08-01 15:40:20.123299','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7a57925d-1307-4dcc-1196-10b5b66be600/public',NULL),(101,'2023-08-01 15:40:20.127515','2023-08-01 15:40:20.127558','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/60b1327a-abbc-44a9-fe26-d41dceda2b00/public',NULL),(102,'2023-08-01 15:40:35.731241','2023-08-01 15:40:35.731290','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c9fa9a96-ec17-4189-965a-de173dedbc00/public',NULL),(103,'2023-08-01 15:40:35.736929','2023-08-01 15:40:35.736972','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/75bb858c-bcf4-4aba-e891-663e61579600/public',NULL),(104,'2023-08-01 15:40:35.740908','2023-08-01 15:40:35.740945','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/552c5961-4c7c-4baa-3b36-95dc7a034c00/public',NULL),(105,'2023-08-01 15:40:35.745353','2023-08-01 15:40:35.745390','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/bc54d747-bd91-4cef-5cde-565e5ad18000/public',NULL),(106,'2023-08-01 15:40:35.751326','2023-08-01 15:40:35.751362','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9b088bb9-a60f-41df-2505-45aba1c23c00/public',NULL),(107,'2023-08-01 15:48:59.685068','2023-08-01 15:48:59.685115','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/221427a4-8110-48cf-cfc3-1e0d92c59800/public',NULL),(108,'2023-08-01 15:48:59.690336','2023-08-01 15:48:59.690378','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/edcc0a7f-157e-47ca-1eda-7517dd7fd700/public',NULL),(109,'2023-08-01 15:48:59.694773','2023-08-01 15:48:59.694810','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cf55687e-fb17-4db8-9487-2e64ef4cd900/public',NULL),(110,'2023-08-01 15:48:59.699967','2023-08-01 15:48:59.700004','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/dc7df835-1d40-4232-aad0-d1b3eebcc200/public',NULL),(111,'2023-08-01 15:48:59.705675','2023-08-01 15:48:59.705713','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/736143c9-9028-4e81-b7e1-63308b7c1700/public',NULL),(112,'2023-08-01 15:50:13.748520','2023-08-01 15:50:13.748566','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/26a5a63d-659a-4462-b6de-48e8623e3800/public',NULL),(113,'2023-08-01 15:50:13.754033','2023-08-01 15:50:13.754077','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ada4a45b-6db7-487a-582e-2abd85d8e600/public',NULL),(114,'2023-08-01 15:50:13.759132','2023-08-01 15:50:13.759174','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/8ecae103-6c12-48aa-8e0b-3d2a707f3c00/public',NULL),(115,'2023-08-01 15:50:13.764504','2023-08-01 15:50:13.764543','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/1dd20879-68e6-408c-0b06-34f66c64bb00/public',NULL),(116,'2023-08-01 15:50:13.771372','2023-08-01 15:50:13.771415','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/e867eac0-b9dd-4e24-4001-5b3f71fe5a00/public',NULL),(117,'2023-08-02 00:08:20.850242','2023-08-02 00:08:20.850288','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9ef24ab5-80db-453d-0cfa-f398f770fd00/public',NULL),(118,'2023-08-02 00:08:20.857160','2023-08-02 00:08:20.857202','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d966c78d-97f5-4515-b75d-af466f9e1600/public',NULL),(119,'2023-08-02 00:08:20.861933','2023-08-02 00:08:20.861976','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d6292703-b636-48b7-c1f6-4988c8316600/public',NULL),(120,'2023-08-02 00:08:20.866185','2023-08-02 00:08:20.866222','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/62460168-ea84-4386-5d10-cbff56d6d700/public',NULL),(121,'2023-08-02 00:08:20.871224','2023-08-02 00:08:20.871261','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2f131120-7e6f-4f69-8c9b-843e74372c00/public',NULL),(122,'2023-08-02 00:59:25.093786','2023-08-02 00:59:25.093832','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/3599aa11-343a-4280-8367-a76e30df4400/public',NULL),(123,'2023-08-02 00:59:25.098402','2023-08-02 00:59:25.098466','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5565ec91-8b5d-4be5-f12b-b1bfa1048d00/public',NULL),(124,'2023-08-02 00:59:25.102127','2023-08-02 00:59:25.102166','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cd6153c4-adbb-4a93-f830-e42da4952300/public',NULL),(125,'2023-08-02 00:59:25.106565','2023-08-02 00:59:25.106604','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cfebf885-52fd-49bc-756c-e6d6cd29cf00/public',NULL),(126,'2023-08-02 00:59:25.110544','2023-08-02 00:59:25.110614','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/bdc03f04-f638-45c3-c8c5-ac8a03479e00/public',NULL),(127,'2023-08-02 01:07:42.211085','2023-08-02 01:07:42.211131','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ad2ed40f-5f9a-4c62-7d7a-bab734978300/public',NULL),(128,'2023-08-02 01:07:42.214925','2023-08-02 01:07:42.214967','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ba74fc77-c4bd-4401-7a47-18c13fd12500/public',NULL),(129,'2023-08-02 01:07:42.218869','2023-08-02 01:07:42.218910','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4e56082d-deb3-4f1e-4a10-0374f106f200/public',NULL),(130,'2023-08-02 01:07:42.222408','2023-08-02 01:07:42.222448','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ad840e27-ef23-47bb-abac-eecccf993100/public',NULL),(131,'2023-08-02 01:07:42.225994','2023-08-02 01:07:42.226059','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/0e600464-3be6-4ebb-6666-951db5d58b00/public',NULL),(132,'2023-08-02 02:00:26.934476','2023-08-02 02:00:26.934524','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/e9c06e75-8818-44e2-864d-aa02b66aa800/public',26),(133,'2023-08-02 02:00:26.939301','2023-08-02 02:00:26.939344','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2580204b-f633-4448-c90d-eb3e62b9ea00/public',26),(134,'2023-08-02 02:00:26.944096','2023-08-02 02:00:26.944141','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4c6a7eae-f1b3-4603-8184-82dc03dd8900/public',26),(135,'2023-08-02 02:00:26.949220','2023-08-02 02:00:26.949266','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/f798bf9e-0383-47ac-d21d-1c4aff0d2a00/public',26),(136,'2023-08-02 02:00:26.953966','2023-08-02 02:00:26.954019','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/e6876d33-113a-43b5-fc8e-008538a13f00/public',26),(137,'2023-08-09 15:08:00.856837','2023-08-17 04:15:23.545480','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/23624d37-e7a1-4e86-cd31-0436438eb600/public',27),(138,'2023-08-09 15:08:00.861242','2023-08-09 15:08:00.861284','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/8ff963d9-3256-422b-d1c1-15483c59cb00/public',27),(139,'2023-08-09 15:08:00.865597','2023-08-17 04:16:48.698292','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/454d9377-0680-4b03-992e-1cc59d05b200/public',27),(140,'2023-08-09 15:08:00.871805','2023-08-09 15:08:00.871908','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/8ff963d9-3256-422b-d1c1-15483c59cb00/public',27),(141,'2023-08-09 15:08:00.875996','2023-08-17 04:15:44.450049','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/23624d37-e7a1-4e86-cd31-0436438eb600/public',27),(142,'2023-08-09 15:30:19.093720','2023-08-09 15:30:19.093767','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c50c5e85-7546-4a1c-8989-1ba509275c00/public',28),(143,'2023-08-09 15:30:19.098590','2023-08-17 04:19:16.143285','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/04171dbc-a802-48d2-0b78-1b1b8f00f800/public',28),(144,'2023-08-09 15:30:19.102946','2023-08-17 04:19:55.415446','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/cf5ba492-f9b8-4fba-b3d6-214336360a00/public',28),(145,'2023-08-09 15:30:19.107226','2023-08-17 04:20:13.643323','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/7f190fb3-e78e-41a7-54d1-49f618d3ea00/public',28),(146,'2023-08-09 15:30:19.111630','2023-08-09 15:30:19.111670','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/c50c5e85-7546-4a1c-8989-1ba509275c00/public',28),(147,'2023-08-09 15:32:59.696034','2023-08-09 15:32:59.696086','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4796bb83-7dcb-450c-a970-cb6b270b0e00/public',29),(148,'2023-08-09 15:32:59.700443','2023-08-17 04:22:42.225568','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65c5dcab-7bd1-4efc-165c-f5b32e9b7200/public',29),(149,'2023-08-09 15:32:59.704779','2023-08-17 04:23:11.947811','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/db9f8c25-2640-4699-8a2b-f82182228200/public',29),(150,'2023-08-09 15:32:59.709518','2023-08-17 04:23:30.602907','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ac1b45c7-b4d8-4ce5-4c65-1d8e1dec2f00/public',29),(151,'2023-08-09 15:32:59.714425','2023-08-17 04:23:42.360805','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/47039032-89eb-48c1-e767-89067fbe8d00/public',29),(152,'2023-08-09 15:37:09.456645','2023-08-09 15:37:09.456691','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/aa7c41be-4604-4ed5-71f8-adf47984b300/public',30),(153,'2023-08-09 15:37:09.461100','2023-08-17 04:25:17.678115','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/019af598-e691-4504-26e2-7bc127158d00/public',30),(154,'2023-08-09 15:37:09.465848','2023-08-17 04:25:29.506551','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/923895eb-0954-47c3-5af4-f03d10d91900/public',30),(155,'2023-08-09 15:37:09.470096','2023-08-17 04:25:41.480797','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/288767c3-2a21-4264-1223-ad09670d9100/public',30),(156,'2023-08-09 15:37:09.474200','2023-08-09 15:37:09.474250','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/aa7c41be-4604-4ed5-71f8-adf47984b300/public',30),(157,'2023-08-09 15:41:04.429716','2023-08-17 04:38:21.302208','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9f5a24ea-3fb8-4b0a-52a8-8afd09372100/public',31),(158,'2023-08-09 15:41:04.434075','2023-08-17 04:41:54.171794','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/81abf364-ddcd-4457-8f30-f4429ac3f900/public',31),(159,'2023-08-09 15:41:04.439357','2023-08-17 04:42:56.511049','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/befd7c8d-0039-48c3-a280-bf098ee11500/public',31),(160,'2023-08-09 15:41:04.444058','2023-08-09 15:41:04.444107','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/66c1b909-6f07-47af-84f0-dc64c4737100/public',31),(161,'2023-08-09 15:41:04.448662','2023-08-17 04:38:33.471494','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9f5a24ea-3fb8-4b0a-52a8-8afd09372100/public',31),(162,'2023-08-09 15:47:41.065022','2023-08-09 15:47:41.065076','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/59350a93-8159-4ce6-c60c-d3481bbdf700/public',32),(163,'2023-08-09 15:47:41.074806','2023-08-17 04:44:13.948095','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/948b063b-7d13-4812-be90-26225b392800/public',32),(164,'2023-08-09 15:47:41.079089','2023-08-09 15:47:41.079126','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/59350a93-8159-4ce6-c60c-d3481bbdf700/public',32),(165,'2023-08-09 15:47:41.084012','2023-08-17 04:44:22.163874','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/948b063b-7d13-4812-be90-26225b392800/public',32),(166,'2023-08-09 15:47:41.087964','2023-08-09 15:47:41.088002','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/59350a93-8159-4ce6-c60c-d3481bbdf700/public',32),(167,'2023-08-09 15:57:27.612853','2023-08-09 15:57:27.612902','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/a8d12dba-d452-4109-4c26-f767c86cf200/public',33),(168,'2023-08-09 15:57:27.618162','2023-08-17 04:45:54.190221','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9bd3175a-ff11-4509-4fc4-b184f1154400/public',33),(169,'2023-08-09 15:57:27.622560','2023-08-09 15:57:27.622595','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/a8d12dba-d452-4109-4c26-f767c86cf200/public',33),(170,'2023-08-09 15:57:27.627149','2023-08-17 04:46:10.674512','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9bd3175a-ff11-4509-4fc4-b184f1154400/public',33),(171,'2023-08-09 15:57:27.631582','2023-08-09 15:57:27.631621','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/a8d12dba-d452-4109-4c26-f767c86cf200/public',33),(172,'2023-08-09 16:00:49.707655','2023-08-09 16:00:49.707695','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65e08a6e-67f0-4db2-763d-7016b1bc7e00/public',34),(173,'2023-08-09 16:00:49.712852','2023-08-09 16:00:49.712901','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65e08a6e-67f0-4db2-763d-7016b1bc7e00/public',34),(174,'2023-08-09 16:00:49.717151','2023-08-09 16:00:49.717191','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65e08a6e-67f0-4db2-763d-7016b1bc7e00/public',34),(175,'2023-08-09 16:00:49.721465','2023-08-09 16:00:49.721508','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65e08a6e-67f0-4db2-763d-7016b1bc7e00/public',34),(176,'2023-08-09 16:00:49.725715','2023-08-09 16:00:49.725754','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/65e08a6e-67f0-4db2-763d-7016b1bc7e00/public',34),(177,'2023-08-09 16:02:54.329723','2023-08-09 16:02:54.329769','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/07ec5aca-6e3d-4d66-965e-d4eeeeb2bd00/public',35),(178,'2023-08-09 16:02:54.334052','2023-08-09 16:02:54.334096','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/07ec5aca-6e3d-4d66-965e-d4eeeeb2bd00/public',35),(179,'2023-08-09 16:02:54.338401','2023-08-09 16:02:54.338445','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/07ec5aca-6e3d-4d66-965e-d4eeeeb2bd00/public',35),(180,'2023-08-09 16:02:54.342770','2023-08-09 16:02:54.342814','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/07ec5aca-6e3d-4d66-965e-d4eeeeb2bd00/public',35),(181,'2023-08-09 16:02:54.346860','2023-08-09 16:02:54.346990','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/07ec5aca-6e3d-4d66-965e-d4eeeeb2bd00/public',35),(182,'2023-08-09 16:04:47.305845','2023-08-09 16:04:47.305888','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2d9429f1-2083-46ff-3cd0-ce8fd3f7a200/public',36),(183,'2023-08-09 16:04:47.310784','2023-08-17 04:48:29.586092','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5c8daf71-e403-4914-fe65-924f9cf2e200/public',36),(184,'2023-08-09 16:04:47.315632','2023-08-09 16:04:47.315684','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2d9429f1-2083-46ff-3cd0-ce8fd3f7a200/public',36),(185,'2023-08-09 16:04:47.320353','2023-08-17 04:48:39.984541','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/5c8daf71-e403-4914-fe65-924f9cf2e200/public',36),(186,'2023-08-09 16:04:47.325016','2023-08-09 16:04:47.325064','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/2d9429f1-2083-46ff-3cd0-ce8fd3f7a200/public',36),(187,'2023-08-09 16:08:09.961808','2023-08-09 16:08:09.961851','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ef7a4c6d-556a-4506-f555-27a4f9ca8100/public',37),(188,'2023-08-09 16:08:09.969103','2023-08-17 04:50:02.082632','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ca60289f-53aa-43db-5a9f-432bf40aeb00/public',37),(189,'2023-08-09 16:08:09.973775','2023-08-09 16:08:09.973817','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ef7a4c6d-556a-4506-f555-27a4f9ca8100/public',37),(190,'2023-08-09 16:08:09.978864','2023-08-17 04:50:10.581392','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ca60289f-53aa-43db-5a9f-432bf40aeb00/public',37),(191,'2023-08-09 16:08:09.983166','2023-08-09 16:08:09.983209','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/ef7a4c6d-556a-4506-f555-27a4f9ca8100/public',37),(192,'2023-08-09 16:11:12.445401','2023-08-09 16:11:12.445443','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6ace3738-43e8-4acf-4b00-00245bf6d400/public',38),(193,'2023-08-09 16:11:12.450334','2023-08-17 04:52:00.238610','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/17be5ba9-ae99-4ced-d744-03c26749f000/public',38),(194,'2023-08-09 16:11:12.454567','2023-08-17 04:52:17.832421','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/731bd38d-251a-4664-a6a9-fd82b4585300/public',38),(195,'2023-08-09 16:11:12.458840','2023-08-09 16:11:12.458880','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6ace3738-43e8-4acf-4b00-00245bf6d400/public',38),(196,'2023-08-09 16:11:12.463958','2023-08-17 04:52:30.731107','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/731bd38d-251a-4664-a6a9-fd82b4585300/public',38),(197,'2023-08-10 12:41:39.595532','2023-08-10 12:41:39.595578','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/d1ea12b2-7bee-4819-d118-97b86be16400/public',39),(198,'2023-08-10 12:41:39.599425','2023-08-10 12:41:39.599465','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/6bbff98d-c48c-460f-affb-3613007dfe00/public',39),(199,'2023-08-10 12:41:39.603026','2023-08-10 12:41:39.603065','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/a887e1ef-eb0f-4708-4f7d-b7938058ab00/public',39),(200,'2023-08-10 12:41:39.606613','2023-08-10 12:41:39.606649','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/9675404f-d47e-4a45-17d7-24023a910600/public',39),(201,'2023-08-10 12:41:39.610203','2023-08-10 12:41:39.610238','https://imagedelivery.net/1s092Kgpn1nbxBESmZNkpg/4c30238c-1c92-467a-a84b-738724ab6b00/public',39);
/*!40000 ALTER TABLE `photos_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_itemstatsdaily`
--

DROP TABLE IF EXISTS `stats_itemstatsdaily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_itemstatsdaily` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `total_daily_items` int NOT NULL,
  `nego_selected_items` int NOT NULL,
  `avg_selected_days_to_sell` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_itemstatsdaily`
--

LOCK TABLES `stats_itemstatsdaily` WRITE;
/*!40000 ALTER TABLE `stats_itemstatsdaily` DISABLE KEYS */;
INSERT INTO `stats_itemstatsdaily` VALUES (1,'2023-08-03 02:00:03.818596','2023-08-03 02:00:03.818642',1,0,14),(2,'2023-08-11 02:00:02.948894','2023-08-11 02:00:02.948936',13,9,23);
/*!40000 ALTER TABLE `stats_itemstatsdaily` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchcategory`
--

DROP TABLE IF EXISTS `stats_searchcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchcategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchcategory`
--

LOCK TABLES `stats_searchcategory` WRITE;
/*!40000 ALTER TABLE `stats_searchcategory` DISABLE KEYS */;
INSERT INTO `stats_searchcategory` VALUES (1,'쇼케이스'),(2,'가스레인지/인덕션'),(3,'기타'),(4,'가구'),(5,'세척기'),(6,'냉장고/냉동고'),(7,'포장기계'),(8,'커피머신');
/*!40000 ALTER TABLE `stats_searchcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchlocation`
--

DROP TABLE IF EXISTS `stats_searchlocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchlocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `location` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchlocation`
--

LOCK TABLES `stats_searchlocation` WRITE;
/*!40000 ALTER TABLE `stats_searchlocation` DISABLE KEYS */;
INSERT INTO `stats_searchlocation` VALUES (1,'마포구'),(2,'서대문구'),(3,'영등포구'),(4,'강남구'),(5,'도봉구');
/*!40000 ALTER TABLE `stats_searchlocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchstats`
--

DROP TABLE IF EXISTS `stats_searchstats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchstats` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` longtext NOT NULL,
  `searched_keyword` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchstats`
--

LOCK TABLES `stats_searchstats` WRITE;
/*!40000 ALTER TABLE `stats_searchstats` DISABLE KEYS */;
INSERT INTO `stats_searchstats` VALUES (1,'2023-08-02 05:30:00.671976','2023-08-02 05:30:01.557715','0EAimXI713deuRi3h3rIgiFvCyx1',''),(2,'2023-08-09 12:21:43.682867','2023-08-09 12:21:43.740612','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(3,'2023-08-09 12:21:54.829228','2023-08-09 12:21:54.905301','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(4,'2023-08-09 12:22:10.295765','2023-08-09 12:22:10.329282','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(5,'2023-08-10 04:25:33.848654','2023-08-10 04:25:33.883121','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(6,'2023-08-10 08:46:42.772195','2023-08-10 08:46:42.793736','Y3K1mkgOedQWwRd9dW6PiZzsLM62','불판'),(7,'2023-08-10 08:46:47.661313','2023-08-10 08:46:47.669984','Y3K1mkgOedQWwRd9dW6PiZzsLM62','세척기'),(8,'2023-08-10 11:41:57.989019','2023-08-10 11:41:58.037304','Y3K1mkgOedQWwRd9dW6PiZzsLM62',''),(9,'2023-08-10 11:42:11.923460','2023-08-10 11:42:11.986559','Y3K1mkgOedQWwRd9dW6PiZzsLM62',''),(10,'2023-08-10 11:42:15.218106','2023-08-10 11:42:15.293952','Y3K1mkgOedQWwRd9dW6PiZzsLM62',''),(11,'2023-08-11 08:58:14.195561','2023-08-11 08:58:14.250464','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(12,'2023-08-11 13:00:44.859276','2023-08-11 13:00:44.910108','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(13,'2023-08-11 13:01:03.153841','2023-08-11 13:01:03.214147','b5t3QSplAfY62o00Wt2I3o8ojSt1',''),(14,'2023-08-13 02:12:52.902914','2023-08-13 02:12:53.079070','11tujIZf4QWmzlID8y9oUvSvWT42',''),(15,'2023-08-13 02:13:17.058543','2023-08-13 02:13:17.106121','11tujIZf4QWmzlID8y9oUvSvWT42',''),(16,'2023-08-13 14:57:25.596617','2023-08-13 14:57:25.659765','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',''),(17,'2023-08-13 14:57:28.021852','2023-08-13 14:57:28.083753','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',''),(18,'2023-08-13 14:57:40.566725','2023-08-13 14:57:40.648513','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',''),(19,'2023-08-13 14:57:45.734063','2023-08-13 14:57:45.800709','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',''),(20,'2023-08-17 03:18:59.508741','2023-08-17 03:18:59.521921','YffrXPieCvgV2cQAn2HPkFTyhMJ3','우성');
/*!40000 ALTER TABLE `stats_searchstats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchstats_searched_categories`
--

DROP TABLE IF EXISTS `stats_searchstats_searched_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchstats_searched_categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `searchstats_id` bigint NOT NULL,
  `searchcategory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stats_searchstats_search_searchstats_id_searchcat_fd871a9c_uniq` (`searchstats_id`,`searchcategory_id`),
  KEY `stats_searchstats_se_searchcategory_id_65fdb203_fk_stats_sea` (`searchcategory_id`),
  CONSTRAINT `stats_searchstats_se_searchcategory_id_65fdb203_fk_stats_sea` FOREIGN KEY (`searchcategory_id`) REFERENCES `stats_searchcategory` (`id`),
  CONSTRAINT `stats_searchstats_se_searchstats_id_be6899af_fk_stats_sea` FOREIGN KEY (`searchstats_id`) REFERENCES `stats_searchstats` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchstats_searched_categories`
--

LOCK TABLES `stats_searchstats_searched_categories` WRITE;
/*!40000 ALTER TABLE `stats_searchstats_searched_categories` DISABLE KEYS */;
INSERT INTO `stats_searchstats_searched_categories` VALUES (1,1,1),(2,1,2),(3,2,3),(5,3,3),(4,3,4),(6,4,4),(7,5,3),(8,8,5),(10,9,5),(9,9,6),(12,10,1),(13,10,5),(11,10,6),(14,11,3),(15,12,4),(17,13,4),(16,13,6),(18,15,7),(19,18,8),(20,19,8);
/*!40000 ALTER TABLE `stats_searchstats_searched_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchstats_searched_locations`
--

DROP TABLE IF EXISTS `stats_searchstats_searched_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchstats_searched_locations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `searchstats_id` bigint NOT NULL,
  `searchlocation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stats_searchstats_search_searchstats_id_searchloc_a2ed730b_uniq` (`searchstats_id`,`searchlocation_id`),
  KEY `stats_searchstats_se_searchlocation_id_460aa8ba_fk_stats_sea` (`searchlocation_id`),
  CONSTRAINT `stats_searchstats_se_searchlocation_id_460aa8ba_fk_stats_sea` FOREIGN KEY (`searchlocation_id`) REFERENCES `stats_searchlocation` (`id`),
  CONSTRAINT `stats_searchstats_se_searchstats_id_4fe65ff2_fk_stats_sea` FOREIGN KEY (`searchstats_id`) REFERENCES `stats_searchstats` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchstats_searched_locations`
--

LOCK TABLES `stats_searchstats_searched_locations` WRITE;
/*!40000 ALTER TABLE `stats_searchstats_searched_locations` DISABLE KEYS */;
INSERT INTO `stats_searchstats_searched_locations` VALUES (1,14,1),(2,14,2),(3,14,3),(4,16,4),(5,17,4),(6,17,5),(7,18,4),(8,18,5),(9,19,4),(10,19,5);
/*!40000 ALTER TABLE `stats_searchstats_searched_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchstats_searched_used_years`
--

DROP TABLE IF EXISTS `stats_searchstats_searched_used_years`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchstats_searched_used_years` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `searchstats_id` bigint NOT NULL,
  `searchusedyears_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stats_searchstats_search_searchstats_id_searchuse_3a9033e2_uniq` (`searchstats_id`,`searchusedyears_id`),
  KEY `stats_searchstats_se_searchusedyears_id_332ddd8f_fk_stats_sea` (`searchusedyears_id`),
  CONSTRAINT `stats_searchstats_se_searchstats_id_239bcb4a_fk_stats_sea` FOREIGN KEY (`searchstats_id`) REFERENCES `stats_searchstats` (`id`),
  CONSTRAINT `stats_searchstats_se_searchusedyears_id_332ddd8f_fk_stats_sea` FOREIGN KEY (`searchusedyears_id`) REFERENCES `stats_searchusedyears` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchstats_searched_used_years`
--

LOCK TABLES `stats_searchstats_searched_used_years` WRITE;
/*!40000 ALTER TABLE `stats_searchstats_searched_used_years` DISABLE KEYS */;
/*!40000 ALTER TABLE `stats_searchstats_searched_used_years` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_searchusedyears`
--

DROP TABLE IF EXISTS `stats_searchusedyears`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_searchusedyears` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `used_years` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_searchusedyears`
--

LOCK TABLES `stats_searchusedyears` WRITE;
/*!40000 ALTER TABLE `stats_searchusedyears` DISABLE KEYS */;
/*!40000 ALTER TABLE `stats_searchusedyears` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlists_wishlist`
--

DROP TABLE IF EXISTS `wishlists_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlists_wishlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` longtext NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlists_wishlist`
--

LOCK TABLES `wishlists_wishlist` WRITE;
/*!40000 ALTER TABLE `wishlists_wishlist` DISABLE KEYS */;
INSERT INTO `wishlists_wishlist` VALUES (1,'2023-07-03 07:07:37.685427','2023-07-03 07:07:37.685499','lePr0jQPSgOSLL3aU7KJ6XwpEYp2',NULL),(2,'2023-07-04 02:53:47.728121','2023-07-04 02:53:47.728261','YffrXPieCvgV2cQAn2HPkFTyhMJ3',NULL),(3,'2023-07-06 01:07:06.247495','2023-07-06 01:07:06.247606','D439KIogxNfyaUOvmklBnw8ysJX2',NULL),(4,'2023-07-06 05:08:51.581001','2023-07-06 05:08:51.581171','JNtZRuKGjSRyxJNRkX5GmSvRUYA3',NULL),(5,'2023-07-15 02:54:07.034282','2023-07-15 02:54:07.034449','1EHft4nUyZg7aK3qrNtkWVNIoKW2',NULL),(6,'2023-07-22 00:59:44.411044','2023-07-22 00:59:44.411108','fB0vVScdshZphLChk6UQ6fesBqi2',NULL),(7,'2023-07-26 09:14:24.817399','2023-07-26 09:14:24.817482','0EAimXI713deuRi3h3rIgiFvCyx1',NULL),(8,'2023-07-28 11:07:28.117226','2023-07-28 11:07:28.117282','01ir5tmnTiYpbEWZv5NUqXzr2Ch2',NULL),(9,'2023-07-29 10:12:29.717714','2023-07-29 10:12:29.717788','YKhQGp0zyEMBEuOyTHJk5V1kNQu1',NULL),(10,'2023-08-06 10:02:12.629956','2023-08-06 10:02:12.630070','EdPP969IQlRC04l1uPPUucGs5I52',NULL),(11,'2023-08-12 07:28:04.349334','2023-08-12 07:28:04.349464','55TRDdtgQ9YqmcYjBW85g0pUAfv1',NULL),(12,'2023-08-18 10:38:06.360815','2023-08-18 10:38:06.361027','qzZZVpx7VeTcuxszrg7XNLrIkUt2',NULL);
/*!40000 ALTER TABLE `wishlists_wishlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlists_wishlist_items`
--

DROP TABLE IF EXISTS `wishlists_wishlist_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlists_wishlist_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `wishlist_id` bigint NOT NULL,
  `item_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wishlists_wishlist_items_wishlist_id_item_id_721cf210_uniq` (`wishlist_id`,`item_id`),
  KEY `wishlists_wishlist_items_item_id_28621fd2_fk_items_item_id` (`item_id`),
  CONSTRAINT `wishlists_wishlist_i_wishlist_id_a23bc569_fk_wishlists` FOREIGN KEY (`wishlist_id`) REFERENCES `wishlists_wishlist` (`id`),
  CONSTRAINT `wishlists_wishlist_items_item_id_28621fd2_fk_items_item_id` FOREIGN KEY (`item_id`) REFERENCES `items_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlists_wishlist_items`
--

LOCK TABLES `wishlists_wishlist_items` WRITE;
/*!40000 ALTER TABLE `wishlists_wishlist_items` DISABLE KEYS */;
INSERT INTO `wishlists_wishlist_items` VALUES (16,3,1),(43,3,39),(28,7,1),(17,7,2),(27,7,3),(26,7,6),(24,7,9),(23,7,10),(20,7,11),(19,7,12),(18,7,13),(22,7,14),(21,7,15),(15,8,1),(5,8,2),(14,8,3),(13,8,6),(12,8,7),(9,8,9),(8,8,10),(7,8,11),(6,8,12),(4,8,13),(11,8,14),(10,8,15),(41,9,6),(42,9,7),(30,9,11),(2,9,13),(1,9,14),(37,9,27),(38,9,28),(36,9,29),(39,9,30),(40,9,31),(29,9,32),(35,9,33),(33,9,34),(34,9,35),(31,9,38),(32,9,39);
/*!40000 ALTER TABLE `wishlists_wishlist_items` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-22  4:15:40
