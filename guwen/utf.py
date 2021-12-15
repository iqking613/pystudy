from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

j = 2570
html = urlopen("http://guji.artx.cn/Article/" + str(j) +".html")
bsObj = BeautifulSoup(html, "html.parser")
bookname = bsObj.find("div",{"class":"dforum_show_title"}).findAll("h1")
for name in bookname:
    print(name.get_text())
    os.rename('my_book.text',name.get_text() +".text")
# links = selector.xpath('//*[@id="dright"]/div[2]/h1')
# print(links)


# book = bsObj.div.h1
# name = book.get_text()
# # print(book.get_text())
# # bookname = bsObj.findAll("div",{"class":"dforum_show_title"})
# # for name in bookname:
# #     print(name)
#
# os.rename('my_book.text',name +".text")

# res =  requests.get(url, headers=header)
# # wbdata = requests.get(url,headers=header).text
# # soup = BeautifulSoup(wbdata,'lxml')
# # print(soup)
#
# f = open("sj.txt","r+")
# # f.write("fdfs")
# # f.close()
# for j in range(2194,2325):
#     # html = urlopen("http://guji.artx.cn/Article/" + str(j) +".html")
#     url = 'http://guji.artx.cn/Article/'+ str(j) +".html"
#     res = requests.get(url, headers=header)
#     html_content = res.text.encode('ISO-8859-1').decode('utf8')
#     bsObj = BeautifulSoup(html_content, "html.parser")
#     print(bsObj)
# # title = bsObj.findAll("div", {"class":"dforum_show_title"})
# # for ti in title:
# #     print(ti.get_text())
#     nameList = bsObj.findAll("div", {"id":"r_zhengwen"})
#     for name in nameList:
#     # print(name.get_text())
#         f.write(name.get_text())
# f.close()
