#conding:utf8


import requests



class Translate(object):
    def __init__(self):
        self.ok = 'ok'


    def en2ch(self, q):
        import urllib.request
        from HandleJs import Py4Js
        # 利用 谷歌翻译 爬虫 进行翻译
        #  http://blog.csdn.net/yingshukun/article/details/53470424
        content =  q
        js = Py4Js()
        tk = js.getTk(content)
        if len(content) > 4891:
            print("翻译的长度超过限制！！！")
            return

        param = {'tk': tk, 'q': content}

        result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
                &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
                &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

        # 返回的结果为Json，解析为一个嵌套列表
        # print(type(result))

        # print(type(result.json()))
        # print(len(result.json()))
        rst = ''
        for ii in range(0, len(result.json()[0]) - 1):
            rst = rst + result.json()[0][ii][0]

        return rst






# 主程序
if __name__ == "__main__":
    # 实例化爬虫
    trans = Translate()

    # 翻译
    q = 'Rotor cracks represent an uncommon but serious threat to rotating machines and must be detected early to avoid catastrophic machine failure. An important aspect of analyzing rotor cracks is understanding their influence on the rotor stability. It is well-known that the extent of rotor instability versus shaft speed is exacerbated by deeper cracks. Consequently, crack propagation can eventually result in an unstable response even if the shaft speed remains constant. Most previous investigations of crack-induced rotor instability concern simple Jeffcott rotors. This work advances the state-of-the-art by (a) providing a novel inertial-frame model of an overhung rotor, and (b) assessing the stability of the cracked overhung rotor using Floquet stability analysis. The rotor Floquet stability analysis is performed for both an open crack and a breathing crack, and conclusions are drawn regarding the importance of appropriately selecting the crack model. The rotor stability is analyzed versus crack depth, external viscous damping ratio, and rotor inertia. In general, this work concludes that the onset of instability occurs at lower shaft speeds for thick rotors, lower viscous damping ratios, and deeper cracks. In addition, when comparing commensurate cracks, the breathing crack is shown to induce more regions of instability than the open crack, though the open crack generally predicts an unstable response for shallower cracks than the breathing crack. Keywords: rotordynamics, stability, rotor cracks.'

    print(trans.en2ch(q))