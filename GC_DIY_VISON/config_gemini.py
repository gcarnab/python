# --- CONFIGURAZIONE HARDWARE ---
CAMERA_INDEX = 0          # Indice della webcam (0=integrata, 1=esterna Logitech)
PIXEL_TO_MM = 0.5         # Fattore di conversione (da calibrare con righello)

# --- PARAMETRI DI VISIONE ---
MIN_AREA = 1500           # Area minima in pixel per ignorare il rumore
# Range Colore Bianco in HSV (Hue, Saturation, Value)
LOWER_WHITE = [0, 0, 160] 
UPPER_WHITE = [180, 60, 255]

# --- STILE GRAFICO ---
COLOR_CONTOUR = (0, 255, 0)  # Verde
COLOR_POINTER = (0, 0, 255)  # Rosso
COLOR_TEXT = (255, 255, 255) # Bianco
COLOR_AXES = (100, 100, 100)  # Grigio per gli assi