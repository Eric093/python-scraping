# Version avec gestion des deux erreurs: url + fichier
# Renvoie toujours none quelle que soit l'erreur

from urllib.error import HTTPError
from urllib.error import URLError

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
        html = urlopen("https://www.conanauction.fr/")  # A retoucher (getTitle url)
        bsObj = BeautifulSoup(html, "html.parser")

        ##### Test pour n'avoir que le calendrier
        # nameList = bsObj.findAll("div", {"class":"entry-title"})
        nameList = bsObj.find("div", {"class":"page_calendrier"}).findAll("div", {"class":"entry-title"})

        for name in nameList:
            print(name.get_text())
            
    except AttributeError as e:
        return None
    #return title

title=getTitle("https://www.conanauction.fr/")