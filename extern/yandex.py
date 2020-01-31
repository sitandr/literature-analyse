import requests
from bs4 import BeautifulSoup as bs

def search(query, site = None):
    
    res = []

    url = "https://yandex.ru/search/?text=" + query + ("" if site is None else "&site=" + site)
    responce = requests.get(url).text
    # print(responce.encode('cp1251', 'ignore'))
    
    soup = bs(responce, "html.parser")
    data = bs(str(soup.find_all('div', class_="main__content")[0]), "html.parser")
    new_data = data.find_all('li', class_="serp-item")
    for li in new_data:
        buff = bs(str(li), "html.parser")
        all_buff = bs(str(buff.find_all('h2')[0]), "html.parser")
        ass = all_buff.find_all('a')
        for a in ass:
            if site is None or a.get("href").find(site) != -1:
                res.append(a.get("href"))
    return res

if __name__ == "__main__":
    refs = search("лев толстой", "wikipedia.org")
    print("\n".join(refs))
