import tkinter as tk

class MyGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a text entry widget
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a listbox widget
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        # Create a button widget
        self.button = tk.Button(self, text="Add", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        # Get the text from the text entry widget
        text = self.entry.get()

        # Add the text to the listbox widget
        self.listbox.insert(tk.END, text)

        # Clear the text entry widget
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My GUI")

    my_gui = MyGUI(root)
    my_gui.pack()

    root.mainloop()
