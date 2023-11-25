# Version avec gestion des deux erreurs: url + fichier
# Renvoie toujours none quelle que soit l'erreur

import logging

from urllib.error import HTTPError
from urllib.error import URLError

## Paramétrage des logs -------------------------
from logging.handlers import RotatingFileHandler
logging.basicConfig(filename='log/programlog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
# ----------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    ## Gestion des erreurs de connexion
    try:
        html = urlopen(url)

    except HTTPError as e:
        print(e, "- File not exist")
        return None

    except URLError as e:
        print("URL Error - The server could not be found!")
        return None

    ## Scrapper
    try:
        logging.debug("Demarrage du traitement")

        html = urlopen("https://www.conanauction.fr/calendrier")
        bsObj = BeautifulSoup(html, "html.parser")

        ## BeautifulSoup pour avoir le calendrier
        #  nameList = bsObj.findAll("div", {"class":"entry-title"})
        # nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"})
        # nameList = bsObj.find("div", {"class":"page_calendrier"}.findAll("div", {"class":"entry-title"}).find("a").attrs['href'])
        nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"})#.findAll('a')
        
        #print(nameList)######## OK Sort le contenu total du bsObj !!!!!!
        nameList_String = str(nameList)
        #print(nameList_String)

        ## Nouveau BeautifulSoup pour extraire nom de la vente et url relative
        bsObj2 = BeautifulSoup(str(nameList), "html.parser")
        #html_code = nameList.source
        liste = bsObj2.findAll('a')
        #print(liste)

        for name in liste:#nameList:
            print(name.get_text())
            # print(name['href'])
            href = name.get('href')
            print(href) 

            
            
    except AttributeError as e:
        return None
    #return title

if __name__ == "__main__":
    logging.debug('Demarrage programme ----------------------------')
    
    title=getTitle("https://www.conanauction.fr/")