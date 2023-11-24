""" from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import html


url = 'https://www.goodreads.com/shelf/show/art/gendersBooks.html'

html_source = requests.get(url).content 

soup = BeautifulSoup(html, 'html.parser')

# - To get the tag that we want -
tag = soup.find('a', {'class' : 'booktitle'})

# - Extract Book Title -
href = tag.text

# - Extract href from Tag -
title = tag.get('href') """
#---------------------------------------------------
from bs4 import BeautifulSoup 

html_code = '''

<div class="entry-title">
<h2>
<a href="/catalogue/146788-vip-very-important-perriand">VIP - Very Important Perriand</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/146849-vente-asie-classique-or-vente-sur-designation">VENTE ASIE - CLASSIQUE - OR - VENTE SUR DESIGNATION</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/146525-grands-vins-vente-dune-partie-de-la-cave-du-restaurant-leon-de-lyon-en-presence-de-laurent-gerra">GRANDS VINS - VENTE D'UNE PARTIE DE LA CAVE DU RESTAURANT LEON DE LYON - EN PRESENCE DE LAURENT GERRA</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/145530-mobilier-et-objets-dart-arts-populaires-asie">MOBILIER ET OBJETS D’ART - ARTS POPULAIRES - ASIE</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/146210-gravures-tableaux-anciens-tableaux-modernes-et-contemporains">GRAVURES - TABLEAUX ANCIENS - TABLEAUX MODERNES ET CONTEMPORAINS</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/147052-bijoux-et-montres">BIJOUX ET MONTRES </a>
</h2>
</div>, <div class="entry-title">
<h2>
<a href="/catalogue/146211-mode-et-vintage-hermes-chanel-yves-saintlaurent-louis-vuitton-">MODE ET VINTAGE : Hermès - Chanel - Yves Saint-Laurent - Louis Vuitton ...</a>
</h2>
</div>, <div class="entry-title">
<h2>
<a class="cataPasDispo" href="/vente/137976-livres-anciens-et-modernes">LIVRES ANCIENS ET MODERNES</a>
</h2>
</div>

'''

soup = BeautifulSoup(html_code, 'html.parser')
nameList = soup.findAll('a')


# title = tag.text 
# print(title)

# - Href Link -
# href = tag.get('href')
# print(href) 

for name in nameList:
            print(name.get_text())
            # print(name['href'])
            href = name.get('href')
            print(href) 
            
            #if 'href' in name.attrs :
             #   print(name.get_url())