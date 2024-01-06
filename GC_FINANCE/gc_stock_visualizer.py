import pandas as pd 
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import os


def page_download(web_url, directory="GC_FINANCE/DATA"):
    # Assicurati che la directory esista, altrimenti creala
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        # Scarica la pagina web
        response = requests.get(web_url)
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

def get_real_time_data(symbol) :

    url = f"https://finance.yahoo.com/quote/{symbol}"
    #print(">>> URL: ", url)

    try :
        my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        headers = {'User-Agent': my_user_agent}
        response = requests.get(url, headers=headers)
        #response = requests.get(url)
        #print(">>> response.text: ", response.text)

        #soup = BeautifulSoup(response.text,'lxml')
        soup = BeautifulSoup(response.text,'html.parser')

        #page_download(url)

        class_path = "D(ib) Mend(20px)"
        #element_to_find = "span"
        element_to_find = "fin-streamer"

        stocks_data = {
            'symbol' : symbol,
            'price' : soup.find('div', {'class': class_path}).find_all(element_to_find)[0].text,
            'change' : soup.find('div', {'class': class_path}).find_all(element_to_find)[2].text,           
        }

        #price = soup.find('div', {'class': class_path}).find_all(element_to_find)[0].text
        #change = soup.find('div', {'class': class_path}).find_all(element_to_find)[2].text

    except Exception as e:
        print(f"### real_time_price Error : {e}")
        price, change = None, None

    #return price, change   
    return stocks_data


if __name__ == "__main__":

    my_stocks = ['MSFT','AAPL','GOOGL','NVDA']
    
    iteration = 0
    while iteration < 2 :
        output_data = []
        time_stamp = datetime.datetime.now()
        time_stamp_str = time_stamp.strftime('%Y-%m-%d-%H-%M-%S')
        row_data = [time_stamp_str]  # Initialize the list with timestamp

        for item in my_stocks :
            #print("Getting: ", item)
            #stock_data.append(get_real_time_data(item))           
            stock_info = {'data': get_real_time_data(item)}
            row_data.extend(stock_info.values())  # Append stock data to the row

        output_data.append(row_data)
        df = pd.DataFrame(output_data)
        print(df.head)

        # Convert the list of lists to a DataFrame
        #output_df = pd.DataFrame(output_data, columns=['timestamp', 'symbol', 'price', 'change'])
        #print(output_df.head)

        file_path = 'GC_FINANCE/DATA/' + str(time_stamp_str[0:10]) + '_stock_data.csv'
        df.to_csv(file_path, mode='a',header=False)
        iteration+=1