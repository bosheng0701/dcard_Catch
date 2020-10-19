import requests
import re
from bs4 import BeautifulSoup
import sys
import os 




while(1):
    fp=open ('dcard.txt','a', encoding='utf-8')
    url =input("輸入文章ID: ")
    index = requests.get('http://dcard.tw/_api/posts/'+url+'/comments?limit=100')
    soup=index.json()
    j=1
    try:
        for i in soup:
            print(str(j)+i["content"])
            fp.write(i["content"]+"\n")
            j+=1
    except:
        fp.write(i["content"]+"\n")
        os.system ('pause')
