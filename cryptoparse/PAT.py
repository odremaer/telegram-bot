import requests
from bs4 import BeautifulSoup


URL = 'https://www.coingecko.com/ru/Криптовалюты/patron/eth'
HEADERS = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/81.0.4044.113 Safari/537.36',
    'accept': '*/*'
}


def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='col-12 row p-0 m-0')
    pat = ''
    for item in items:
        pat += (item.find('span', class_='no-wrap').get_text())
    return {'pat':pat}


def get_html(url):
    r = requests.get(url,headers=HEADERS)
    return r


def parse2():
    html = get_html(URL)
    if html.status_code == 200:
        res = get_content(html.text)
    else:
        print('что-то пошло не так')
    return res

parse2()