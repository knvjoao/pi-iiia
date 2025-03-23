import requests
from bs4 import BeautifulSoup
from db import insert_filmes, confirmation, connect_to_db

base_url = "https://nahoradoocio.lowlevel.com.br/category/lista-de-filmes/"
STATUS_OK = 200

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}


# Realizar o scrap de cada lista.
def scrap_movies(list_url, conn):
    print(f"Accessando URL: {list_url}")
    response = requests.get(list_url, headers = headers)
    
    if response.status_code == STATUS_OK:
        print(f"Sucesso ao acessar: {list_url}")

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Encontrar os títulos de cada série ou filme.
        titles = soup.select("div.main-container article.blog-post h2")
        category = soup.find("h1", {"class": "post-title"})
        category_text = category.get_text()

        # Para cada título da lista
        for title in titles:
            title_text = title.get_text()
            print(f"Título: {title_text}  |  Categoria: {category_text}")
            insert_filmes(title_text, category_text, conn)  # Passando conn para a função            
    else:
        print(f"Falha ao acessar {list_url}. Erro {response.status_code}")


# Esta função abre os botões(<a>) "leia mais". A cada link aberto, é executado scrap_movies.
def acess_movies_lists(base_url, conn):
    print(f"Accessando: {base_url}")
    response = requests.get(base_url, headers = headers)
    
    if response.status_code == STATUS_OK:
        print("Acesso realizado.")
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        read_more_divs = soup.find_all("div", {"class": "read-more"})

        for div in read_more_divs:
            link = div.find("a")
            if link:
                list_url = link.get("href")
                print(f'Link: {list_url}')
                scrap_movies(list_url, conn)
    else:
        print(f"Falha ao acessar {base_url}. Erro {response.status_code}")



# Executar o programa
conn = connect_to_db()
acess_movies_lists(base_url, conn)
confirmation(conn)