
CREATE DATABASE IF NOT EXISTS `covid_19`;
use 'covid_19';
CREATE TABLE `communiques` (
  `id_communique` int(11) NOT NULL,
  `date_communique` date NOT NULL,
  `nombre_tests` int(11) NOT NULL,
  `cas_positifs` int(11) NOT NULL,
  `cas_contact` int(11) NOT NULL,
  `cas_communautaire` int(11) NOT NULL,
  `cas_impotes` int(11) ,
  `cas_gueris` int(11) NOT NULL,
  `nombre_deces` int(11) NOT NULL,
  `nom_fichier` varchar(255) NOT NULL,
  `date_extraction` varchar(255) NOT NULL,
  `localites` json 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE `communiques`
  ADD PRIMARY KEY (`id_communique`);


ALTER TABLE `communiques`
  MODIFY `id_communique` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;


