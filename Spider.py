
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://music.163.com/#/discover/playlist")
bs = BeautifulSoup(html.read(),'html.parser')
text_list = bs.find_all('span','nb')
for text in text_list:
    print(text.get_text())
html.close()




