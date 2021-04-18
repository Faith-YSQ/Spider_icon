import requests
from pyquery import PyQuery as pq
import os


def down_pic(m_url, save_dir):
    header = {
        'Referer': 'https://www.flaticon.com/search?word=financial',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
                      'Chrome/90.0.4430.72 Safari/537.36 ',
    }

    html = requests.get(m_url, headers=header)

    # print(html.text)

    doc = pq(html.text)
    img = doc('li.icon--item>div.icon--holder>a>img')
    # print(img)

    i = 0
    for url in img.items():
        i += 1
        a = url.attr('data-src')
        # print(a)
        b = requests.get(a, headers=header)
        with open("{}//".format(save_dir) + str(i) + '.png', 'wb') as f:
            f.write(b.content)
            f.close()
        print('抓取成功{}'.format(i))


if __name__ == '__main__':
    for j in range(1, 3):
        n_url = 'https://www.flaticon.com/search/{}?word=financial'.format(j)
        # print(n_url)
        os.mkdir(str(j))
        if n_url == 'https://www.flaticon.com/search/1?word=financial':
            n_url = 'https://www.flaticon.com/search?word=financial'
            down_pic(n_url, j)
        else:
            down_pic(n_url, j)
