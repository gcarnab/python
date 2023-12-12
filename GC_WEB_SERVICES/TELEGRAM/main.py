from GCTelegramService import GCTelegramBotService
import json
from pprint import pprint

########### GLOBAL VARIABLES ###########

service_base_url = "https://api.telegram.org/"
token_bot = "bot6980924938:AAESasUzI526sR3bB6_YduyRXrCbrVgjz9Q"
chat_id = "392851387"
parse_mode = "HTML" # HTML or Markdown

########################################


def main_menu():
    print("\n<<<<< GC TELEGRAM SERVICE >>>>>")
    print("Scegli un'opzione:")
    print("0. Info BOT")
    print("1. Send message")
    print("2. ")
    print("3. ")
    print("x. Exit")


def main():
    while True:
        main_menu()
        choice = input("Inserisci il numero dell'opzione desiderata: ")
        
        if choice == '0':
            service = GCTelegramBotService(service_base_url,token_bot)
            result = service.getUpdates()
            pprint(json.dumps(json.loads(result), sort_keys=True, indent=4, separators=(",", ": ")))            
        elif choice == "1":
            service = GCTelegramBotService(service_base_url,token_bot)
            message_text = input("Inserisci il messaggio da inviare: ")
            result = service.sendMessage(chat_id, parse_mode, message_text)
            pprint(json.dumps(json.loads(result), sort_keys=True, indent=4, separators=(",", ": ")))   
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
