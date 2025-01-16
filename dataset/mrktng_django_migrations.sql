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
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-02-09 15:59:05.252518'),(2,'auth','0001_initial','2024-02-09 15:59:06.309504'),(3,'admin','0001_initial','2024-02-09 15:59:06.581744'),(4,'admin','0002_logentry_remove_auto_add','2024-02-09 15:59:06.592292'),(5,'admin','0003_logentry_add_action_flag_choices','2024-02-09 15:59:06.603048'),(6,'contenttypes','0002_remove_content_type_name','2024-02-09 15:59:06.721971'),(7,'auth','0002_alter_permission_name_max_length','2024-02-09 15:59:06.823117'),(8,'auth','0003_alter_user_email_max_length','2024-02-09 15:59:06.849762'),(9,'auth','0004_alter_user_username_opts','2024-02-09 15:59:06.860765'),(10,'auth','0005_alter_user_last_login_null','2024-02-09 15:59:06.944777'),(11,'auth','0006_require_contenttypes_0002','2024-02-09 15:59:06.949617'),(12,'auth','0007_alter_validators_add_error_messages','2024-02-09 15:59:06.961418'),(13,'auth','0008_alter_user_username_max_length','2024-02-09 15:59:07.063607'),(14,'auth','0009_alter_user_last_name_max_length','2024-02-09 15:59:07.165124'),(15,'auth','0010_alter_group_name_max_length','2024-02-09 15:59:07.187354'),(16,'auth','0011_update_proxy_permissions','2024-02-09 15:59:07.200101'),(17,'auth','0012_alter_user_first_name_max_length','2024-02-09 15:59:07.306862'),(18,'cdy','0001_initial','2024-02-09 15:59:07.461610'),(19,'sessions','0001_initial','2024-02-09 15:59:07.513665'),(20,'cdy','0002_delete_wrk','2024-02-09 16:06:06.651701'),(21,'cdy','0003_bin_bund_device_dispatch_fin_gps_inb_inboundtruck_and_more','2024-02-17 12:03:16.354878'),(22,'cdy','0004_alter_gps_gid','2024-02-17 18:14:30.283716'),(23,'cdy','0002_alter_material_aweight_alter_material_crt_and_more','2024-02-22 06:47:18.639143'),(24,'cdy','0002_mt','2024-02-22 07:16:28.785226'),(25,'cdy','0003_alter_master_mcode','2024-02-22 08:42:38.742943'),(26,'cdy','0002_inb_weight','2024-02-24 05:48:29.389341'),(27,'cdy','0003_inb_wag','2024-02-24 05:50:56.289740'),(28,'cdy','0004_remove_inb_wname','2024-02-24 05:52:06.884316'),(29,'cdy','0005_wagn_od','2024-02-24 06:41:00.941569'),(30,'cdy','0006_wagon_od','2024-02-24 06:45:07.667067'),(31,'cdy','0007_remove_rke_val','2024-02-24 08:18:48.385876'),(32,'cdy','0002_mp_mcode','2024-02-24 08:51:02.303031'),(33,'cdy','0003_workoder_ct','2024-02-24 09:05:35.068627'),(34,'cdy','0004_gen','2024-02-25 12:26:12.068498'),(35,'cdy','0005_gn','2024-02-27 06:58:01.790098'),(36,'cdy','0006_remove_gn_name_gn_name','2024-02-27 07:55:36.809321'),(37,'cdy','0007_remove_gen_ge_remove_gn_cat_remove_gn_name_gen_gen_and_more','2024-02-27 10:05:12.789987'),(38,'cdy','0008_student_mark_delete_gen_delete_gn','2024-02-28 04:31:35.820482'),(39,'cdy','0002_heo_remove_hero_ct_remove_hero_mve','2024-03-04 14:20:33.814344'),(40,'cdy','0003_remove_workoder_ct','2024-03-06 05:36:11.135084'),(41,'cdy','0004_mtu','2024-03-07 05:25:30.448752'),(42,'cdy','0005_yourmodel','2024-03-08 17:59:36.315696'),(43,'cdy','0006_hook_uid_wagon_uid','2024-03-23 04:46:33.926461'),(44,'cdy','0007_alter_bund_od_alter_inb_od_alter_inboundtruck_od_and_more','2024-04-04 03:25:28.326418'),(45,'cdy','0008_rake_desti_wagn_sto','2024-04-04 09:16:49.947193'),(46,'cdy','0009_delete_fin_inb_ct_workoder_stat','2024-04-04 09:26:05.927092'),(47,'cdy','0010_rake_rcont','2024-04-04 09:38:38.555840'),(48,'cdy','0011_wagn_uid','2024-04-04 09:41:26.363672'),(49,'cdy','0012_remove_inb_ct','2024-04-06 04:42:43.439868'),(50,'cdy','0013_inb_ct','2024-04-06 05:16:08.733227'),(51,'cdy','0014_remove_inb_wag','2024-04-06 05:25:51.524536'),(52,'cdy','0015_inb_bns','2024-04-06 05:27:11.338013'),(53,'cdy','0016_remove_bund_mtype_remove_bund_wt_inb_tp','2024-04-06 05:49:56.100478'),(54,'cdy','0017_alter_bund_od','2024-04-06 05:53:28.356728'),(55,'cdy','0018_inb_mcode','2024-04-07 17:10:59.150281'),(56,'cdy','0019_alter_inb_mcode','2024-04-07 17:12:59.782530'),(57,'cdy','0020_loc_c1_loc_c2_alter_loc_stat','2024-04-07 18:29:38.471933'),(58,'cdy','0021_user_eid_alter_user_ac_alter_user_val','2024-04-18 03:33:21.507325'),(59,'cdy','0002_user_tme','2024-04-20 09:51:05.373126'),(60,'cdy','0003_map','2024-04-22 19:41:52.631451'),(61,'cdy','0004_mseg','2024-04-23 09:22:28.842993'),(62,'cdy','0005_ordstat_delete_master','2024-04-23 10:59:23.267428'),(63,'cdy','0006_mseg_c','2024-04-23 11:22:24.334382'),(64,'cdy','0007_rake_asgn','2024-04-24 17:37:24.702118'),(65,'cdy','0008_alter_hook_status_alter_hook_platform','2024-04-25 14:20:50.294229'),(66,'cdy','0009_alter_hook_platform','2024-04-25 14:27:09.976173'),(67,'cdy','0010_alter_hook_platform','2024-04-25 14:29:51.408551'),(68,'cdy','0011_mt_grcode_mt_grcodedes_mt_lcode_mt_lcodedes_mt_mtype_and_more','2024-04-26 15:31:38.373374'),(69,'cdy','0012_alter_dispatch_dno','2024-04-26 17:30:19.922946'),(70,'cdy','0013_alter_dispatch_din_alter_dispatch_dq_and_more','2024-04-26 17:44:24.492388'),(71,'cdy','0014_rename_bi_inboundtruck_mdesc_and_more','2024-04-26 21:00:41.774087'),(72,'cdy','0015_remove_inboundtruck_ono','2024-04-26 21:01:59.659326'),(73,'cdy','0016_inboundtruck_nm','2024-04-26 21:03:29.671485'),(74,'cdy','0017_inboundtruck_ono','2024-04-26 21:10:10.649176'),(75,'cdy','0018_dispatch_ono','2024-04-26 21:18:01.260057'),(76,'cdy','0019_remove_hook_status_remove_hook_h_number_and_more','2024-04-26 21:18:39.786442'),(77,'cdy','0020_hook_status_hook_h_number_hook_platform','2024-04-26 21:21:55.973064');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29  2:30:16
