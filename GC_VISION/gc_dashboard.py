import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def execute_module(module_name):
    module_path = os.path.join(os.path.dirname(__file__), f'{module_name}.py')
    try:
        subprocess.run(['python', module_path], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Error', f'Error executing module {module_name}: {e}')

# Create the main application window
app = tk.Tk()
app.title('GC Vision Dashboard')

# Function to handle menu item selection
def menu_click(module_name):
    execute_module(module_name)

# Create a menu bar
menu_bar = tk.Menu(app)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Draw Shapes', command=lambda: menu_click('gc_draw_shapes'))
file_menu.add_command(label='Module 2', command=lambda: menu_click('module2'))
file_menu.add_command(label='Module 3', command=lambda: menu_click('module3'))
file_menu.add_separator()
file_menu.add_command(label='Exit', command=app.quit)
menu_bar.add_cascade(label='Modules', menu=file_menu)

# Set the menu bar
app.config(menu=menu_bar)

# Run the application
app.mainloop()
