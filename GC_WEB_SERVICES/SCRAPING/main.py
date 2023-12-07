import requests
from bs4 import BeautifulSoup
from GCWebScraper import WebScraper

########### GLOBAL VARIABLES ###########

url_to_scrape = None

########################################

# Funzione per impostare l'URL
def imposta_url():
    global url_to_scrape
    url_to_scrape = input("Inserisci l'URL della pagina: ")
    print(f"\n>>>>> URL PAGINA MEMORIZZATO :  {url_to_scrape}")

def get_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.title
        return title_tag.text
    else:
        return f'Errore nella richiesta. Codice di stato: {response.status_code}'

def main_menu():
    print("\n<<<<< GC WEB SCRAPER >>>>>")
    print("Scegli un'opzione:")
    print("0. Inserisci url pagina web")
    print("1. Scarica pagina web")
    print("2. Estrai titolo della pagina")
    print("3. TODO")
    print("x. Exit")


def main():
    while True:
        main_menu()
        choice = input("Inserisci il numero dell'opzione desiderata: ")
        
        if choice == '0':
            imposta_url()
        elif choice == "1":
            if url_to_scrape is None:
                imposta_url()
            else :
                scraper = WebScraper(url_to_scrape)
                scraper.scarica_pagina()                       
        elif choice == "2":
            if url_to_scrape is None:
                imposta_url()
            else :
                scraper = WebScraper(url_to_scrape)
                scraper.getTitle()             
        elif choice == "3":
            pass           
        elif choice == "4":
            pass                            
        elif choice == "x" or choice =="X":
            print("Uscita.")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
