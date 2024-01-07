from spyne import Application, rpc, ServiceBase, Unicode, json, Integer, Iterable, ComplexModel, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import logging
import json

# Nome del file JSON che funge da "database"
DATABASE_FILE = "SOAP/DATA/rubrica.json"

# Carica i dati dal file JSON, o restituisci una lista vuota se il file non esiste
def load_database():
    try:
        with open(DATABASE_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Salva i dati nel file JSON con formattazione indentata
def save_database(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=2)

class Contatto(ComplexModel):
    Nome = Unicode(description="Nome del contatto")
    Cognome = Unicode(description="Cognome del contatto")
    Email = Unicode(description="Email del contatto", minOccurs=0)
    Telefono = Unicode(description="Numero di telefono del contatto", minOccurs=0)


class RubricaService(ServiceBase):

    @rpc(_returns=Array(Contatto))
    def ottieni_rubrica(ctx):
        data = load_database()

        return data
  
    @rpc(Contatto, _returns=Integer)
    def aggiungi_contatto(ctx, contatto):
        try:
            with open(DATABASE_FILE, 'r') as file:
                rubrica = json.load(file)
        except FileNotFoundError:
            rubrica = []

        rubrica.append({
            'Nome': contatto.Nome,
            'Cognome': contatto.Cognome,
            'Email': contatto.Email,
            'Telefono': contatto.Telefono
        })

        try:
            with open(DATABASE_FILE, 'w') as file:
                json.dump(rubrica, file, indent=2)
        except Exception as e:
            logging.error(f"Error writing to rubrica.json: {e}")

        return 1  # Successo

    @rpc(Array(Contatto), _returns=Integer)
    def aggiorna_rubrica(ctx, rubrica):
        try:
            current_rubrica = load_database()
            for contact_update in rubrica:
                # Iterate through the updated contacts
                index_to_update = -1

                # Find the index of the contact to update in the current rubrica
                for i, current_contact in enumerate(current_rubrica):
                    if current_contact['Nome'] == contact_update.Nome and current_contact['Cognome'] == contact_update.Cognome:
                        index_to_update = i
                        break

                # If the contact is found, update it
                if index_to_update != -1:
                    current_rubrica[index_to_update] = {
                        'Nome': contact_update.Nome,
                        'Cognome': contact_update.Cognome,
                        'Email': contact_update.Email,
                        'Telefono': contact_update.Telefono
                    }

            # Save the updated rubrica to the file
            save_database(current_rubrica)
        except Exception as e:
            logging.error(f"Error writing to rubrica.json: {e}")

        return 1  # Successo
    
class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """

        for i in range(times):
            yield u'Hello, %s' % name

class AdditionService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, num1, num2):
        return num1 + num2

class SubtractionService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, num1, num2):
        return num1 - num2

application = Application([RubricaService, HelloWorldService, AdditionService, SubtractionService],
    tns='http://test.python.spyne',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()