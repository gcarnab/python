import tkinter as tk

class MyGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label widget
        self.label = tk.Label(self, text="Hello, world!")
        self.label.pack()

        # Create a button widget
        self.button = tk.Button(self, text="Click Me!", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        # Update the text of the label widget
        self.label.config(text="Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My GUI")

    my_gui = MyGUI(root)
    my_gui.pack()

    root.mainloop()
