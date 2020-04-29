##https://www.hdwallpapers.in/animals__birds-desktop-wallpapers.html
##/Desktop/18/day10-beautifulsoup/imagesscrapping1/allimages1
##user@sandeep:~/Desktop/18/day10-beautifulsoup/imagesscrapping1/allimages1$ 

import requests
page=requests.get("https://www.hdwallpapers.in/animals__birds-desktop-wallpapers.html")
print(page)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
#print(soup)
#print(soup.prettify())
list1=soup.find_all('div',class_='thumb')
#print(list1)
print(len(list1))
list2=[]
for everyitem in list1:
    list2.append(everyitem.find("img"))
#print(list2)
list3=[]
for everyitem in list2:
    list3.append(everyitem['src'])
print(list3)
urllist=[]
for everyitem in list3:
    urllist.append("https://www.hdwallpapers.in"+everyitem)
print(urllist)
count=1
for everyitem in urllist:
    r2=requests.get(everyitem,stream="True")
    if r2.status_code==200:
        print("downloading................."+everyitem)
        fp=open("/home/user/Desktop/18/day10-beautifulsoup/imagesscrapping1/allimages1/"+"-image-number-"+str(count)+"-.jpg",'wb')
    for chunk in r2:
        fp.write(chunk)
    fp.close()
    count+=1