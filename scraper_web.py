import requests
from bs4 import BeautifulSoup

def scrapear_sitio(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}  # Para evitar bloques
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Ejemplo: Extrae títulos (adapta para otros sitios)
        titulos = soup.find_all('h2')  # Cambia 'h2' según estructura del sitio
        for titulo in titulos[:5]:  # Top 5
            print(titulo.text.strip())
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo: Cambia URL por una real pública (ej. noticias)
scrapear_sitio("https://news.ycombinator.com")