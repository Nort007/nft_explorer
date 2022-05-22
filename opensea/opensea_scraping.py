import requests
import json
from bs4 import BeautifulSoup
import time


def scrape(url: str, headers: dict) -> str:
    """Скрапит данные html"""
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url, headers=session.headers)
    return response.text


def explore_data(html: str = None, file: str = None, elements: dict = None) -> json:
    """Указывается один из двух параметров который будет исследован
    elements ключ: является тегом html
    elements значение: атрибут html тега, dict/json в виде ключ-значение
    """
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        if elements is not None:
            for tag, attribute in elements.items():
                data = soup.find(tag, attribute).getText()
                return json.loads(data)
    elif file is not None:
        with open(file, 'r') as f:
            data = json.load(f)
            return data


def explore_data_by_element(html: str = None, tag: str = 'div', attribute: str = 'class', el: str = "") -> None:
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all(tag, {attribute: el})
    print(soup.prettify())
    return data


def save_file(data):
    """Сохраняет данные в файл"""
    t = time.strftime('%d_%m_%y_%H:%M:%S', time.gmtime())
    with open(f'opensea_data_{t}.json', 'w') as f:
        return json.dump(data, f)


url = 'https://opensea.io/assets?search[query]=0x524cab2ec69124574082676e6f654a18df49a048'
headers = {
    'Referer': 'https://opensea.io/',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'content-encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
ELEMENTS = {
        'script': {'id': '__NEXT_DATA__'}
    }

# if __name__ == '__main__':
#     text = scrape(url, headers)
    # explore_html = explore_data(html=text, elements=ELEMENTS)
    # save_file(explore_html)
    # explore_file = explore_data(file='opensea_data_16_05_22_10:57:41.json', elements=ELEMENTS)
    # d = explore_file['props']['relayCache'][0][1]['data']['assets']['search']['edges'][0]
    # print(json.dumps(d, indent=4))
    # exp_by_el = explore_data_by_element(html=text, tag='div', attribute='class', el='slick-track')
    # print(exp_by_el)