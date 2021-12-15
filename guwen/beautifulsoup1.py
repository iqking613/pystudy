# from urllib.request import urlopen
# import requests
# from bs4 import BeautifulSoup
# def get_html(r):
#     try:
#         response = requests.get(r, headers=headers)
#         response.encoding = 'GBK'
#         response.encoding = 'utf-8'
#         print(response.encoding)
#         r = response.text
#         return r
#     except:
#         print('请求网址出错')
# r = requests.get("http://guji.artx.cn/Article/2194.html")
#
# bsobj = r.text
# soup = BeautifulSoup(bsobj,'html.parser')
# name = soup.find_all(id="r_zhengwen")
# print(name)
