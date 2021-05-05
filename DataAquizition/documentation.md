Ce module permet de télécharger tous les communiqués relatifs au covid_19 et d'extraire les données.
Pour ce faire on télécharge les tweets du munistère sur le covid grâce au module twint.

Le fichier "main.py" se charge d'aller télécharger les tweets et les images des communiqués puis passe les images 
au module "DataExtractor.py" qui va extraire les données de chaque communiqués et les sauvegarde dans un fichier json avec comme nom 
la date du communiqué

Pour exécuter ce module:
On clone le projet: 
  #git clone https://github.com/BambaDeme/Covid-19-progression-modeler.git
On se place dans le répertoire du projet puis on active l'environnement virtuel: 
  # source env/bin/activate (ou avtive.bash)
Une l'environnement virtuel activé, on peut exécuter lancer le DataAquizition: 
 # python DataAquizition/main.py

Les images des communiqués seront dans le répertoire "images" et les fichiers json contenants
les données extraites seront dans le répertoire "json/communiques"
