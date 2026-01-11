# ===============================
# WEBCAM
# ===============================

CAMERA_INDEX = 0              # 0 = webcam principale
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# ===============================
# THRESHOLDING
# ===============================

# Soglia per rilevare oggetti chiari su sfondo scuro
THRESHOLD_VALUE = 200         # Prova valori tra 170 e 220
THRESHOLD_MAX = 255

# Area minima per considerare valido un oggetto
MIN_OBJECT_AREA = 500

# ===============================
# GRAFICA
# ===============================

WINDOW_NAME = "Sistema Visione Artificiale - Premi ESC per uscire"

# Colori (BGR)
COLOR_CONTOUR = (0, 255, 0)   # Verde
COLOR_MARKER = (0, 0, 255)    # Rosso
COLOR_TEXT = (255, 0, 0)  # Bianco

# ===============================
# TESTO
# ===============================

TEXT_SCALE = 0.6
TEXT_THICKNESS = 2

# ===============================
# ASSI CARTESIANI
# ===============================

SHOW_AXES = True

AXIS_COLOR = (255, 255, 0)     
AXIS_THICKNESS = 1
AXIS_TEXT_SCALE = 0.5

# ===============================
# AREA OGGETTO
# ===============================

SHOW_OBJECT_AREA = True
