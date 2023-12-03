import cv2
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np

class TemplateMatching:

    def __init__(self):
        self.methods = {
            'cv2.TM_CCOEFF': cv2.TM_CCOEFF,
            'cv2.TM_CCOEFF_NORMED': cv2.TM_CCOEFF_NORMED,
            'cv2.TM_CCORR': cv2.TM_CCORR,
            'cv2.TM_CCORR_NORMED': cv2.TM_CCORR_NORMED,
            'cv2.TM_SQDIFF': cv2.TM_SQDIFF,
            'cv2.TM_SQDIFF_NORMED': cv2.TM_SQDIFF_NORMED
        }

    def match_template(self, template_path, full_image_path, canvas, selected_method):

        # All the 6 methods for comparison in a list
        # Note how we are using strings, later on we'll use the eval() function to convert to function
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        
        # Let the user choose the template matching method
        #selected_method = self.choose_method(tk.Tk())
        #selected_method = cv2.TM_CCOEFF
        #selected_method = eval("0")
        #print("selected_method = " + str(selected_method))

        if selected_method is not None:
            # Read images
            template = cv2.imread(template_path, cv2.IMREAD_COLOR)
            full_image = cv2.imread(full_image_path, cv2.IMREAD_COLOR)
            height, width,channels = template.shape

            # Convert images to RGB format
            template_rgb = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
            full_image_rgb = cv2.cvtColor(full_image, cv2.COLOR_BGR2RGB)

            # Perform template matching
            result = cv2.matchTemplate(full_image_rgb, template_rgb, cv2.TM_CCOEFF_NORMED)
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

            # Display the heatmap on the canvas
            self.show_image_on_canvas(heatmap_image, canvas)

    def generate_heatmap_image(self, heatmap):
        # Normalize the heatmap values to the range [0, 255]
        heatmap_normalized = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)

        # Convert the heatmap to a 3-channel image
        heatmap_image = cv2.applyColorMap(np.uint8(heatmap_normalized), cv2.COLORMAP_JET)

        # Convert the image to PIL format
        return Image.fromarray(heatmap_image)

    def show_image_on_canvas(self, image, canvas):
        # Resize the image to fit the canvas
        canvas_width, canvas_height = canvas.winfo_width(), canvas.winfo_height()
        resized_image = image.resize((canvas_width, canvas_height), Image.ANTIALIAS)

        # Convert the image to PhotoImage
        photo_image = ImageTk.PhotoImage(image=resized_image)

        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
        canvas.image = photo_image  # Save a reference to prevent garbage collection      

    def choose_method(self, root):
        # Create a simple GUI to choose the method
        selected_method = [self.methods['cv2.TM_CCOEFF']]  # Use a list to store the selected method

        def on_method_change(*args):
            # Callback function to update the selected method
            selected_method[0] = method_var.get()

        # Create the dropdown menu
        method_var = tk.StringVar()
        method_var.set('cv2.TM_CCOEFF')  # Set the default method
        method_menu = ttk.Combobox(root, textvariable=method_var, values=list(self.methods.keys()))
        method_menu.bind("<<ComboboxSelected>>", on_method_change)
        method_menu.pack()

        # Display the GUI
        root.wait_window(root)

        # Return the selected method
        return selected_method[0]