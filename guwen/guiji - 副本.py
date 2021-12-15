import requests
from lxml import etree
from urllib.parse import urljoin
import collections
import time
from random import randint
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup



headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


def login():
    login_url = "http://www.artx.cn/user/login.asp?act=submit"
    login_data = {
        'duser': 'testcode',
        'dpwd': 'testcode',
    }
    session = requests.Session()
    res = session.post(login_url, headers=headers, data=login_data)
    if res.status_code == 200:
        return session
    print('login failed')
    return None


# start_url = 'http://guji.artx.cn/Article/2570.html'
# html = urlopen('http://guji.artx.cn/article/2634.html')
# bsObj = BeautifulSoup(html, "html.parser")
# bookname = bsObj.findAll("a", {"href":"2570.html"})
# for name in bookname:
#     print(name.get_text())
j = 2570
start_url = "http://guji.artx.cn/Article/" + str(j) +".html"
html = urlopen("http://guji.artx.cn/Article/" + str(j) +".html")
bsObj = BeautifulSoup(html, "html.parser")
bookname = bsObj.findAll("a", {"href":'"str(j) +".html'})
for name in bookname:
    print(name.get_text())

def get_content(session, url, title=''):
    if not url:
        return
    res = session.get(url)
    res.encoding = 'utf-8'
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    sn = cookies.get('guji%5Fsn', '1')
    cookies['sn'] = str(int(sn) + 1)
    # all links
    selector = etree.HTML(res.text)
    texts = selector.xpath('//*[@id="r_zhengwen"]/text()')
    with open('my_book.text', 'a+', encoding='utf8') as f:
        if title:
            f.write('\r\n')
            f.write(title)
            f.write('\r\n------------------------------------------------------------------\r\n')
        for text in texts:
            f.write(text)
    links = selector.xpath('//*[@id="dright"]/div[5]/div[2]/ul/li/a')
    catalog = collections.OrderedDict()
    for link in links:
        url = link.attrib['href']
        cata_name = link.text
        catalog[url] = cata_name
    for url in catalog:
        time.sleep(randint(1, 3))
        title = catalog[url]
        url = urljoin(start_url, url)
        print(f'下载:{title}；{url},')
        get_content(session, url, title)


def html_parse():
    with open('test.html', encoding='utf8') as f:
        contents = f.read()
    selector = etree.HTML(contents)
    texts = selector.xpath('//*[@id="r_zhengwen"]/text()')
    links = selector.xpath('//*[@id="dright"]/div[5]/div[2]/ul/li/a')
    for link in links:
        print(link.text, link.attrib['href'])


if __name__ == "__main__":
    # html_parse()
    session = login()
    if session:
        get_content(session, start_url)

os.rename('my_book.txt',name.get_text())
