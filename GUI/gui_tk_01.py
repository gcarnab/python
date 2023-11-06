import tkinter as tk
from tkinter import colorchooser
import random

class CirclePanel(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super(CirclePanel, self).__init__(parent, *args, **kwargs)
        self.circle_color = "red"  # Initial circle color (red)
        self.bind("<Configure>", self.draw_circle)
    
    def set_circle_color(self, color):
        self.circle_color = color
        self.draw_circle()
    
    def draw_circle(self, event=None):
        self.delete("all")
        circle_radius = min(self.winfo_width(), self.winfo_height()) // 2
        circle_center = self.winfo_width() // 2, self.winfo_height() // 2
        self.create_oval(circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                          circle_center[0] + circle_radius, circle_center[1] + circle_radius,
                          fill=self.circle_color)

class CircleFrame(tk.Tk):
    def __init__(self):
        super(CircleFrame, self).__init__()
        self.title("Random Color Circle Plotter")
        self.geometry("300x300")
        
        self.circle_panel = CirclePanel(self, bg="white", width=300, height=300)
        self.circle_panel.pack(expand=True, fill=tk.BOTH)
        
        color_picker_button = tk.Button(self, text="Choose Color", command=self.choose_color)
        color_picker_button.pack(pady=10)
        
        random_color_button = tk.Button(self, text="Random Color", command=self.random_color)
        random_color_button.pack()
    
    def choose_color(self):
        color = colorchooser.askcolor()[1]  # Open color chooser dialog
        if color:
            self.circle_panel.set_circle_color(color)
    
    def random_color(self):
        random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255),
                                                    random.randint(0, 255),
                                                    random.randint(0, 255))
        self.circle_panel.set_circle_color(random_color)

if __name__ == "__main__":
    app = CircleFrame()
    app.mainloop()
