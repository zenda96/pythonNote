#-*- coding:utf-8 -*-

import urllib.parse  
import urllib.request  
from bs4 import BeautifulSoup

data={}  
data['word']="python"  
   
url_values=urllib.parse.urlencode(data) 
print(url_values)
url="http://www.baidu.com/s"  


data=urllib.request.urlopen(url,url_values).read()    
soup = BeautifulSoup(data)
print(soup.prettify())  