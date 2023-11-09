from bs4 import BeautifulSoup
import requests

r=requests.get("https://proxyway.com/reviews/smartproxy-proxies")

soup=BeautifulSoup(r.content,"html.parser")

a_href=soup.find("a",{"class":"single-intro__cta"}).get("href")

print(a_href)