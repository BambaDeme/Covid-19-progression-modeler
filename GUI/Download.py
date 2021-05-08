from PIL import Image
import DataExtractor

import cv2

import twint
import requests
import nest_asyncio
import json

import datetime


#images = ["images/ExzMcvDWgAYWkNg.jpeg","images/ExzMeVeXAAsNmS5.jpeg"]

def extractor(images,date):
    # initialize empty  text
    text = ''

    # Extraire le text des images
    for image in images:
        text += DataExtractor.getText(image)
    text = text.lower()

    
    # obtenir le nombre de tests
    tests = DataExtractor.getTests(text)
    text = text[tests["endIndex"]:-1]
    numbers = tests['numbers']
    tests_realises = numbers['tests']
    cas_positifs = numbers['positifs']
    taux = numbers['taux']

    #print(tests)

    # les cas contact
    contacts = DataExtractor.getCasContact(text)
    text = text[contacts["endIndex"] :-1]
    cas_contact = contacts['number']
    #print(contacts)

    # les cas importes
    #cas_importes = DataExtractor.getcasImportes(text)
    #print("cas_importes: ",cas_importes)

    # les cas communautaires
    cas_com = DataExtractor.getCasCom(text)
    text = text[cas_com["endIndex"] :-1]
    cas_coms = cas_com['number']
    #print(cas_com)

    # Truncate text to listing of cases per city
    try:
        text = text[text.index("comme suit")+12:]
    except:
        try:
            text = text[text.index(":")+1:-1]
        except:
            print('Unable to Gather More Information!')
    #print(text)

    # get and print array of location and there number of cases
    cas = DataExtractor.getCityCases(text)
    text = text[cas["endIndex"] :-1]

    #print(cas)
    #print(DataExtractor.getNbGueris(text))
    nombre_gueris = int(DataExtractor.getNbGueris(text))
    #nombre_gueris = DataExtractor.getNbGueris(text)
    #print("cas gueris ",nombre_gueris)
    nombre_deces = int(DataExtractor.getDeces(text))
    #print("deces: ",nombre_deces)

    total = DataExtractor.getOverall(text)
    
    #print(total)

    cases = DataExtractor.exportIntoJson(cas["cas"])
    #print(cases)
    DataExtractor.exportToFile(date,tests_realises,cas_positifs,cas_contact,cas_coms,nombre_gueris,nombre_deces,cases)

def downloader():
    nest_asyncio.apply()

    config = twint.Config()
    config.Username = "MinisteredelaS1"
    config.Search = "Communiqué"
    config.hashtags = "Cov19sn"
    #config.Since = "2021-05-03"
    config.Store_object = True
    config.Store_json = True
    config.Images = True
    config.Output = "communiques.json" 
    twint.run.Search(config)

    tweets = []

    for line in open('communiques.json', 'r'):
        
        i=1
        tweet = json.loads(line)
        urls = tweet["photos"]
        date = tweet["date"]

        images=[]
        for url in urls:
            nom = url.split("/")
            nom = nom[len(nom)-1]
            response = requests.get(url)
            
            with open("../images/"+nom, "wb") as f:
                f.write(response.content)
            images.append("../images/"+nom)
        print(images)
        extractor(images,date)



# fonction qui vérifie si une date existe dans les communiqués
def findDate(date):
    for line in open("communiques.json","r"):
        tweet = json.loads(line)
        if tweet["date"] == str(date):
            return True
    return False

"""
date = datetime.date.today()
#print(date)
#print(date - datetime.timedelta(1))
up_do_date = False
try:
    for line in open('communiques.json', 'r'):
        tweet = json.loads(line)
        #on verifie si les communiques du jour ont été téléchargés
        # si c'est le cas l'extraction aussi a été fait
        # Donc tout est à jour plus de téléchargement ou d'extraction à faire
        if findDate(str(datetime.date.today())):
            up_do_date = True
            break;
except IOError:
    print("Downloading and extracting all tweets...!")
    downloader()
else:
    if up_do_date:
        print("All tweets have already been downloaded and extracted !!!")
        print("everything is up to date")
    else:
        date = date - datetime.timedelta(1)
        loop = 1

        while(findDate(date)==False and loop<1000):
            date = date - datetime.timedelta(1)
            loop+=1
        print("last dowloaded tweet date: ",date)
        print("Dowloading and extracting new tweets since: ",date)
        
"""





