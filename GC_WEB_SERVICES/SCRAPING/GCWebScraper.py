import requests
from bs4 import BeautifulSoup
import os

# Libreria per il web scraping by GC
class WebScraper:
    def __init__(self, url):
        self.url = url

    def scarica_pagina(self, directory="GC_WEB_SERVICES/DATA"):
        # Assicurati che la directory esista, altrimenti creala
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            # Scarica la pagina web
            response = requests.get(self.url)
            response.raise_for_status()  # Solleva un'eccezione in caso di errore HTTP

            # Ottieni il contenuto HTML
            html_content = response.text

            # Utilizza BeautifulSoup per analizzare l'HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Estrai il titolo della pagina
            titolo_pagina = soup.title.string

            # Salva l'HTML in un file nella directory DATA
            file_path = os.path.join(directory, f"{titolo_pagina}.html")

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(html_content)

            print(f"\n>>>>> Pagina scaricata con successo e salvata in {file_path}")
        except requests.exceptions.RequestException as e:
            print(f"Errore durante il download della pagina: {e}")

    def getTitle(self):
        try:
            # Scarica la pagina web
            response = requests.get(self.url)
            response.raise_for_status()  # Solleva un'eccezione in caso di errore HTTP

            # Ottieni il contenuto HTML
            html_content = response.text

            # Utilizza BeautifulSoup per analizzare l'HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Estrai il titolo della pagina
            titolo_pagina = soup.title.string

            print(f"\n >>>>>>> Titolo della pagina: {titolo_pagina}")

        except requests.exceptions.RequestException as e:
            print(f"Errore durante il download della pagina: {e}")
