import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def detect_faces(frame, canvas_heatmap):
    
    # Perform face detection using Haarcascades
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    base_path = 'C:/GCDATA/DEV/vscode-workspace/python/GC_VISION/GC_VSION_DASHBOARD/assets/'
    xml_file_name = 'haarcascade_frontalface_default.xml'
    full_xml_path = base_path + xml_file_name
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + xml_file_name)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the heatmap
    heatmap = np.zeros_like(gray)
    for (x, y, w, h) in faces:
        heatmap[y:y+h, x:x+w] += 1

    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    photo_heatmap = ImageTk.PhotoImage(image=Image.fromarray(heatmap))
    canvas_heatmap.create_image(0, 0, anchor=tk.NW, image=photo_heatmap)
