##searching tags by class and id
from bs4 import BeautifulSoup
import requests
page=requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
#print(page.status_code)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#print(soup)
print(soup.find_all('p',class_='outer-text'))
print(soup.find_all('p',id='first'))
print(soup.find_all(class_='outer-text'))
print(soup.find_all(id='first'))
print(soup.select("div p"))