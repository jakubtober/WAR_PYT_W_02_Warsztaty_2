-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: workshop_2
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

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
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_user` int(11) NOT NULL,
  `to_user` int(11) NOT NULL,
  `text` text,
  `creation_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `to_user` (`to_user`),
  CONSTRAINT `Messages_ibfk_1` FOREIGN KEY (`to_user`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` VALUES (1,17,18,'Nowa wiadomosc tekstowa','2017-11-29'),(2,17,18,'Druga wiadomosc tekstowa','2017-11-29'),(3,18,17,'Druga wiadomosc tekstowa','2017-11-29'),(4,17,18,'przykladowy','2017-12-01'),(5,17,19,'wiadomosc od Mariana','2017-12-01'),(6,19,20,'wiadomosc prywatna od test2@gmail.com','2017-12-01'),(7,18,17,'Wiadomosc od test@gmail.com do Mariana','2017-12-01'),(8,18,22,'czesc Goha, co u ciebie','2017-12-01');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (17,'kowalski.marian@gmail.com','kowalski.marian@gmail.com','vIuf35gdJCcI7r4x5f07a998360780ad2396c390413a9e9e8119d94c402a65c433223356099f60fd'),(18,'test@gmail.com','test@gmail.com','2PRdHABSvVtchNkU7a8c7f974101395233cfebe118a9cccf15e1e6897d591e0d0258f2178d234eab'),(19,'test2@gmail.com','test2@gmail.com','vrSacVJPNRY95D5g3da1c89e9d10c89f982ac0622df35bc5224b725ccdc386073df611ffc312fa9c'),(20,'test3@gmail.com','test3@gmail.com','gB6QUhDAtaw4Aoonbcb8986d8da9753f05babf5878d9d16c75d47f335b9a009020b4f579f0cd348b'),(22,'goha@yahoo.pl','goha@yahoo.pl','DoY8003iQvnZ5QCg2827ac85843de4f0dc739978c99249f0360e8af57f263a5d2419e631301d0db6');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-02  8:53:42
