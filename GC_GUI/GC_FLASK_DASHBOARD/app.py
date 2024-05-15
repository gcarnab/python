from flask import Flask, render_template, request, redirect, url_for
import os
import importlib

app = Flask(__name__)

# Define available projects and their module paths
projects = {
    'Hello World': 'hello_world.main',
}

'''
# Mock data for demonstration
projects = {
    'Project 1': 'print("Executing Project 1 Code")',
    'Project 2': 'print("Executing Project 2 Code")',
    'Project 3': 'print("Executing Project 3 Code")'
}
'''

@app.route('/')
def dashboard():
    return render_template('dashboard.html', projects=projects)
'''
@app.route('/execute', methods=['POST'])
def execute_project():
    project_name = request.form['project']
    if project_name in projects:
        # In a real situation, you'd replace the exec function with more secure practices
        exec(projects[project_name])
    return redirect(url_for('dashboard'))
'''

@app.route('/execute', methods=['POST'])
def execute_project():
    project_name = request.form['project']
    if project_name in projects:
        module_name = projects[project_name]
        try:
            module = importlib.import_module(module_name)
            return redirect(url_for('show_result', result=module.run()))
        except ImportError:
            return "Module not found", 404
    return redirect(url_for('dashboard'))

@app.route('/result')
def show_result():
    result = request.args.get('result', '')
    return f"<h1>{result}</h1>"

if __name__ == '__main__':
    app.run(debug=True)