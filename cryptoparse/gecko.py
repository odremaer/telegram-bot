import requests
from bs4 import BeautifulSoup


URL = 'https://www.coingecko.com/ru'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
           'accept':'*/*'}






def get_html(urlg,params=None):
    r = requests.get(urlg, headers=HEADERS, params=params)
    return r



def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('td', class_='td-price price text-right')
    btc = ''
    eth = ''
    for item in items:
        if item.find('span',class_='no-wrap').get('data-coin-symbol') == 'btc':
            btc+=(item.find('span', class_='no-wrap').get_text())
        if item.find('span',class_='no-wrap').get('data-coin-symbol') == 'eth':
            eth+=(item.find('span', class_='no-wrap').get_text())
    return {'btc':btc,'eth':eth}



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        res = get_content(html.text)
    else:
        print('что-то пошло не так')
    return res


parse()