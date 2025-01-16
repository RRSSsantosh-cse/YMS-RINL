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
-- Table structure for table `mt`
--

DROP TABLE IF EXISTS `mt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mt` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mid` int NOT NULL,
  `mcode` varchar(30) NOT NULL,
  `mdesc` varchar(30) NOT NULL,
  `aweight` varchar(30) NOT NULL,
  `cweight` varchar(30) NOT NULL,
  `cstock` varchar(30) NOT NULL,
  `ptype` varchar(30) NOT NULL,
  `crt` varchar(30) NOT NULL,
  `dte` date NOT NULL,
  `tm` time(6) NOT NULL,
  `grcode` varchar(30) NOT NULL,
  `grcodedes` varchar(30) NOT NULL,
  `lcode` varchar(30) NOT NULL,
  `lcodedes` varchar(30) NOT NULL,
  `mtype` varchar(30) NOT NULL,
  `scodedes` varchar(30) NOT NULL,
  `seccode` varchar(30) NOT NULL,
  `secodedes` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mt`
--

LOCK TABLES `mt` WRITE;
/*!40000 ALTER TABLE `mt` DISABLE KEYS */;
INSERT INTO `mt` VALUES (1,19911,'611040000','BLOOM 320*250MM WT','1033.261','1029.418','1029.418','furnished','0','2023-06-21','19:49:14.000000','2','2','2','2','2','2','2','2'),(2,19912,'615100700','BLOOM 200*200MM 2830','609.710','505.428','505.428','furnished','0','2023-06-21','19:49:15.000000','2','2','2','2','2','2','2','2'),(3,20187,'451100025130200','ROUND 25MM IS 2062 E250A SBM','N/A','N/A','N/A','furnished','0','2023-06-21','19:53:48.000000','2','2','2','2','2','2','2','2'),(4,19980,'17140656533100','BILLET 65X65 MM SAE1018','N/A','N/A','N/A','furnished','0','2023-06-21','19:50:22.000000','2','2','2','2','2','2','2','2'),(5,19914,'631040000','BLOOM 320*250MM WT','1033.261','1029.418','1029.418','furnished','0','2023-06-21','19:49:14.000000','2','2','2','2','2','2','2','2');
/*!40000 ALTER TABLE `mt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29  2:30:17
