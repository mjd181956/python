from bs4 import BeautifulSoup
html="这是一个网页源码"
soup=BeautifulSoup(html,"lxml")
#使用对象的方法
soup.find_all("")
