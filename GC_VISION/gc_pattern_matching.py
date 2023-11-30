import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carica l'immagine del pattern (quello che vuoi cercare)
pattern_image = cv2.imread('GC_VISION/DATA/gc_face.jpg', cv2.IMREAD_GRAYSCALE)
pattern_image = cv2.cvtColor(pattern_image, cv2.COLOR_BGR2RGB)
height, width,channels = pattern_image.shape

full_image = cv2.imread('GC_VISION/DATA/gc_full_image.jpg')
full_image = cv2.cvtColor(full_image, cv2.COLOR_BGR2RGB)

# All the 6 methods for comparison in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    
    # Create a copy of the image
    full_copy = full_image.copy()
    
    # Get the actual function instead of the string
    method = eval(m)

    # Apply template Matching with the method
    res = cv2.matchTemplate(full_copy,pattern_image,method)
    
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
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Heatmap result of Template Matching')
    
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detected Point')
    plt.suptitle(m)
    plt.show()


'''
# Inizializza il rilevatore di feature ORB
orb = cv2.ORB_create()

# Trova i punti chiave e i descrittori con ORB
keypoints_pattern, descriptors_pattern = orb.detectAndCompute(pattern_image, None)

# Inizializza il rilevatore di feature ORB per la webcam
cap = cv2.VideoCapture(0)

while True:
    # Legge un frame dalla webcam
    ret, frame = cap.read()

    # Converti il frame in scala di grigi
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Trova i punti chiave e i descrittori con ORB per il frame della webcam
    keypoints_frame, descriptors_frame = orb.detectAndCompute(gray_frame, None)

     # Verifica che ci siano punti chiave e descrittori validi
    if keypoints_frame and descriptors_frame is not None:
        # Inizializza il matcher di feature BF (Brute-Force)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Esegue il matching dei descrittori
        matches = bf.match(descriptors_pattern, descriptors_frame)

        # Ordina i match in base alla loro distanza
        matches = sorted(matches, key=lambda x: x.distance)

        # Disegna i primi 10 match sul frame della webcam
        img_matches = cv2.drawMatches(
            pattern_image, keypoints_pattern, gray_frame, keypoints_frame, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        # Mostra il frame con i match
        cv2.imshow('Pattern Matching', img_matches)

    # Interrompe il loop se si preme 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia la cattura e chiude la finestra
cap.release()
cv2.destroyAllWindows()

'''