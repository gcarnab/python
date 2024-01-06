from flask import Flask, request, render_template
from zeep import Client

app = Flask(__name__)

# Replace the URL with the address where your SOAP service is running
SOAP_SERVICE_URL = 'http://127.0.0.1:8000/?wsdl'

client = Client(SOAP_SERVICE_URL)

@app.route('/')
def index():
    return render_template('index.html')

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
