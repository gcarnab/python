import tkinter as tk
from tkinter import filedialog, ttk
import cv2
from PIL import Image, ImageTk
from modules.GCVisionService import GCVisionService
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time

class GCVisionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard 2.0")
        self.log_flag = True

        # Create a GCVisionService instance
        self.vision_service = GCVisionService()

        ##### SETTINGS VARIABLES #####
        self.use_live_view_for_detection = tk.BooleanVar()
        self.use_live_view_for_detection.set(False)
        self.blur_ksize = tk.IntVar(value=5)  # Initial value for ksize

        self.initial_folder = "C:/GCDATA/DEV/vscode-workspace/python/GC_VISION/GC_VSION_DASHBOARD/data"

        # Set the dimensions of the main window
        window_width = 1024  # Change this to your desired width
        window_height = 480  # Change this to your desired height
        self.root.geometry(f"{window_width}x{window_height}")

        # canvas dimentions
        self.canvas_width = 320
        self.canvas_height = 240

        # Create tabs
        self.notebook = ttk.Notebook(root)

        ################ Tab 1
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Home")

        # Menu-like frame in Tab 1
        self.menu_frame = ttk.Frame(self.tab1)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        button1 = ttk.Button(self.menu_frame, text="Acquire frame", command=self.acquire_callback)
        button1.pack(pady=10,side=tk.LEFT)

        # Add buttons or other widgets as menu items
        button2 = ttk.Button(self.menu_frame, text="Edge Detection", command=self.edge_detection_callback)
        button2.pack(pady=10,side=tk.LEFT)

        button3 = ttk.Button(self.menu_frame, text="Template Matching", command=self.template_matching_callback)
        button3.pack(pady=10,side=tk.LEFT)

        # Create a Frame for canvases on Tab1
        self.content_frame  = ttk.Frame(self.tab1,padding=(1, 1, 1, 1), relief="solid", borderwidth=2)
        self.content_frame .pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #---------------------------------------------------
        # Create a Frame for "Live View" canvas and label
        self.live_view_frame = ttk.Frame(self.content_frame, width=self.canvas_width, height=self.canvas_height,padding=(1, 1, 1, 1), relief="solid", borderwidth=2)
        self.live_view_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Canvas for displaying live video frames
        self.live_view_canvas = tk.Canvas(self.live_view_frame, width=self.canvas_width, height=self.canvas_height, borderwidth=2, relief="solid")
        self.live_view_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Label for "Live View"
        self.live_view_label = ttk.Label(self.live_view_frame, text="Live View")
        self.live_view_label.pack(pady=5)

        #---------------------------------------------------
        # Create a Frame for "Image Source" canvas and label
        self.image_source_frame = ttk.Frame(self.content_frame, width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1), relief="solid", borderwidth=2)
        self.image_source_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Canvas for Image Source
        self.image_source_canvas = tk.Canvas(self.image_source_frame, width=self.canvas_width, height=self.canvas_height, borderwidth=2, relief="solid")
        self.image_source_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Label for "Image Source"
        self.image_source_label = ttk.Label(self.image_source_frame, text="Image Source")
        self.image_source_label.pack(pady=5)

        #---------------------------------------------------
        # Create a Frame for "Image Processing" canvas and label
        self.image_processing_frame = ttk.Frame(self.content_frame, width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1), relief="solid", borderwidth=2)
        self.image_processing_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Canvas for image processing
        self.image_processing_canvas = tk.Canvas(self.image_processing_frame, width=self.canvas_width, height=self.canvas_height, borderwidth=2, relief="solid")
        self.image_processing_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Label for "Image Processing"
        self.image_processing_label = ttk.Label(self.image_processing_frame, text="Image Processing")
        self.image_processing_label.pack(pady=5)

        ################# Tab 2: Settings
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Settings")

        # Create a Frame for settings
        self.settings_frame = ttk.LabelFrame(self.tab2, text="General Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.settings_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Add widgets for settings
        use_live_view_checkbox = ttk.Checkbutton(self.settings_frame, text="Use Live View", variable=self.use_live_view_for_detection)
        use_live_view_checkbox.pack(pady=5, anchor=tk.W)

        # Add radio buttons for detection features
        self.selected_feature = tk.StringVar()
        self.selected_feature.set("edge_detection")  # Set the default feature

        edge_detection_radio = ttk.Radiobutton(self.settings_frame, text="Edge Detection", variable=self.selected_feature, value="edge_detection")
        edge_detection_radio.pack(side=tk.LEFT, padx=5)

        face_detection_radio = ttk.Radiobutton(self.settings_frame, text="Template matching", variable=self.selected_feature, value="template_matching")
        face_detection_radio.pack(side=tk.LEFT, padx=5)

        # Create a LabelFrame for Edge Detection settings
        self.edge_detection_frame = ttk.LabelFrame(self.tab2, text="Edge Detection Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.edge_detection_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add settings widgets inside edge_detection_frame
        self.ksize_label = ttk.Label(self.edge_detection_frame, text="Blur Kernel Size (ksize):")
        self.ksize_label.grid(row=0, column=0, pady=5, padx=5)

        # Slider for controlling ksize
        self.ksize_slider = ttk.Scale(self.edge_detection_frame, from_=0, to=10, variable=self.blur_ksize, orient=tk.HORIZONTAL, length=200, command=self.update_ksize_label)
        self.ksize_slider.grid(row=0, column=1, pady=5, padx=5)

        # Label to display ksize value
        self.ksize_value_label = ttk.Label(self.edge_detection_frame, text=f"Current ksize: {self.blur_ksize.get()}")
        self.ksize_value_label.grid(row=0, column=2, pady=5, padx=5)

        # Button to apply settings
        apply_settings_button = ttk.Button(self.edge_detection_frame, text="Apply Settings", command=self.apply_settings)
        apply_settings_button.grid(row=1, column=0, columnspan=2, pady=10)


        ####### Open the video stream #######
        self.cap = cv2.VideoCapture(0)

        # Start video streaming
        self.video_stream()

        # Pack the notebook for positioning widgets
        self.notebook.pack(fill=tk.BOTH, expand=True)

        print("self.canvas_height", self.canvas_height)

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

            # Schedule the next frame update
            self.root.after(10, self.video_stream)

    ########### CALLBACK FUNCTIONS ###########
            
    def edge_detection_callback(self):
        if self.log_flag :
            print("edge_detection_callback selected")  

        if self.use_live_view_for_detection.get() :
            #frame = self.cap.read()
            self.vision_service.edge_detection(self.cap.read(), self.image_processing_canvas, self.image_source_canvas, self.use_live_view_for_detection.get())

        else :
            # Call the edge_detection method from GCVisionService
            image_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select an Image",
                                                    filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
            if image_path:
                # Perform edge detection and display the result in image_processing_canvas
                self.vision_service.edge_detection(image_path, self.image_processing_canvas, self.image_source_canvas, self.use_live_view_for_detection.get())

    def acquire_callback(self):
        if self.log_flag :
            print("acquire_callback selected")     

        ret, frame = self.cap.read()

        if ret:
            # Generate a timestamp
            timestamp = time.strftime("%Y%m%d%H%M%S")
            filename = f"{self.initial_folder}/captured_frame_{timestamp}.jpg"
            # Save the frame to a file (you can customize the filename and directory)
            cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Display the source image on the source_canvas
            self.display_image_on_canvas(frame, self.image_source_canvas)

            if self.selected_feature.get() == "edge_detection":
                if self.log_flag :
                    print("Perform edge_detection")                 
                # Call the edge_detection method from GCVisionService with image_path set to None
                edges = self.vision_service.edge_detection(frame, self.image_processing_canvas, self.image_source_canvas, True)

                # Display the edge detection result on the processing_canvas
                self.display_image_on_canvas(edges, self.image_processing_canvas)

            elif self.selected_feature.get() == "template_matching":
                if self.log_flag :
                    print("Perform template_matching")
                # You can implement face detection logic here
                pass
        else:
            print("Failed to capture a frame from the live view.")

    def template_matching_callback(self):
        if self.log_flag :
            print("template_matching_callback selected")

        # Call the edge_detection method from GCVisionService
        template_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Template Image",
                                                filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
        
        # Call the edge_detection method from GCVisionService
        full_image_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Full Image",
                                                filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
        
        
        if template_path and full_image_path:
            # Perform edge detection and display the result in image_processing_canvas
            result = self.vision_service.match_template(template_path, full_image_path , self.image_processing_canvas, self.image_source_canvas)
            template_image, heatmap_image = result
            # Display the detection result on canvas
            self.display_image_on_canvas(template_image, self.image_source_canvas)
            self.display_image_on_canvas(heatmap_image, self.image_processing_canvas)    

    def display_image_on_canvas(self, image, canvas):
        if self.log_flag :
            print("display_image_on_canvas selected")

        # Resize the image to fit the canvas
        resized_image = cv2.resize(image, (self.canvas_width, self.canvas_height))
                             
        # Convert the NumPy array to PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(resized_image))

        # Update the canvas with the new image
        canvas.config(width=self.canvas_width, height=self.canvas_width)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.photo = photo

    def update_ksize_label(self, value):
        # Update the label displaying ksize value
        self.ksize_value_label.config(text=f"Current ksize: {self.blur_ksize.get()}")

    def apply_settings(self):
        if self.log_flag :
            print("apply_settings selected")

        # Get the current value of ksize from the slider
        print("apply_settings self.blur_ksize.get()= ", self.blur_ksize.get())
        self.vision_service.blur_ksize.set(self.blur_ksize.get())



if __name__ == "__main__":
    root = tk.Tk()
    app = GCVisionDashboard(root)
    root.mainloop()
