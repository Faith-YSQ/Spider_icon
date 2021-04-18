import requests
from pyquery import PyQuery as pq

header = {
    'Referer': 'https://www.flaticon.com/search?word=financial',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
                  'Chrome/90.0.4430.72 Safari/537.36 ',
}

html = requests.get('https://www.flaticon.com/search?word=financial', headers=header)

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
    with open("金融图标//"+str(i) + '.png', 'wb') as f:
        f.write(b.content)
        f.close()
    print('抓取成功{}'.format(i))
