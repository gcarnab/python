import requests
import json
from pprint import pprint

class GCTelegramBotService:
    """
    Class for interaction with Telegram Bot
    @author : GCARNAB

    """    
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def getUpdates(self) :
        """
        Use this method to receive incoming updates using long polling
        @author : GCARNAB
        
        """            
        url = self.url + self.token + "/getUpdates"

        response = requests.request("GET", url)        
        return response.text

    def sendMessage(self, chat_id, parse_mode, message_text) :
        """
        Use this method to send text messages. On success, the sent Message is returned.
        @author : GCARNAB
        
        """     

        emoji_01 = '\U0001F916 This is a Robot face!\n'
        emoji_01 += '\uE404 This is a smiling face!'
        final_message_text=f"From GC {message_text}! {emoji_01}"

        url = self.url + self.token + \
            "/sendMessage?chat_id=" + chat_id + \
            "&parse_mode=" + parse_mode + \
            "&text=" + final_message_text
        print(">>>>> URL TO SEND: ", url)
        response = requests.request("GET", url)        
        return response.text    

