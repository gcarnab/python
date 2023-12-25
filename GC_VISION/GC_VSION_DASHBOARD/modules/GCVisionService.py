import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

class GCVisionService:
    """
    Class for OpenCV 
    @author : GCARNAB

    """   
    class TemplateMatchingMethods(Enum):
        TM_CCOEFF = cv2.TM_CCOEFF
        TM_CCOEFF_NORMED = cv2.TM_CCOEFF_NORMED
        TM_CCORR = cv2.TM_CCORR
        TM_CCORR_NORMED = cv2.TM_CCORR_NORMED
        TM_SQDIFF = cv2.TM_SQDIFF
        TM_SQDIFF_NORMED = cv2.TM_SQDIFF_NORMED  

    def __init__(self):
        # Initialize any necessary attributes or configurations here
        self.cap = cv2.VideoCapture(0)
        self.blur_ksize = tk.IntVar(value=5)
        self.methods = self.TemplateMatchingMethods    
        self.grid_width = tk.IntVar(value=7)
        self.grid_height = tk.IntVar(value=7)

    def get_live_view_frame(self):
        _, frame = self.cap.read()
        return frame
    """
    Method for EDGE DETECTION
    @description : Perform edge detection using Canny
    @params : frame
    @return :
    @author : GCARNAB

    """   
    def edge_detection(self, image, processing_canvas, source_canvas, use_live):
        # Check if live view should be used
        if use_live:
            print("Perform edge detection using live view frames")
            #img = self.get_live_view_frame()

            # Convert the image to grayscale for edge detection
            gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Convert the image to RGB 
            img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Perform edge detection
            edges = cv2.Canny(image=gray_frame, threshold1=0, threshold2=255)
        else:
            print("Perform edge detection using image")
            # Load the image           
            img = cv2.imread(image)
            ksize_value = self.blur_ksize.get()
            blurred_img = cv2.blur(img,ksize=(ksize_value,ksize_value))

            # Convert the image to RGB 
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Convert the image to grayscale for edge detection
            gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Calculate the median pixel value
            med_val = np.median(img) 
            # Lower bound is either 0 or 70% of the median value, whicever is higher
            lower = int(max(0, 0.7* med_val))
            # Upper bound is either 255 or 30% above the median value, whichever is lower
            upper = int(min(255,1.3 * med_val))
            edges = cv2.Canny(image=blurred_img, threshold1=lower , threshold2=upper+100)


        # Resize the images to fit the canvases
        resized_edges = self.resize_image(edges, processing_canvas.winfo_reqwidth(), processing_canvas.winfo_reqheight())
        resized_img_rgb = self.resize_image(img_rgb, source_canvas.winfo_reqwidth(), source_canvas.winfo_reqheight())

        # Convert the edge-detected image to PhotoImage format
        #image = Image.fromarray(edges)
        #photo = ImageTk.PhotoImage(image)

        # Convert the NumPy arrays to PhotoImages
        edges_photo = ImageTk.PhotoImage(image=Image.fromarray(resized_edges))
        img_rgb_photo = ImageTk.PhotoImage(image=Image.fromarray(resized_img_rgb))

        processing_canvas.delete("all")  # Clear the canvas
        source_canvas.delete("all")  # Clear the canvas

        # Update the canvases with the new images
        processing_canvas.config(width=edges_photo.width(), height=edges_photo.height())
        source_canvas.config(width=img_rgb_photo.width(), height=img_rgb_photo.height())

        processing_canvas.create_image(0, 0, anchor=tk.NW, image=edges_photo)
        processing_canvas.photo = edges_photo

        source_canvas.create_image(0, 0, anchor=tk.NW, image=img_rgb_photo)
        source_canvas.photo = img_rgb_photo

        return edges

    def get_live_view_frame(self):
        # Simulate live view frames (replace this with your live view implementation)
        # For demonstration, return a black frame
        return np.zeros((480, 640, 3), dtype=np.uint8)
    
    def resize_image(self, img, target_width, target_height):
        """
        Resize the image while maintaining its aspect ratio.
        """
        original_height, original_width = img.shape[:2]
        aspect_ratio = original_width / original_height

        if target_width / aspect_ratio <= target_height:
            new_width = int(target_width)
            new_height = int(target_width / aspect_ratio)
        else:
            new_width = int(target_height * aspect_ratio)
            new_height = int(target_height)

        resized_img = cv2.resize(img, (new_width, new_height))
        return resized_img

    def match_template(self, template_path, full_image_path, processing_canvas, source_canvas, method):
 
        # All the 6 methods for comparison in a list
        # Note how we are using strings, later on we'll use the eval() function to convert to function
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        
        # Read images
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        full_image = cv2.imread(full_image_path, cv2.IMREAD_COLOR)
        height, width,channels = template.shape

        # Convert images to RGB format
        template_rgb = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        full_image_rgb = cv2.cvtColor(full_image, cv2.COLOR_BGR2RGB)

        # Perform template matching
        #result = cv2.matchTemplate(full_image_rgb, template_rgb, cv2.TM_CCOEFF_NORMED)
        result = cv2.matchTemplate(full_image_rgb, template_rgb, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Draw a rectangle around the matched area
        h, w = template_rgb.shape[:2]
        #h, w = template.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw the Red Rectangle
        #cv2.rectangle(full_image_rgb,top_left, bottom_right, 255, 10)        
        cv2.rectangle(full_image_rgb, top_left, bottom_right, (255, 0, 0), 2)

        # Convert the image to PIL format
        heatmap_image = Image.fromarray(full_image_rgb)

        # Generate the heatmap image
        heatmap_image = self.generate_heatmap_image(result)

        # Plot the Images
        plt.subplot(131)
        plt.imshow(template_rgb)
        plt.title('Template')

        plt.subplot(132)
        plt.imshow(full_image_rgb)
        plt.title('Full')

        plt.subplot(133)
        plt.imshow(heatmap_image)
        plt.title('Heatmap')
        plt.show()

        return template_rgb,full_image_rgb
        
    
    def generate_heatmap_image(self, heatmap):
        # Normalize the heatmap values to the range [0, 255]
        heatmap_normalized = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)

        # Convert the heatmap to a 3-channel image
        heatmap_image = cv2.applyColorMap(np.uint8(heatmap_normalized), cv2.COLORMAP_JET)

        # Convert the image to PIL format
        return Image.fromarray(heatmap_image)
    
    def grid_detection(self, image, processing_canvas, source_canvas) :
        print("Perform grid_detection")
        # Load the image           
        img = cv2.imread(image)

        grid_width = self.grid_width.get()
        grid_height = self.grid_height.get()

        #found, corners = cv2.findChessboardCorners(img,(7,7))
        found, corners = cv2.findCirclesGrid(img, (grid_width,grid_height), cv2.CALIB_CB_SYMMETRIC_GRID)

        img_copy = img.copy()
        
        #result_image = cv2.drawChessboardCorners(img_copy, (7, 7), corners, found)
        result_image = cv2.drawChessboardCorners(img_copy, (grid_width, grid_height), corners, found)

        # Create a figure with 1 row and 3 columns, and set the figsize
        fig, axs = plt.subplots(1, 3, figsize=(10, 10))  # Adjust the figsize as needed

        # Plot the Images with adjusted aspect ratios
        axs[0].imshow(img)
        axs[0].set_title('Grid')
        #axs[0].set_aspect('auto')  # Adjust aspect ratio as needed

        axs[1].imshow(result_image)
        axs[1].set_title('Result')
        #axs[1].set_aspect('auto')  # Adjust aspect ratio as needed

        # Add a blank subplot to increase space between the images
        axs[2].axis('off')  # Turn off axis for the blank subplot

        # Adjust layout
        plt.tight_layout()

        plt.show()

        return result_image