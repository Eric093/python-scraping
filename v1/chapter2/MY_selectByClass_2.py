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
    logging.debug("Demarrage traitement")

    ## Interception des erreurs de connexion ##
    try:
        logging.debug(url)
        html = urlopen(url)

    except HTTPError as e:
        print(e, "- Le fichier n'existe pas")
        logging.debug(e, "- Le fichier n'existe pas")

        return None

    except URLError as e:
        print("Erreur URL - Serveur introuvable !")
        logging.debug("Erreur URL - Serveur introuvable !")
        return None

    ## Scrapper
    try:

        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")

        ## BeautifulSoup pour avoir le calendrier
        nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"})
        
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
            logging.debug(name.get_text())
            # print(name['href'])
            href = name.get('href')
            print(href) 
            logging.debug(href)
            
    ## Gestion des erreurs        
    except AttributeError as e:
        return None
    #return title

if __name__ == "__main__":
    logging.debug('Demarrage programme ----------------------------')
    
    ## URL et repertoire à examiner
    title=getTitle("https://www.conanauction.fr/calendrier")