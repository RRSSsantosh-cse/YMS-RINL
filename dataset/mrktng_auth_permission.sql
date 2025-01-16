-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: mrktng
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add hook',7,'add_hook'),(26,'Can change hook',7,'change_hook'),(27,'Can delete hook',7,'delete_hook'),(28,'Can view hook',7,'view_hook'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add wagon',9,'add_wagon'),(34,'Can change wagon',9,'change_wagon'),(35,'Can delete wagon',9,'delete_wagon'),(36,'Can view wagon',9,'view_wagon'),(37,'Can add workorder',10,'add_workorder'),(38,'Can change workorder',10,'change_workorder'),(39,'Can delete workorder',10,'delete_workorder'),(40,'Can view workorder',10,'view_workorder'),(41,'Can add wrk',11,'add_wrk'),(42,'Can change wrk',11,'change_wrk'),(43,'Can delete wrk',11,'delete_wrk'),(44,'Can view wrk',11,'view_wrk'),(45,'Can add bin',12,'add_bin'),(46,'Can change bin',12,'change_bin'),(47,'Can delete bin',12,'delete_bin'),(48,'Can view bin',12,'view_bin'),(49,'Can add bund',13,'add_bund'),(50,'Can change bund',13,'change_bund'),(51,'Can delete bund',13,'delete_bund'),(52,'Can view bund',13,'view_bund'),(53,'Can add device',14,'add_device'),(54,'Can change device',14,'change_device'),(55,'Can delete device',14,'delete_device'),(56,'Can view device',14,'view_device'),(57,'Can add dispatch',15,'add_dispatch'),(58,'Can change dispatch',15,'change_dispatch'),(59,'Can delete dispatch',15,'delete_dispatch'),(60,'Can view dispatch',15,'view_dispatch'),(61,'Can add fin',16,'add_fin'),(62,'Can change fin',16,'change_fin'),(63,'Can delete fin',16,'delete_fin'),(64,'Can view fin',16,'view_fin'),(65,'Can add gps',17,'add_gps'),(66,'Can change gps',17,'change_gps'),(67,'Can delete gps',17,'delete_gps'),(68,'Can view gps',17,'view_gps'),(69,'Can add inb',18,'add_inb'),(70,'Can change inb',18,'change_inb'),(71,'Can delete inb',18,'delete_inb'),(72,'Can view inb',18,'view_inb'),(73,'Can add inboundtruck',19,'add_inboundtruck'),(74,'Can change inboundtruck',19,'change_inboundtruck'),(75,'Can delete inboundtruck',19,'delete_inboundtruck'),(76,'Can view inboundtruck',19,'view_inboundtruck'),(77,'Can add loc',20,'add_loc'),(78,'Can change loc',20,'change_loc'),(79,'Can delete loc',20,'delete_loc'),(80,'Can view loc',20,'view_loc'),(81,'Can add master',21,'add_master'),(82,'Can change master',21,'change_master'),(83,'Can delete master',21,'delete_master'),(84,'Can view master',21,'view_master'),(85,'Can add material',22,'add_material'),(86,'Can change material',22,'change_material'),(87,'Can delete material',22,'delete_material'),(88,'Can view material',22,'view_material'),(89,'Can add mcode',23,'add_mcode'),(90,'Can change mcode',23,'change_mcode'),(91,'Can delete mcode',23,'delete_mcode'),(92,'Can view mcode',23,'view_mcode'),(93,'Can add mp',24,'add_mp'),(94,'Can change mp',24,'change_mp'),(95,'Can delete mp',24,'delete_mp'),(96,'Can view mp',24,'view_mp'),(97,'Can add rake',25,'add_rake'),(98,'Can change rake',25,'change_rake'),(99,'Can delete rake',25,'delete_rake'),(100,'Can view rake',25,'view_rake'),(101,'Can add rke',26,'add_rke'),(102,'Can change rke',26,'change_rke'),(103,'Can delete rke',26,'delete_rke'),(104,'Can view rke',26,'view_rke'),(105,'Can add truckdispatch',27,'add_truckdispatch'),(106,'Can change truckdispatch',27,'change_truckdispatch'),(107,'Can delete truckdispatch',27,'delete_truckdispatch'),(108,'Can view truckdispatch',27,'view_truckdispatch'),(109,'Can add vehicle',28,'add_vehicle'),(110,'Can change vehicle',28,'change_vehicle'),(111,'Can delete vehicle',28,'delete_vehicle'),(112,'Can view vehicle',28,'view_vehicle'),(113,'Can add wagn',29,'add_wagn'),(114,'Can change wagn',29,'change_wagn'),(115,'Can delete wagn',29,'delete_wagn'),(116,'Can view wagn',29,'view_wagn'),(117,'Can add workoder',30,'add_workoder'),(118,'Can change workoder',30,'change_workoder'),(119,'Can delete workoder',30,'delete_workoder'),(120,'Can view workoder',30,'view_workoder'),(121,'Can add work',31,'add_work'),(122,'Can change work',31,'change_work'),(123,'Can delete work',31,'delete_work'),(124,'Can view work',31,'view_work'),(125,'Can add mt',32,'add_mt'),(126,'Can change mt',32,'change_mt'),(127,'Can delete mt',32,'delete_mt'),(128,'Can view mt',32,'view_mt'),(129,'Can add gen',33,'add_gen'),(130,'Can change gen',33,'change_gen'),(131,'Can delete gen',33,'delete_gen'),(132,'Can view gen',33,'view_gen'),(133,'Can add gn',34,'add_gn'),(134,'Can change gn',34,'change_gn'),(135,'Can delete gn',34,'delete_gn'),(136,'Can view gn',34,'view_gn'),(137,'Can add mark',35,'add_mark'),(138,'Can change mark',35,'change_mark'),(139,'Can delete mark',35,'delete_mark'),(140,'Can view mark',35,'view_mark'),(141,'Can add student',36,'add_student'),(142,'Can change student',36,'change_student'),(143,'Can delete student',36,'delete_student'),(144,'Can view student',36,'view_student'),(145,'Can add compensation',37,'add_compensation'),(146,'Can change compensation',37,'change_compensation'),(147,'Can delete compensation',37,'delete_compensation'),(148,'Can view compensation',37,'view_compensation'),(149,'Can add employee',38,'add_employee'),(150,'Can change employee',38,'change_employee'),(151,'Can delete employee',38,'delete_employee'),(152,'Can view employee',38,'view_employee'),(153,'Can add hero',39,'add_hero'),(154,'Can change hero',39,'change_hero'),(155,'Can delete hero',39,'delete_hero'),(156,'Can view hero',39,'view_hero'),(157,'Can add heo',40,'add_heo'),(158,'Can change heo',40,'change_heo'),(159,'Can delete heo',40,'delete_heo'),(160,'Can view heo',40,'view_heo'),(161,'Can add mtu',41,'add_mtu'),(162,'Can change mtu',41,'change_mtu'),(163,'Can delete mtu',41,'delete_mtu'),(164,'Can view mtu',41,'view_mtu'),(165,'Can add your model',42,'add_yourmodel'),(166,'Can change your model',42,'change_yourmodel'),(167,'Can delete your model',42,'delete_yourmodel'),(168,'Can view your model',42,'view_yourmodel'),(169,'Can add map',43,'add_map'),(170,'Can change map',43,'change_map'),(171,'Can delete map',43,'delete_map'),(172,'Can view map',43,'view_map'),(173,'Can add mseg',44,'add_mseg'),(174,'Can change mseg',44,'change_mseg'),(175,'Can delete mseg',44,'delete_mseg'),(176,'Can view mseg',44,'view_mseg'),(177,'Can add ordstat',45,'add_ordstat'),(178,'Can change ordstat',45,'change_ordstat'),(179,'Can delete ordstat',45,'delete_ordstat'),(180,'Can view ordstat',45,'view_ordstat');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29  2:30:18
