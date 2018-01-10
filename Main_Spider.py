#!/usr/bin/env python
# -*- coding:utf-8 -*-
# anthor: 小偷的部落 time:2017/12/17


import time
import url_analyse
import translate
import write_to_file
import os




# 爬虫类
class Spider:
    # 初始化函数
    def __init__(self):
        self.url_analyse = url_analyse.Url_analyse()
        self.translate = translate.Translate()
        self.write_to_file = write_to_file.Write_to_file()



    def remove_exist_floder(self,KeyWords):
        # 移除已存在的文件夹（以 KeyWords 命名）
        path = '.\\爬取结果\\' + KeyWords
        if not os.path.exists(path):
            os.makedirs(path)




    def remove_exist_txt(self,KeyWords):
        # 移除已存在的结果文件（以 KeyWords.txt 命名）
        filename = '.\\爬取结果\\' + KeyWords + '\\' + KeyWords + '.txt'
        if os.path.exists(filename):
            os.remove(filename)
            return




    def get_start_url(self,KeyWords):
        # 用空格对关键词切片
        KeyWords_split = KeyWords.split()
        # 拼接起始页面网址
        start_url = 'http://www.sciencedirect.com/search?qs='
        for ii in range(0, len(KeyWords_split)):
            # 'http://www.sciencedirect.com/search?qs=turbine%20blade%20crack&show=25&sortBy=relevance'
            if ii == 0:
                start_url = start_url + KeyWords_split[ii]
            else:
                start_url = start_url + '%20' + KeyWords_split[ii]
        start_url = start_url + '&show=25&sortBy=relevance'
        return start_url




    def run(self,KeyWords,Page_num):
        # 移除已存在的文件夹（以 KeyWords 命名）
        self.remove_exist_floder(KeyWords)

        # 移除已存在的结果文件（以 KeyWords.txt 命名）
        self.remove_exist_txt(KeyWords)

        # 获得起始页面网址
        start_url = self.get_start_url(KeyWords)

        # 分析起始搜索页面
        new_urls = self.url_analyse.analyse_SearchPage(start_url)

        # 开始爬虫
        count = 1
        while True:

            # 判断是否需要翻页
            if len(new_urls):
                # 从 new_urls 取一个新链接进行爬取
                new_url = new_urls[0]

                # 爬取新链接，获得 英文标题 和 英文摘要
                (title_en, abstract_en) = self.url_analyse.analyse_EveryPage(new_url, count)

                # 从 new_urls 移除已经爬取的链接
                new_urls.remove(new_urls[0])

                # 利用百度翻译API翻译标题和摘要
                title_cn = self.translate.en2ch(title_en)
                abstract_cn = self.translate.en2ch(abstract_en)

                # 将文章信息（中英文题目、中英文摘要、PDF下载链接）写入 KeyWords.txt
                self.write_to_file.write_to_txt(KeyWords,count,title_en,abstract_en,title_cn,abstract_cn,new_url)

                # 统计已处理的文献个数
                count = count + 1

            else:
                # 翻页
                print(start_url + '&offset=' + str(int(count-1)))
                new_urls = self.url_analyse.analyse_SearchPage(start_url + '&offset=' + str(int(count-1)))

            # 搜索文献数目达到要求便退出
            if count>Page_num:
                break







# 主程序
if __name__ == "__main__":

    # 实例化爬虫
    spider = Spider()

    # 统计程序开始的时间
    start = time.time()

    # 搜索关键词（方式1 赋值）
    # KeyWords = 'crack breathing rotor'

    # 搜索关键词（方式2 键盘输入）
    KeyWords = input('输入要查找的 关键词（用空格连接）：    ')

    # 设置搜索文章的数目
    Page_num = 5000

    # 打印检索初始条件
    print(KeyWords, Page_num)

    # 开始爬虫
    spider.run(KeyWords, Page_num)
