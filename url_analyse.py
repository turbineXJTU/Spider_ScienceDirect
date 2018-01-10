#conding:utf8

import time
from bs4 import BeautifulSoup
import random

from urllib.request import urlopen
from urllib.request import Request

class Url_analyse(object):
    def __init__(self):
        self.ok = 'ok'




    # 爬取检索页
    def analyse_SearchPage(self, start_url):
        print('检索页>正在爬取  ' + start_url)
        req = Request(start_url)
        req.add_header("Host", "www.sciencedirect.com")
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
        flag = 1
        while flag<20:
            try:
                print('检索页>正在向网页发送请求')
                resp = urlopen(req, timeout=10)
                flag = 200
                soup = BeautifulSoup(resp, "html.parser")
                new_urls = []
                for ii in soup.find_all("div", {"class": "result-item-content"}):
                    for jj in ii.find_all("h2"):
                        for zzl_href in jj.find_all("a"):
                            new_urls.append(r'http://www.sciencedirect.com' + zzl_href.get('href'))

            except:
                print('检索页>网络出了问题，第 %s 次重连' % str(flag))
                flag = flag +1
                new_urls = []
                if flag > 20:
                    print('检索页>放弃爬取')
        return new_urls






    # 爬取论文页
    def analyse_EveryPage(self, new_url, count):
        print('\n\n论文页>正在爬取  %d : %s' % (count, new_url))
        req = Request(new_url)
        req.add_header("Host", "www.sciencedirect.com")
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")


        flag = 1
        # 失败后最多重连20次
        while flag<20:
            try:
                print('论文页>正在向网页发送请求')
                resp = urlopen(req, timeout=10)
                flag = 200
                soup = BeautifulSoup(resp, "html.parser")
                try:
                    print('论文页>正在从网页解析内容')
                    title = soup.find("span", {"class": "title-text"}).get_text()
                    temp = soup.find("div", {"class": "abstract author"})
                    abstract = temp.find("p").get_text()
                except:
                    print('论文页>从网页解析内容失败')
                    title = '论文页>解析失败'
                    abstract = '论文页>解析失败'
            except:
                print('论文页>网络出了问题，第 %s 次重连' % str(flag))
                flag = flag + 1
                title = '论文页>多次重连失败'
                abstract = '论文页>多次重连失败'
                if flag > 20:
                    print('论文页>放弃爬取')


        # 休息一会儿再爬
        time_lapse = random.uniform(2, 4)
        print('论文页>暂停 %f 秒爬下一篇' % (time_lapse))
        time.sleep(time_lapse)


        return (title,abstract)



