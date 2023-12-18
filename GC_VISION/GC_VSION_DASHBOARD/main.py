import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from modules import face_detection, edge_detection, camera_settings
from modules.template_matching import TemplateMatching

class CanvasWithBorder(tk.Frame):
    def __init__(self, master, title):
        tk.Frame.__init__(self, master)
        
        # Create a title label
        self.label_title = tk.Label(self, text=title)
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)
        
        # Create the canvas
        self.canvas = tk.Canvas(self, width=200, height=150, borderwidth=2, relief="solid")  
        # Adjust the width and height as needed
        self.canvas.pack(side=tk.TOP, padx=10, pady=10)

class OpenCVDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("GC Vision Dashboard Rel.(1.0)")

        # Set the dimensions of the main window
        window_width = 1000  # Change this to your desired width
        window_height = 480  # Change this to your desired height
        self.root.geometry(f"{window_width}x{window_height}")

        # Allow the window to be resizable
        self.root.resizable(width=True, height=True)

        # Initialize OpenCV camera
        self.cap = cv2.VideoCapture(0)

        # Create instances for Modules
        self.template_matching = TemplateMatching()

        # Create menu
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.cv_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="OpenCV Modules", menu=self.cv_menu)

        # Add OpenCV modules to the menu
        #self.cv_menu.add_command(label="Face Detection", command=self.show_face_detection)
        #self.cv_menu.add_command(label="Edge Detection", command=self.show_edge_detection)
        self.cv_menu.add_command(label="Template Matching Method", command=self.choose_template_method)
        self.cv_menu.add_command(label="Template Matching", command=self.show_template_matching)
        self.cv_menu.add_separator()
        self.cv_menu.add_command(label="Camera Settings", command=self.show_camera_settings)
        self.cv_menu.add_separator()
        self.cv_menu.add_command(label="Exit", command=root.destroy)

        # Create canvas with border for live preview
        self.frame_live_preview = CanvasWithBorder(root, "Live Preview")
        self.frame_live_preview.pack(side=tk.LEFT, padx=10, pady=10)

        # Create canvas with border for heatmap
        self.frame_heatmap = CanvasWithBorder(root, "Heatmap")
        self.frame_heatmap.pack(side=tk.LEFT, padx=10, pady=10)

        # Create canvas with border for template matching
        self.frame_template_matching = CanvasWithBorder(root, "Matching : Pattern")
        self.frame_template_matching.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_full_template_matching = CanvasWithBorder(root, "Matching : Full image")
        self.frame_full_template_matching.pack(side=tk.LEFT, padx=10, pady=10)

        # Create button for photo snapshot
        self.snapshot_button = ttk.Button(root, text="Take Snapshot", command=self.take_snapshot)
        self.snapshot_button.pack(side=tk.BOTTOM, pady=10)

        # Start video stream
        self.show_frame()

    def option1_callback(self):
        print("Option 1 selected")

    def option2_callback(self):
        print("Option 2 selected")

    def create_edge_detection_tab(self):
        # TODO: Implement edge detection tab
        pass

    def create_object_detection_tab(self):
        # TODO: Implement object detection tab
        pass
    
    def show_frame(self):
        ret, frame = self.cap.read()

        if ret:
            # Display live preview
            canvas_width, canvas_height = self.frame_live_preview.canvas.winfo_width(), self.frame_live_preview.canvas.winfo_height()
            self.photo_live_preview = self.convert_to_photo(frame, canvas_width, canvas_height)
            self.frame_live_preview.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_live_preview)

            # Perform face detection
            #face_detection.detect_faces(frame, self.canvas_heatmap)

        self.root.after(10, self.show_frame)

    def convert_to_photo(self, frame, canvas_width, canvas_height):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Resize the frame to fit the canvas while maintaining the aspect ratio
        frame = cv2.resize(frame, (canvas_width, canvas_height))
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        return photo

    def show_face_detection(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform face detection
            face_detection.detect_faces(frame, self.canvas_heatmap)

            # Display live preview
            canvas_width, canvas_height = self.canvas_live_preview.winfo_width(), self.canvas_live_preview.winfo_height()
            self.photo_live_preview = self.convert_to_photo(frame, canvas_width, canvas_height)
            self.canvas_live_preview.create_image(0, 0, anchor=tk.NW, image=self.photo_live_preview)


    def show_edge_detection(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform edge detection
            edge_detection.detect_edges(frame, self.canvas_heatmap)

            # Display live preview
            canvas_width, canvas_height = self.canvas_live_preview.winfo_width(), self.canvas_live_preview.winfo_height()
            self.photo_live_preview = self.convert_to_photo(frame, canvas_width, canvas_height)
            self.canvas_live_preview.create_image(0, 0, anchor=tk.NW, image=self.photo_live_preview)

    def show_image_on_canvas(self, image, canvas):
        # Resize the image to fit the canvas
        canvas_width, canvas_height = canvas.winfo_width(), canvas.winfo_height()
        resized_image  = image.resize((canvas_width, canvas_height), Image.LANCZOS)

        # Convert the image to PhotoImage
        photo_image = ImageTk.PhotoImage(image=resized_image)

        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
        canvas.image = photo_image  # Save a reference to prevent garbage collection

    def choose_template_method(self):
        # Let the user choose the template matching method
        # method = self.template_matching.choose_method()
        method = self.template_matching.choose_method(self.root)
        
        #if method is not None:
        #    # Perform template matching with the chosen method
        #    self.template_matching.match_template("path_to_template_image", "path_to_full_image", self.canvas, method)

    def show_template_matching(self):
        # Let the user choose the template matching method
        #method = self.template_matching.choose_method()

        ret, frame = self.cap.read()
        if ret:
            # Browse for template image file
            template_path = filedialog.askopenfilename(title="Select Template Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

            # Browse for full image file
            full_image_path = filedialog.askopenfilename(title="Select Full Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

            if template_path and full_image_path:

                # Load the template image
                template_image = Image.open(template_path)        

                # Load the full image
                full_image = Image.open(full_image_path)     

                # Rotate the full image (adjust the angle as needed)
                rotated_full_image = full_image.rotate(90, resample=Image.BICUBIC)

                # Display the template image on the template matching canvas
                self.show_image_on_canvas(template_image, self.frame_template_matching.canvas)

                # Display the full image on the template matching canvas
                self.show_image_on_canvas(rotated_full_image, self.frame_full_template_matching.canvas)

                # Perform template matching
                self.template_matching.match_template(template_path, full_image_path, self.frame_heatmap.canvas, "")
      
                # Perform face detection
                ret, frame = self.cap.read()
                face_detection.detect_faces(frame, self.frame_heatmap.canvas)

    def show_camera_settings(self):
        camera_settings.show_settings(self.cap)

    def take_snapshot(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("GC_VISION/GC_VSION_DASHBOARD/data/snapshot.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print("Snapshot taken.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenCVDashboard(root)
    root.mainloop()
