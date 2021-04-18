import requests
from pyquery import PyQuery as pq
import os


class Pic(object):

    def __init__(self, base_url, base_path, page_num=None):
        self.base_url = base_url
        self.base_path = base_path
        self.page_num = page_num

    def download(self):
        header = {
            'Referer': 'https://www.flaticon.com/search?word=financial',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
                          'Chrome/90.0.4430.72 Safari/537.36 ',
        }

        html = requests.get(self.base_url, headers=header)
        doc = pq(html.text)
        img = doc('li.icon--item>div.icon--holder>a>img')
        i = 0
        for url in img.items():
            i += 1
            a = url.attr('data-src')
            b = requests.get(a, headers=header)
            with open("{}//".format(self.base_path) + str(i) + '.png', 'wb') as f:
                f.write(b.content)
                f.close()
            print('抓取成功{}'.format(i))


if __name__ == '__main__':
    for j in range(3, 5):
        n_url = 'https://www.flaticon.com/search/{}?word=financial'.format(j)
        os.mkdir(str(j))
        if n_url == 'https://www.flaticon.com/search/1?word=financial':
            n_url = 'https://www.flaticon.com/search?word=financial'
            Pic(n_url, j).download()
        else:
            Pic(n_url, j).download()
