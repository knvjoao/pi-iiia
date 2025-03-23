import requests
from bs4 import BeautifulSoup
from db import connect_to_db, insert_post, confirmation


# Observação: foram trocadas duas linhas do código, que foi executado duas vezes. Para o base_url, são duas opções:
# base_url = "https://nahoradoocio.lowlevel.com.br/category/lista-de-filmes/"
# base_url = "https://nahoradoocio.lowlevel.com.br/category/maratonas-de-series/"

base_url = "https://nahoradoocio.lowlevel.com.br/category/maratonas-de-series/"
STATUS_OK = 200
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
url = base_url
response = requests.get(url, headers = headers)
conn = connect_to_db()


if response.status_code == STATUS_OK:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    posts = soup.find_all("h2", {"class": "post-title"})

    for post in posts:
        link = post.find("a")
        titulo = link.get_text()
        link_titulo = link.get("href")


        print(f"Título: {titulo}")
        print(f"Link: {link_titulo}")
        insert_post(titulo, link_titulo, "series", conn)          # Segunda linha trocada. "filmes" para base_url com filmes, "series" para series
 
    confirmation(conn)