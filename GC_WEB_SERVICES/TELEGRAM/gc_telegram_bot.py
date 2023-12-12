import requests
import json
from pprint import pprint

token_bot = "bot6980924938:AAESasUzI526sR3bB6_YduyRXrCbrVgjz9Q"
service_base_url = "https://api.telegram.org/"
chat_id = "392851387"
parse_mode = "HTML" # HTML or Markdown

def getUpdates() :
    url = service_base_url + token_bot + "/getUpdates"

    response = requests.request("GET", url)        
    return response.text

def sendMessage(message_text) :
    url = service_base_url + token_bot + "/sendMessage?chat_id=" + chat_id + "&parse_mode=" + parse_mode + "&text=" + message_text
    print(">>>>> URL TO SEND: ", url)
    response = requests.request("GET", url)        
    return response.text    

def main():
    #result = getUpdates()
    #pprint(json.dumps(json.loads(result), sort_keys=True, indent=4, separators=(",", ": ")))

    result = sendMessage("YEAHHHH!")
    pprint(json.dumps(json.loads(result), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == "__main__":
    main()