import tkinter as tk
from tkinter import filedialog, ttk
import cv2
from PIL import Image, ImageTk
from modules.GCVisionService import GCVisionService
import matplotlib.pyplot as plt
import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler

class GCVisionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard 2.0")

        # Set up logging
        self.log_folder = "C:/GCDATA/DEV/vscode-workspace/python/GC_VISION/GC_VSION_DASHBOARD/log"        
        self.log_flag = True
        self.configure_logging()

        # Create a GCVisionService instance
        self.vision_service = GCVisionService()
        self.setup_global_settings()
        self.setup_feature_settings()

        ########## GUI CREATION ##############

        # Create tabs
        self.notebook = ttk.Notebook(root)

        #---------------------> TAB 1 <------------------------------
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Home")

        # Menu-like frame in Tab 1
        self.menu_frame = ttk.Frame(self.tab1)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        button1 = ttk.Button(self.menu_frame, text="Acquire frame", command=self.acquire_callback)
        button1.pack(pady=10,side=tk.LEFT)

        # Add buttons or other widgets as menu items
        button2 = ttk.Button(self.menu_frame, text="Edge Detection", command=self.edge_detection_callback)
        button2.pack(pady=5,side=tk.LEFT)

        button3 = ttk.Button(self.menu_frame, text="Template Matching", command=self.template_matching_callback)
        button3.pack(pady=5,side=tk.LEFT)

        button4 = ttk.Button(self.menu_frame, text="Grid Detection", command=self.grid_detection_callback)
        button4.pack(pady=5,side=tk.LEFT)

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

        #--------------------------> General Settings <------------------------------------------

        #---------------------> TAB 2 <------------------------------
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Settings")

        # Create a Frame for settings
        self.settings_frame = ttk.LabelFrame(self.tab2, text="General Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.settings_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        #------------> Button to apply settings <--------------

        self.apply_settings_button = ttk.Button(self.settings_frame, text="Apply Settings", command=self.apply_settings)
        self.apply_settings_button.pack(side=tk.LEFT, padx=5)

        #------------> Settings widgets <--------------

        use_live_view_checkbox = ttk.Checkbutton(self.settings_frame, text="Use Live View", variable=self.use_live_view_for_detection)
        use_live_view_checkbox.pack(pady=5, anchor=tk.W)

        # Add radio buttons for detection features
        self.selected_feature = tk.StringVar()
        self.selected_feature.set("edge_detection")  # Set the default feature

        edge_detection_radio = ttk.Radiobutton(self.settings_frame, text="Edge Detection", variable=self.selected_feature, value="edge_detection")
        edge_detection_radio.pack(side=tk.LEFT, padx=5)

        face_detection_radio = ttk.Radiobutton(self.settings_frame, text="Template matching", variable=self.selected_feature, value="template_matching")
        face_detection_radio.pack(side=tk.LEFT, padx=5)

        #--------------------------> Edge Detection settings <------------------------------------------

        # Create a LabelFrame for Edge Detection settings
        self.edge_detection_frame = ttk.LabelFrame(self.tab2, text="Edge Detection Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.edge_detection_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add settings widgets inside edge_detection_frame
        self.ksize_label = ttk.Label(self.edge_detection_frame, text="Blur Kernel Size (ksize):")
        self.ksize_label.grid(row=0, column=0, pady=5, padx=5)

        # Slider for controlling ksize
        self.ksize_slider = ttk.Scale(self.edge_detection_frame, from_=1, to=10, variable=self.blur_ksize, orient=tk.HORIZONTAL, length=50, command=self.update_ksize_label)
        self.ksize_slider.grid(row=0, column=1, pady=5, padx=5)

        # Label to display ksize value
        self.ksize_value_label = ttk.Label(self.edge_detection_frame, text=f"Current: {self.blur_ksize.get()}")
        self.ksize_value_label.grid(row=0, column=2, pady=5, padx=5)

        #--------------------------> Template Matching settings <------------------------------------------

        # Create a LabelFrame for Template Matching settings
        self.template_matching_frame = ttk.LabelFrame(self.tab2, text="Template Matching Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.template_matching_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a Combobox for choosing template matching method
        self.method_label = ttk.Label(self.template_matching_frame, text="TM Method:")
        self.method_label.grid(row=0, column=0, pady=5, padx=5)

        # Create a Combobox for choosing the method
        self.method_combobox = ttk.Combobox(self.template_matching_frame, values=list(GCVisionService.TemplateMatchingMethods.__members__.keys()))
        self.method_combobox.set("TM_CCOEFF_NORMED")  # Set the default method
        self.method_combobox.grid(row=0, column=1, pady=5, padx=5)


        #--------------------------> Grid Detection settings <------------------------------------------

        # Create a LabelFrame for Grid Detection settings
        self.grid_detection_frame = ttk.LabelFrame(self.tab2, text="Grid Detection Settings", width=self.canvas_width, height=self.canvas_height, padding=(1, 1, 1, 1))
        self.grid_detection_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add settings widgets inside Grid Detection
        self.grid_width_label = ttk.Label(self.grid_detection_frame, text="Grid Width :")
        self.grid_width_label.grid(row=0, column=0, pady=5, padx=5)
        # Slider 
        self.grid_width_slider = ttk.Scale(self.grid_detection_frame, from_=1, to=10, variable=self.grid_width, orient=tk.HORIZONTAL, length=50, command=self.update_grid_width_label)
        self.grid_width_slider.grid(row=0, column=1, pady=5, padx=5)
        # Label to display slider values
        self.grid_width_value_label = ttk.Label(self.grid_detection_frame, text=f"Current: {self.grid_width.get()}")
        self.grid_width_value_label.grid(row=0, column=2, pady=5, padx=5)

        self.grid_height_label = ttk.Label(self.grid_detection_frame, text="Grid Height :")
        self.grid_height_label.grid(row=1, column=0, pady=5, padx=5)
        # Slider 
        self.grid_height_slider = ttk.Scale(self.grid_detection_frame, from_=1, to=10, variable=self.grid_height, orient=tk.HORIZONTAL, length=50, command=self.update_grid_height_label)
        self.grid_height_slider.grid(row=1, column=1, pady=5, padx=5)
        # Label to display slider values
        self.grid_height_value_label = ttk.Label(self.grid_detection_frame, text=f"Current: {self.grid_height.get()}")
        self.grid_height_value_label.grid(row=1, column=2, pady=5, padx=5)

        ####### Open the video stream #######
        self.cap = cv2.VideoCapture(0)

        # Start video streaming
        self.video_stream()

        # Pack the notebook for positioning widgets
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.logger.info("Canvas width: %s height : %s", self.canvas_width, self.canvas_height)

    def setup_global_settings(self):
        try:        
            if self.log_flag :
                self.logger.info(">>> setup_global_settings")    
                     
            ########## GLOBAL SETTINGS ##############

            self.initial_folder = "C:/GCDATA/DEV/vscode-workspace/python/GC_VISION/GC_VSION_DASHBOARD/data"
            
            # Set the dimensions of the main window
            window_width = 1024  # Change this to your desired width
            window_height = 480  # Change this to your desired height
            self.root.geometry(f"{window_width}x{window_height}")

            # canvas dimentions
            self.canvas_width = 320
            self.canvas_height = 240

        except Exception as e:
            self.logger.exception("### Error in setup_global_settings: %s", str(e))

    def setup_feature_settings(self):
        try:        
            if self.log_flag :
                self.logger.info(">>> setup_feature_settings")    

            ##### FEATURES SETTINGS VARIABLES #####

            self.use_live_view_for_detection = tk.BooleanVar()
            self.use_live_view_for_detection.set(False)
            self.blur_ksize = tk.IntVar(value=5)  
            self.template_matching_method = tk.StringVar()
            self.grid_width = tk.IntVar(value=7)
            self.grid_height = tk.IntVar(value=7)

            # Add a trace to call a method whenever a setting is changed
            self.use_live_view_for_detection.trace_add("write", self.highlight_apply_settings_button)
            self.blur_ksize.trace_add("write", self.highlight_apply_settings_button)
            self.template_matching_method.trace_add("write", self.highlight_apply_settings_button)
            self.grid_width.trace_add("write", self.highlight_apply_settings_button)
            self.grid_height.trace_add("write", self.highlight_apply_settings_button)
            # Add a trace for the method_combobox
            #self.method_combobox.trace_add("write", self.highlight_apply_settings_button)
            self.method_combobox.bind("<<ComboboxSelected>>", lambda event: self.highlight_apply_settings_button())

        except Exception as e:
            self.logger.exception("### Error in setup_feature_settings: %s", str(e))
    
    def video_stream(self): 
        try:        
            if self.log_flag :
                self.logger.info(">>> video_stream")   

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

        except cv2.error as cv2_error:
            self.logger.error("### OpenCV error in video_stream: %s", str(cv2_error))
        except Exception as e:
            self.logger.exception("### Error in video_stream: %s", str(e))

    ########### CALLBACK FUNCTIONS ###########
            
    def edge_detection_callback(self):
        try :
            if self.log_flag :
                self.logger.info(">>> edge_detection_callback")

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
        
        except cv2.error as cv2_error:
            self.logger.error("### OpenCV error in edge_detection_callback: %s", str(cv2_error))
        except Exception as e:
            self.logger.exception("### Error in edge_detection_callback: %s", str(e))

    def acquire_callback(self):
        try :
            if self.log_flag :
                self.logger.info(">>> acquire_callback")     

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
        except Exception as e:
            self.logger.exception("### Error in acquire_callback: %s", str(e))

    def template_matching_callback(self):
        try :
            if self.log_flag :
                self.logger.info(">>> template_matching_callback")     

            template_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Template Image",
                                                    filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
            
            full_image_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Full Image",
                                                    filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
                
            if template_path and full_image_path:

                # Perform edge detection and display the result in image_processing_canvas
                result = self.vision_service.match_template(template_path, full_image_path, self.image_processing_canvas, self.image_source_canvas, self.template_matching_method.get())
                template_image, heatmap_image = result

                # Display the detection result on canvas
                self.display_image_on_canvas(template_image, self.image_source_canvas)
                self.display_image_on_canvas(heatmap_image, self.image_processing_canvas)    
        except Exception as e:
            self.logger.exception("### Error in template_matching_callback: %s", str(e))

    def grid_detection_callback(self):
        try :
            if self.log_flag :
                self.logger.info(">>> grid_detection_callback")     

            image_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Grid Image",
                                                    filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
            
            #full_image_path = filedialog.askopenfilename(initialdir=self.initial_folder, title="Select Full Image",
            #                                        filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
            
            
            if image_path :
                # Perform grid detection and display the result in image_processing_canvas
                result_image = self.vision_service.grid_detection(image_path , self.image_processing_canvas, self.image_source_canvas)

                # Display the detection result on canvas
                #self.display_image_on_canvas(image_path, self.image_source_canvas)
                self.display_image_on_canvas(result_image, self.image_processing_canvas) 

        except Exception as e:
            self.logger.exception("### Error in grid_detection_callback: %s", str(e))                

    def display_image_on_canvas(self, image, canvas):
        try :
            if self.log_flag :
                self.logger.info(">>> display_image_on_canvas")     

            # Resize the image to fit the canvas
            resized_image = cv2.resize(image, (self.canvas_width, self.canvas_height))
                                
            # Convert the NumPy array to PhotoImage
            photo = ImageTk.PhotoImage(image=Image.fromarray(resized_image))

            # Update the canvas with the new image
            canvas.config(width=self.canvas_width, height=self.canvas_width)
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.photo = photo

        except Exception as e:
            self.logger.exception("### Error in display_image_on_canvas: %s", str(e))               

    ############# SETTINGS LABELS VALUES ###########
        
    def update_ksize_label(self, value):
        if self.log_flag :
            self.logger.info(">>> update_ksize_label")     

        self.ksize_value_label.config(text=f"Current: {self.blur_ksize.get()}")

    def update_grid_width_label(self, value):
        if self.log_flag :
            self.logger.info(">>> update_grid_width_label")             
        self.grid_width_value_label.config(text=f"Current: {self.grid_width.get()}")

    def update_grid_height_label(self, value):
        if self.log_flag :
            self.logger.info(">>> update_grid_height_label")              
        self.grid_height_value_label.config(text=f"Current: {self.grid_height.get()}")

    def highlight_apply_settings_button(self, *args):
        if self.log_flag :
            self.logger.info(">>> highlight_apply_settings_button")   

        # Change the appearance of the apply_settings_button to highlight it
        self.apply_settings_button.configure(
            style="Highlight.TButton",  # Use a custom style for highlighting
            state=tk.NORMAL  # Enable the button
        )

    def apply_settings(self):
        try:         
            if self.log_flag :
                self.logger.info(">>> apply_settings")   

            # Get the current values from settings sliders
            self.vision_service.blur_ksize.set(self.blur_ksize.get())

            self.template_matching_method.set(getattr(GCVisionService.TemplateMatchingMethods, self.method_combobox.get()))
            print("self.template_matching_method" ,  self.template_matching_method)
            print("self.template_matching_method type" ,  type(self.template_matching_method))

            self.vision_service.grid_width.set(self.grid_width.get())
            self.vision_service.grid_height.set(self.grid_height.get())

            # Reset the appearance of the apply_settings_button
            self.apply_settings_button.configure(
                style="TButton",  # Reset to the default style
                state=tk.DISABLED  # Disable the button after applying settings
            )
        except Exception as e:
            # Log the exception
            self.logger.exception("### Error applying settings: %s", str(e))

    def configure_logging(self):
        log_file_path = os.path.join(self.log_folder, "gc_vision_dashboard.log")
        print("log_file_path", log_file_path)

        # Create the log folder if it doesn't exist
        os.makedirs(self.log_folder, exist_ok=True)

        # Configure the logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Use a rotating log file with a new file every day
        handler = TimedRotatingFileHandler(log_file_path, when="midnight", interval=1, backupCount=7)
        handler.setLevel(logging.DEBUG)

        # Create a formatter and add it to the handler
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(handler)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("Highlight.TButton", background="yellow", font=("Helvetica", 12, "bold"), foreground="black")
    app = GCVisionDashboard(root)
    root.mainloop()
