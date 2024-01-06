import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Nome del file JSON che funge da "database"
DATABASE_FILE = "DATA/rubrica.json"

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

@app.route('/')
def home():
    #return render_template('index.html')
    return render_template('home.html')

@app.route('/rubrica', methods=['GET', 'POST'])
def manage_rubrica():
    data = load_database()

    if request.method == 'GET':
        #return jsonify(data)
        # Rendi il template read.html per visualizzare l'elenco dei contatti
        return render_template('read.html', data=data)       
    elif request.method == 'POST':
        try:
            new_contact = request.get_json()
            data.append(new_contact)
            save_database(data)
            return jsonify({"message": "Contatto aggiunto con successo"}), 201
        except Exception as e:
            return jsonify({"message": "Errore durante l'aggiunta del contatto", "error": str(e)}), 400


@app.route('/inserisci')
def inserisci():
    return render_template('create.html')

@app.route('/rubrica/<int:index>', methods=['GET', 'PUT', 'DELETE'])
def manage_contact(index):
    data = load_database()

    if 0 <= index < len(data):
        if request.method == 'GET':
            return render_template('read_one.html', contact=data[index])
        elif request.method == 'PUT':
            try:
                updated_contact = request.get_json()
                data[index] = updated_contact
                save_database(data)
                return jsonify({"message": "Contatto aggiornato con successo"})
            except Exception as e:
                return jsonify({"message": "Errore durante l'aggiornamento del contatto", "error": str(e)}), 400
        elif request.method == 'DELETE':
            del data[index]
            save_database(data)
            return jsonify({"message": "Contatto eliminato con successo"})
    else:
        return jsonify({"message": "Contatto non trovato"}), 404

if __name__ == '__main__':
    app.run(debug=True)
