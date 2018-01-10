#conding:utf8



class Write_to_file(object):
    def __init__(self):
        self.ok = 'ok'

    def write_to_txt(self, KeyWords,count,title_en,abstract_en,title_cn,abstract_cn,new_url):

        filename = '.\\爬取结果\\' + KeyWords + '\\' + KeyWords + '.txt'

        # 打开文件
        file_txt = open(filename, 'a', encoding='utf8')

        # 将列表写入txt文件
        file_txt.write('【' + str(count) + '】:  '
                       'title: '+ title_en + '\n'
                        '题目: ' + title_cn + '\n'
                       'abstract: ' + abstract_en + '\n'
                       '摘要: '+ abstract_cn + '\n'
                       '链接:' + new_url + '\n\n')