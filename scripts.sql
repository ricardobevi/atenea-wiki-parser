delimiter $$

CREATE DATABASE `wiki` /*!40100 DEFAULT CHARACTER SET utf8 */$$


delimiter $$

CREATE TABLE `articulo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titulo` mediumtext,
  `subtitulo` mediumtext,
  `cuerpo` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16383  DEFAULT CHARSET=utf8$$

