import mysql.connector, os, json, glob, shutil

print("Connecting to database ...")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@hmadou",
  db = 'covid_19'
)

cursor = mydb.cursor()

print("Connection successful !!!")

# read JSON file which is in the next parent folder
# parse json data to SQL insert

files = glob.glob("json/communiques/*.json")
#files = glob.glob("../json/communiques/*.json")

#print(files)
print("Loading data to database ...")

for file in files :
    json_data=open(file).read()
    json_obj = json.loads(json_data)
   
    for item in json_obj:
        #print(i)
        
        date_com = item["Date_communique"]
        tests = item["numbre_de_Tests"]
        positifs = item["nouveaux_cas"]
        cas_con = item["cas_contact"]
        cas_com = item["cas_communautaire"]
        gueris = item["numbre_de_gueris"]
        deces = item["numbre_de_deces"]
        nom_fichier = item["nom_fichier"]+'.json'
        date_extraction = item["Date_extraction"]
        localites = item["localities"]
        localites = json.dumps(localites)
        #print(localites)
        #print("\n\n")
        #localities = dict()
        
        sql = "INSERT INTO communiques (date_communique,nombre_tests,cas_positifs,cas_contact,cas_communautaire,cas_gueris,nombre_deces,nom_fichier,date_extraction,localites) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (date_com,tests,positifs,cas_con,cas_com,gueris,deces,nom_fichier,date_extraction,localites)
        cursor.execute(sql,val)
        
mydb.commit()

mydb.close()

print("All data loaded successfully to the database!!!")

