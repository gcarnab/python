import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class OpenCVDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard")

        # Initialize OpenCV camera
        self.cap = cv2.VideoCapture(0)

        # Create menu
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.cv_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="OpenCV Modules", menu=self.cv_menu)

        # Add OpenCV modules to the menu
        self.cv_menu.add_command(label="Face Detection", command=self.face_detection)
        self.cv_menu.add_command(label="Edge Detection", command=self.edge_detection)

        # Create canvas to display video feed
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        # Start video stream
        self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()

        if ret:
            self.photo = self.convert_to_photo(frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.after(10, self.show_frame)

    def convert_to_photo(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        return photo

    def face_detection(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform face detection using Haarcascades
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the result
            self.photo = self.convert_to_photo(frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def edge_detection(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform edge detection using Canny
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)

            # Display the result
            self.photo = self.convert_to_photo(edges)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenCVDashboard(root)
    root.mainloop()
