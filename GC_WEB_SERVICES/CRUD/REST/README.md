# GCARNAB CRUD REST WEB SERVICES REPOSITORY
___

By GCARNAB <a href='https://github.com/gcarnab'> <img src='https://avatars.githubusercontent.com/u/15156604?v=4' width="50"/></a>
___

## Contents

- app_items.py : main file for items CRUD app with SQLlite in-memory DB
- app_rubrica.py : main file for items CRUD app with json DB

## Resources

- https://flask.palletsprojects.com/en/3.0.x/

## Usage

- pip install flask
- pip install Flask-SQLAlchemy

## Tutorial

**Flask** è un framework web leggero per il linguaggio di programmazione Python. Il suo obiettivo è semplificare la creazione di applicazioni web mantenendo la flessibilità per gli sviluppatori. Ecco alcune caratteristiche chiave di Flask spiegate in modo semplice:

1. Routing: Flask ti permette di definire percorsi URL (routes) e associarli a funzioni specifiche. Ad esempio, quando un utente visita il percorso "/", potresti far sì che venga eseguita una funzione che restituisce "Ciao, mondo!".
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ciao, mondo!'

if __name__ == '__main__':
    app.run(debug=True)
```
2. Template: Flask supporta l'uso di modelli per separare il codice HTML dalla logica di backend. Questo rende più facile creare pagine web dinamiche.

3. Request Handling: Puoi gestire richieste HTTP in arrivo, ottenendo dati inviati dai clienti (ad esempio, dati di form) e prendendo decisioni basate su di essi.

4. Integration: Flask può essere facilmente integrato con altri componenti, librerie o framework. Ad esempio, puoi utilizzare un ORM (Object-Relational Mapping) come SQLAlchemy per interagire con un database.

5. Estensibilità: Se hai bisogno di funzionalità aggiuntive, Flask offre una vasta gamma di estensioni che possono essere facilmente integrate nel tuo progetto.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Ciao, {name}!'
    return '''
        <form method="post">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Invia">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

```