-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: rappilending_dev_db
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'FirstName_test','LastName_test','test@test.com','12345678'),(8,'Test_name','Test_apellido','test@hotmail.com','5f4dcc3b5aa765d61d8327deb882cf99'),(9,'Cristian ','Hurtado Diaz','cristian04.97@hotmail.com','5f4dcc3b5aa765d61d8327deb882cf99'),(11,'FirstName_test','LastName_test','test_@test.com','12345678'),(14,'FirstName_test','LastName_test','ojdsov@email.com','12345678'),(15,'FirstName_test','LastName_test','jlgrpy@email.com','12345678'),(16,'FirstName_test','LastName_test','jxhhgz@email.com','12345678'),(17,'FirstName_test','LastName_test','ktcymn@email.com','12345678'),(18,'FirstName_test','LastName_test','dsyhjs@email.com','12345678'),(19,'FirstName_test','LastName_test','snfrii@email.com','12345678'),(20,'FirstName_test','LastName_test','lsjhyx@email.com','12345678'),(21,'FirstName_test','LastName_test','fylawa@email.com','12345678'),(22,'FirstName_test','LastName_test','qjhpgx@email.com','12345678'),(23,'FirstName_test','LastName_test','imfphh@email.com','12345678'),(24,'FirstName_test','LastName_test','lneeme@email.com','12345678'),(25,'FirstName_test','LastName_test','rooxbu@email.com','12345678'),(26,'FirstName_test','LastName_test','cyqipz@email.com','12345678'),(27,'FirstName_test','LastName_test','xbheui@email.com','12345678'),(28,'FirstName_test','LastName_test','aehcsw@email.com','12345678'),(29,'FirstName_test','LastName_test','clpolw@email.com','12345678'),(30,'FirstName_test','LastName_test','anwqjd@email.com','12345678'),(31,'FirstName_test','LastName_test','eqruwc@email.com','12345678'),(32,'FirstName_test','LastName_test','gmtfso@email.com','12345678'),(33,'FirstName_test','LastName_test','njoytz@email.com','12345678'),(34,'FirstName_test','LastName_test','lmnpiy@email.com','12345678'),(35,'FirstName_test','LastName_test','loasss@email.com','12345678'),(36,'FirstName_test','LastName_test','jglvhh@email.com','12345678'),(37,'FirstName_test','LastName_test','gmrizw@email.com','12345678'),(38,'FirstName_test','LastName_test','obeqci@email.com','12345678'),(39,'FirstName_test','LastName_test','smmrpd@email.com','12345678'),(40,'FirstName_test','LastName_test','mqlclq@email.com','12345678'),(41,'FirstName_test','LastName_test','knfnkp@email.com','12345678'),(42,'FirstName_test','LastName_test','ydvvpw@email.com','12345678'),(43,'FirstName_test','LastName_test','dwpemc@email.com','12345678'),(44,'FirstName_test','LastName_test','wrnanj@email.com','12345678'),(45,'FirstName_test','LastName_test','cmromg@email.com','12345678'),(46,'FirstName_test','LastName_test','etnoxx@email.com','12345678'),(47,'FirstName_test','LastName_test','aghmjs@email.com','12345678'),(48,'FirstName_test','LastName_test','tvshkq@email.com','12345678'),(49,'FirstName_test','LastName_test','dpkeqo@email.com','12345678'),(50,'FirstName_test','LastName_test','qnjdgc@email.com','12345678'),(51,'FirstName_test','LastName_test','mhbszf@email.com','12345678'),(52,'FirstName_test','LastName_test','elpxiy@email.com','12345678'),(53,'FirstName_test','LastName_test','wpggkm@email.com','12345678'),(54,'FirstName_test','LastName_test','krngho@email.com','12345678'),(55,'FirstName_test','LastName_test','osrxgw@email.com','12345678'),(56,'FirstName_test','LastName_test','ajihyh@email.com','12345678'),(57,'FirstName_test','LastName_test','lgzsff@email.com','12345678'),(58,'FirstName_test','LastName_test','tmfqzv@email.com','12345678'),(59,'FirstName_test','LastName_test','mvsrpz@email.com','12345678'),(60,'FirstName_test','LastName_test','jcbajv@email.com','12345678'),(61,'FirstName_test','LastName_test','mndqgr@email.com','12345678'),(62,'FirstName_test','LastName_test','usezhj@email.com','12345678'),(63,'FirstName_test','LastName_test','wvfsjs@email.com','12345678'),(64,'FirstName_test','LastName_test','gznxal@email.com','12345678'),(65,'FirstName_test','LastName_test','fpohwo@email.com','12345678'),(66,'FirstName_test','LastName_test','lizetu@email.com','12345678'),(67,'FirstName_test','LastName_test','izffla@email.com','12345678'),(68,'FirstName_test','LastName_test','yjgbsl@email.com','12345678'),(69,'FirstName_test','LastName_test','cfboso@email.com','12345678'),(70,'FirstName_test','LastName_test','kebjyl@email.com','12345678'),(71,'FirstName_test','LastName_test','wtjnog@email.com','12345678'),(72,'FirstName_test','LastName_test','vllpjm@email.com','12345678'),(73,'FirstName_test','LastName_test','xudygq@email.com','12345678'),(74,'FirstName_test','LastName_test','snlzil@email.com','12345678'),(75,'FirstName_test','LastName_test','reiqnm@email.com','12345678'),(76,'FirstName_test','LastName_test','xvulsj@email.com','12345678'),(77,'FirstName_test','LastName_test','nzyylm@email.com','12345678'),(78,'FirstName_test','LastName_test','uxpyje@email.com','12345678');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-02 20:59:12
