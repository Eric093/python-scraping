# Version avec gestion des deux erreurs: url + fichier
# Renvoie toujours none quelle que soit l'erreur


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.conanauction.fr/")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("div", {"class":"entry-title"})
for name in nameList:
    print(name.get_text())