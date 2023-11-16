# Version avec gestion des deux erreurs: url + fichier
# Renvoie toujours none quelle que soit l'erreur

import logging

from urllib.error import HTTPError
from urllib.error import URLError

# Paramétrage des logs -------------------------
from logging.handlers import RotatingFileHandler
logging.basicConfig(filename='log/programlog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
# ----------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    # Gestion des erreurs de connexion
    try:
        html = urlopen(url)

    except HTTPError as e:
        print(e, "- File not exist")
        return None

    except URLError as e:
        print("URL Error - The server could not be found!")
        return None

    # Scrapper
    try:
        html = urlopen("https://www.conanauction.fr/resultats-des-ventes?year=2021&tab=tab2#tj_container_nbre")  # A retoucher (getTitle url présent plus bas)
        bsObj = BeautifulSoup(html, "html.parser")

        ##### Test pour n'avoir que le calendrier
        # nameList = bsObj.findAll("div", {"class":"entry-title"})
        nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"})
        #nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"}).get("href")
        ######## Avec get href ne renvoie rien ? ajouter un find a ?


        for name in nameList:
            print(name.get_text())
            if 'href' in name.attrs :
                print(name.get_url())
            
            
    except AttributeError as e:
        return None
    #return title

title=getTitle("https://www.conanauction.fr/")