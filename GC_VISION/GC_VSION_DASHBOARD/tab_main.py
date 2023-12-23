import tkinter as tk
from tkinter import filedialog, ttk
import cv2
from PIL import Image, ImageTk
from modules.GCVisionService import GCVisionService

class GCVisionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard 2.0")
        self.vision_service = GCVisionService()
        self.initial_folder = "C:/GCDATA/DEV/vscode-workspace/python/GC_VISION/GC_VSION_DASHBOARD/data"

        # Set the dimensions of the main window
        window_width = 800  # Change this to your desired width
        window_height = 480  # Change this to your desired height
        self.root.geometry(f"{window_width}x{window_height}")

        # canvas dimentions
        self.canvas_width = 320
        self.canvas_height = 240

        # Create tabs
        self.notebook = ttk.Notebook(root)

        # Tab 1
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Home")

        # Menu-like frame in Tab 1
        self.menu_frame = ttk.Frame(self.tab1)
        #self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Add buttons or other widgets as menu items
        button1 = ttk.Button(self.menu_frame, text="Option 1", command=self.option1_callback)
        button1.pack(pady=10,side=tk.LEFT)

        button2 = ttk.Button(self.menu_frame, text="Option 2", command=self.option2_callback)
        button2.pack(pady=10,side=tk.LEFT)

        # Add more buttons as needed

        # Content frame in Tab 1

        self.content_frame  = ttk.Frame(self.tab1,padding=(5, 5, 5, 5), relief="solid", borderwidth=2)
        self.content_frame .pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a Frame for "Live View" canvas and label
        self.live_view_frame = ttk.Frame(self.content_frame,padding=(5, 5, 5, 5), relief="solid", borderwidth=2)
        self.live_view_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Canvas for displaying live video frames
        self.live_view_canvas = tk.Canvas(self.live_view_frame, width=self.canvas_width, height=self.canvas_height, borderwidth=2, relief="solid")
        self.live_view_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Label for "Live View"
        self.live_view_label = ttk.Label(self.live_view_frame, text="Live View")
        self.live_view_label.pack(pady=5)

        # Create a Frame for "Image Processing" canvas and label
        self.image_processing_frame = ttk.Frame(self.content_frame,padding=(5, 5, 5, 5), relief="solid", borderwidth=2)
        self.image_processing_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Canvas for image processing
        self.image_processing_canvas = tk.Canvas(self.image_processing_frame, width=self.canvas_width, height=self.canvas_height, borderwidth=2, relief="solid")
        self.image_processing_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Label for "Image Processing"
        self.image_processing_label = ttk.Label(self.image_processing_frame, text="Image Processing")
        self.image_processing_label.pack(pady=5)

        # Open the video stream
        self.cap = cv2.VideoCapture(0)

        # Start video streaming
        self.video_stream()

        # Add content to the content frame
        #label = ttk.Label(self.content_frame, text="Content goes here")
        #label.pack(pady=10, padx=10)

        # Tab 2
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Tab 2")

        # Add buttons or widgets to Tab 2
        button_tab2 = ttk.Button(self.tab2, text="Button in Tab 2", command=self.button_tab2_callback)
        button_tab2.pack(pady=10)

        # Add content to Tab 2
        label2 = ttk.Label(self.tab2, text="Content for Tab 2")
        label2.pack(pady=10, padx=10)

        # Pack the notebook for positioning widgets
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def video_stream(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert BGR image to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize the frame
            frame_resized = cv2.resize(frame_rgb, (self.canvas_width, self.canvas_height))

            # Convert to PhotoImage format
            image = Image.fromarray(frame_resized)
            photo = ImageTk.PhotoImage(image)

            # Update the Canvas with the new frame
            self.live_view_canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.live_view_canvas.photo = photo

            self.image_processing_canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.image_processing_canvas.photo = photo

            # Schedule the next frame update
            self.root.after(10, self.video_stream)

    ########### CALLBACK FUNCTIONS ###########
    def option1_callback(self):
        print("Option 1 selected")
        # Clear the existing content in the Image Processing Canvas
        self.image_processing_canvas.delete("all")

        # Perform edge detection and update the Image Processing Canvas
        edge_image = self.perform_edge_detection(True)

        self.show_image_on_canvas(edge_image, self.image_processing_canvas)


    def perform_edge_detection(self, image_flag=None):
        if image_flag:
            # Read the image from the specified path
            #original_image = cv2.imread(image_path)

            # Browse for template image file
            original_image = filedialog.askopenfilename(
                title="Select Source Image", 
                filetypes=[("Image files", "*.png;*.jpg;*.jpeg")], 
                initialdir=self.initial_folder)
            
            source_image = cv2.imread(original_image)
            print("original_image", original_image)
            print("source_image", source_image)

            result = self.vision_service.detect_edges(source_image)

        else:
            # Capture a frame from the video stream
            _, original_image = self.cap.read()
      
        return result
    
    def show_image_on_canvas(self, image, canvas):
        # Convert the image to PhotoImage format
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image)

        # Update the Canvas with the new image
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.photo = photo

    def option2_callback(self):
        print("Option 2 selected")

    def button_tab2_callback(self):
        print("Button in Tab 2 clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = GCVisionDashboard(root)
    root.mainloop()
