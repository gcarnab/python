import cv2
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

def main() :

    full = cv2.imread('DATA/sammy.jpg')
    full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

    #plt.imshow(full)
    # The Template to Match
    face= cv2.imread('DATA/sammy_face.jpg')
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    height, width,channels = face.shape

    # All the 6 methods for comparison in a list
    # Note how we are using strings, later on we'll use the eval() function to convert to function
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']    
    
    for m in methods:
    
        # Create a copy of the image
        full_copy = full.copy()
        
        # Get the actual function instead of the string
        method = eval(m)

        # Apply template Matching with the method
        res = cv2.matchTemplate(full_copy,face,method)
        
        # Grab the Max and Min values, plus their locations
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # Set up drawing of Rectangle
        
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        # Notice the coloring on the last 2 left hand side images.
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc    
        else:
            top_left = max_loc
            
        # Assign the Bottom Right of the rectangle
        bottom_right = (top_left[0] + width, top_left[1] + height)

        # Draw the Red Rectangle
        cv2.rectangle(full_copy,top_left, bottom_right, 255, 10)

        # Plot the Images
        plt.subplot(131)
        plt.imshow(res)
        plt.title('Result of Template Matching')
        
        plt.subplot(132)
        plt.imshow(full_copy)
        plt.title('Detected Point')
        plt.suptitle(m)

        # Plot the Images
        plt.subplot(133)
        plt.imshow(face)
        plt.title('Template')  
    
    plt.show()

if __name__ == "__main__":
   main()