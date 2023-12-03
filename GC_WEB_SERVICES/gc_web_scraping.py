import requests
from bs4 import BeautifulSoup

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
    print("1. Ottenere il titolo di una pagina web")
    print("2. TODO")
    print("3. TODO")
    print("x. Exit")

def main():
    while True:
        main_menu()
        choice = input("Inserisci il numero dell'opzione desiderata: ")

        if choice == '1':
            url = input("Inserisci l'URL della pagina web: ")
            title = get_title(url)
            print(f'Titolo della pagina: {title}')
        elif choice == "2":
            pass          
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
