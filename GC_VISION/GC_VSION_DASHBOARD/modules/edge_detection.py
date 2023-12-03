import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def detect_edges(frame, canvas_heatmap):
    # Perform edge detection using Canny
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Display the heatmap
    heatmap = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    photo_heatmap = ImageTk.PhotoImage(image=Image.fromarray(heatmap))
    canvas_heatmap.create_image(0, 0, anchor=tk.NW, image=photo_heatmap)
