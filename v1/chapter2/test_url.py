from bs4 import BeautifulSoup
import requests

# r=requests.get("https://proxyway.com/reviews/smartproxy-proxies")
r=requests.get("https://www.conanauction.fr/calendrier")

soup=BeautifulSoup(r.content,"html.parser")

a_href=soup.find("div",{"class":"entry-title"}).get("href")

print(a_href)

