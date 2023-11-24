import tkinter as tk

root = tk.Tk()
root.style = tk.ttk.Style()
root.style.theme_use("vista")

class MyGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a text entry widget
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a listbox widget
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        # Create a button to add items to the listbox
        self.add_button = tk.Button(self, text="Add", command=self.on_add_button_click)
        self.add_button.pack()

        # Create a button to remove items from the listbox
        self.remove_button = tk.Button(self, text="Remove", command=self.on_remove_button_click)
        self.remove_button.pack()

    def on_add_button_click(self):
        # Get the text from the text entry widget
        text = self.entry.get()

        # Add the text to the listbox widget
        self.listbox.insert(tk.END, text)

        # Clear the text entry widget
        self.entry.delete(0, tk.END)

    def on_remove_button_click(self):
        # Get the selected item from the listbox widget
        selected_item_index = self.listbox.selection_get()

        print(selected_item_index)

        # If there is a selected item, remove it from the listbox widget
        if selected_item_index:
            self.listbox.delete(selected_item_index[0])


if __name__ == "__main__":
    root = tk.Tk()
    root.title("My GUI")

    my_gui = MyGUI(root)
    my_gui.pack()

    root.mainloop()
