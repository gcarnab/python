# GCARNAB CRUD SOAP WEB SERVICES REPOSITORY
___

By GCARNAB <a href='https://github.com/gcarnab'> <img src='https://avatars.githubusercontent.com/u/15156604?v=4' width="50"/></a>
___

## Contents

- **server_spyne.py** : server SOAP using **spyne**
- **client_server_flask.py** : server HTTP using **flask** with SOAP client integrated using **zeep**


## Resources

- http://spyne.io/docs/2.10/
- https://docs.python-zeep.org/en/master/

## Usage

- pip install zeep
- pip install spyne

1. Execute server_spyne.py
2. Execute client_server_flask.py
3. Goto http://localhost:5000/ for GUI

## Docs

1. **Zeep** è una libreria moderna che utilizza un approccio basato sui dati. Questo approccio è più semplice e immediato rispetto all'approccio basato sui modelli utilizzato dalle altre due librerie. Zeep supporta un'ampia gamma di funzionalità, tra cui la sicurezza, la compressione e la serializzazione.

2. **Suds** è una libreria più matura che utilizza un approccio basato sui dati. Questo approccio è simile a quello utilizzato da Zeep, ma suds è meno flessibile e supporta meno funzionalità avanzate.

3. **Spyne** è una libreria moderna che utilizza un approccio basato sui modelli. Questo approccio consente di creare web service SOAP più flessibili e facili da usare. Spyne supporta un'ampia gamma di funzionalità, tra cui la sicurezza, la compressione e la serializzazione.

## Tutorial Spyne
1. Definire un Servizio Spyne
Iniziamo a creare il nostro servizio Spyne. Creiamo uno script Python chiamato servizio_spyne.py. In questo script, definiremo un semplice servizio che risponderà al saluto di un utente.

```python
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ServizioSemplice(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def saluta(ctx, nome):
        return f"Ciao, {nome}!"

applicazione = Application([ServizioSemplice],
                          tns='http://esempio.com/servizio_spyne',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

applicazione_wsgi = WsgiApplication(applicazione)

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, applicazione_wsgi)
    print("In ascolto su http://127.0.0.1:8000")
    server.serve_forever()

```
Qui stiamo definendo un servizio Spyne chiamato ServizioSemplice che ha un metodo saluta che prende un parametro nome e restituisce un saluto personalizzato. La configurazione di Application indica che il nostro servizio sarà disponibile all'indirizzo http://esempio.com/servizio_spyne e utilizzerà il protocollo SOAP 1.1.

2. Eseguire il Servizio Spyne
Ora possiamo eseguire il nostro servizio Spyne. Apri il terminale e esegui il seguente comando:

```console
python servizio_spyne.py

```
3. Creare un Cliente Zeep
Creiamo uno script Python chiamato client_zeep.py per interagire con il nostro servizio Spyne utilizzando Zeep.

```python
from zeep import Client

# URL del WSDL del servizio Spyne
wsdl_url = 'http://127.0.0.1:8000/?wsdl'

# Creiamo un oggetto client Zeep
client = Client(wsdl_url)

# Chiamiamo il metodo 'saluta' del nostro servizio
risultato = client.service.saluta(nome='Alice')

# Stampiamo il risultato
print(risultato)

```
4. Eseguire il Cliente Zeep

```console
python client_zeep.py
```