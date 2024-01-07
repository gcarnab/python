from flask import Flask, request, render_template, flash, redirect
from zeep import Client
import logging

app = Flask(__name__)

app.secret_key = '3d830b4ef79d639df33f002268546acecd6a312a57672eb1759590153731bb42'

# Replace the URL with the address where your SOAP service is running
SOAP_SERVICE_URL = 'http://127.0.0.1:8000/?wsdl'

client = Client(SOAP_SERVICE_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rubrica')
def rubrica():
    rubrica = client.service.ottieni_rubrica()
    if rubrica is not None:
        return render_template('rubrica.html', rubrica=rubrica)
    else:
        flash('Errore nel recupero della rubrica', 'error')
        return render_template('rubrica.html', rubrica=[])

@app.route('/rubrica/add', methods=['GET', 'POST'])
def aggiungi_contatto():
    if request.method == 'POST':
        nome = request.form['nome']
        cognome = request.form['cognome']
        email = request.form['email']
        telefono = request.form['telefono']

        contatto = {'Nome': nome, 'Cognome': cognome, 'Email': email, 'Telefono': telefono}

        result = client.service.aggiungi_contatto(contatto)

        if result == 1:
            flash('Contatto aggiunto con successo!', 'success')
            return redirect('/rubrica')
        else:
            flash('Errore durante l\'aggiunta del contatto', 'error')

    return render_template('rubrica_add.html')

@app.route('/rubrica/get/<int:index>')
def rubrica_dettaglio(index):
    contatto = ottieni_dettagli_contatto(index)
    if contatto:
        return render_template('rubrica_detail.html', contatto=contatto)
    else:
        flash('Contatto non trovato', 'error')
        return redirect('/rubrica')

@app.route('/rubrica/delete/<int:index>')
def rubrica_cancella(index):
    if cancella_contatto(index):
        flash('Contatto cancellato con successo!', 'success')
    else:
        flash('Errore durante la cancellazione del contatto', 'error')
    return redirect('/rubrica')

# Funzione per ottenere dettagli di un contatto
def ottieni_dettagli_contatto(index):
    rubrica = client.service.ottieni_rubrica()
    if 1 <= index <= len(rubrica):
        return rubrica[index - 1]
    return None

# Funzione per cancellare un contatto
def cancella_contatto(index):
    rubrica = client.service.ottieni_rubrica()
    if 1 <= index <= len(rubrica):
        # Remove the contact from the list
        del rubrica[index - 1]

        # Update the rubrica in the SOAP service
        result = client.service.aggiorna_rubrica(rubrica)

        # Check if the update was successful
        if result == 1:
            logging.info(f"Contact at index {index} deleted successfully.")
            return True
        else:
            logging.error(f"Error updating rubrica in SOAP service. Response: {result}")
    return False

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    times = int(request.form['times'])

    # Call the say_hello SOAP operation
    result = client.service.say_hello(name, times)

    return render_template('result.html', result=result)

@app.route('/add', methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    # Call the add SOAP operation
    result = client.service.add(num1, num2)

    return render_template('result.html', result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    # Call the subtract SOAP operation
    result = client.service.subtract(num1, num2)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
