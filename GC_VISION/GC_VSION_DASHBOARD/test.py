import tkinter as tk
from tkinter import ttk, filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

class GCVisionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard")

        self.cap = cv2.VideoCapture(0)  # Open default camera (change index if using a different camera)

        # Set the dimensions of the main window
        window_width = 1000
        window_height = 480
        self.root.geometry(f"{window_width}x{window_height}")

        # Create tabs
        self.notebook = ttk.Notebook(root)

        # Tab 1: Home
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Home")

        # Create a Frame for controls
        self.controls_frame = ttk.Frame(self.tab1, padding=(10, 10, 10, 10))
        self.controls_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add widgets for controls
        acquire_button = ttk.Button(self.controls_frame, text="Acquire", command=self.acquire_callback)
        acquire_button.pack(pady=10)

        # Create a Frame for canvases
        self.canvases_frame = ttk.Frame(self.tab1, padding=(10, 10, 10, 10))
        self.canvases_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a Canvas for live view
        self.live_view_canvas = tk.Canvas(self.canvases_frame, width=400, height=300, borderwidth=2, relief="solid")
        self.live_view_canvas.pack(side=tk.LEFT, padx=10)
        self.live_view_label = ttk.Label(self.live_view_canvas, text="Live View")
        self.live_view_label.pack(pady=5)

        # Create a Canvas for source image
        self.source_canvas = tk.Canvas(self.canvases_frame, width=400, height=300, borderwidth=2, relief="solid")
        self.source_canvas.pack(side=tk.LEFT, padx=10)
        self.source_label = ttk.Label(self.source_canvas, text="Source Image")
        self.source_label.pack(pady=5)

        # Create a Canvas for edge detection result
        self.processing_canvas = tk.Canvas(self.canvases_frame, width=400, height=300, borderwidth=2, relief="solid")
        self.processing_canvas.pack(side=tk.LEFT, padx=10)
        self.processing_label = ttk.Label(self.processing_canvas, text="Edge Detection Result")
        self.processing_label.pack(pady=5)

        # Pack the notebook for positioning widgets
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def acquire_callback(self):
        # Capture a frame from the live view
        ret, frame = self.cap.read()

        if ret:
            # Save the frame to a file (you can customize the filename and directory)
            filename = "captured_frame.jpg"
            cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Display the source image on the source_canvas
            self.display_image_on_canvas(frame, self.source_canvas)

            # Perform edge detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(image=gray_frame, threshold1=127, threshold2=127)

            # Display the edge detection result on the processing_canvas
            self.display_image_on_canvas(edges, self.processing_canvas)
        else:
            print("Failed to capture a frame from the live view.")

    def display_image_on_canvas(self, image, canvas):
        # Resize the image to fit the canvas
        resized_image = cv2.resize(image, (canvas.winfo_reqwidth(), canvas.winfo_reqheight()))

        # Convert the NumPy array to PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(resized_image))

        # Update the canvas with the new image
        canvas.config(width=photo.width(), height=photo.height())
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.photo = photo


if __name__ == "__main__":
    root = tk.Tk()
    app = GCVisionDashboard(root)
    root.mainloop()
