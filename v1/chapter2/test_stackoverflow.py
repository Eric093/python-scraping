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

</div>
<div class="elementList" style="padding-top: 10px;">
<div class="left" style="width: 75%;">
<a class="leftAlignedImage" href="/book/show/2784.Ways_of_Seeing" title="Ways of Seeing"><img alt="Ways of Seeing" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1464018308l/2784._SY75_.jpg"/></a>
<a class="bookTitle" href="/book/show/2784.Ways_of_Seeing">Ways of Seeing (Paperback)</a>
<br/>
<span class="by">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<div class="authorName__container">
<a class="authorName" href="https://www.goodreads.com/author/show/29919.John_Berger" itemprop="url"><span itemprop="name">John Berger</span></a>
</div>

'''

soup = BeautifulSoup(html_code, 'html.parser')
tag = soup.find('a', {'class':'bookTitle'})

# - Book Title -
title = tag.text 
print(title)

# - Href Link -
href = tag.get('href')
print(href) 
