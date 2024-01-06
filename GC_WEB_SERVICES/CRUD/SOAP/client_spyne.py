from spyne import Client
from spyne.protocol.soap import Soap11

client = Client('http://127.0.0.1:8000/?wsdl', Soap11())
risultato = client.service.say_hello('GCARNAB', 1)

print(risultato)
