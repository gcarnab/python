"""
========================================
CONFIGURAZIONI DEL SISTEMA DI VISIONE
========================================

Questo file contiene tutti i parametri configurabili del sistema.
Gli studenti possono modificare questi valori per sperimentare.

Autore: Progetto Didattico Visione Artificiale
Target: Studenti Scuole Superiori
"""

# ====================================
# PARAMETRI WEBCAM
# ====================================

# Risoluzione della webcam (larghezza x altezza in pixel)
CAMERA_WIDTH = 640      # Larghezza in pixel
CAMERA_HEIGHT = 480     # Altezza in pixel

# Indice della webcam
# 0 = prima webcam, 1 = seconda webcam USB
CAMERA_INDEX = 0

# Frame rate (fotogrammi al secondo)
CAMERA_FPS = 30


# ====================================
# CALIBRAZIONE SPAZIALE
# ====================================

# Millimetri per pixel (da calibrare con oggetto di dimensioni note)
# Esempio: Se un oggetto di 50mm appare largo 100px → MM_PER_PIXEL = 0.5
MM_PER_PIXEL = 0.5      

# Punto di origine del robot (centro immagine di default)
ORIGIN_X = CAMERA_WIDTH // 2   # 320 pixel
ORIGIN_Y = CAMERA_HEIGHT // 2  # 240 pixel


# ====================================
# RILEVAMENTO OGGETTO - COLORE
# ====================================

# MODALITÀ DI RILEVAMENTO:
# "BIANCO" - Rileva oggetti bianchi/chiari (fogli, oggetti bianchi)
# "ROSSO"  - Rileva oggetti rossi
# "BLU"    - Rileva oggetti blu
# "VERDE"  - Rileva oggetti verdi

MODALITA = "BIANCO"  # ← CAMBIA QUESTO per diversi colori!

# Range HSV per diversi colori
# Formato: (Hue_min, Saturation_min, Value_min), (Hue_max, Saturation_max, Value_max)

COLOR_RANGES = {
    "BIANCO": {
        "lower": (0, 0, 200),      # Bassa saturazione, alta luminosità
        "upper": (180, 30, 255)    # Qualsiasi tonalità ma quasi bianco
    },
    "ROSSO": {
        "lower": (0, 100, 100),
        "upper": (10, 255, 255)
    },
    "BLU": {
        "lower": (100, 100, 100),
        "upper": (130, 255, 255)
    },
    "VERDE": {
        "lower": (40, 100, 100),
        "upper": (80, 255, 255)
    },
    "GIALLO": {
        "lower": (20, 100, 100),
        "upper": (30, 255, 255)
    }
}

# Ottieni range colore selezionato
COLOR_LOWER_HSV = COLOR_RANGES[MODALITA]["lower"]
COLOR_UPPER_HSV = COLOR_RANGES[MODALITA]["upper"]


# ====================================
# FILTRI DI RILEVAMENTO
# ====================================

# Area minima oggetto (pixel²)
# Per foglio A4 distante ~40cm: circa 10000-30000 px²
MIN_AREA = 5000          

# Area massima oggetto (pixel²)
MAX_AREA = 200000        

# Filtro blur per ridurre rumore
BLUR_KERNEL = 15         # Deve essere dispari (5, 7, 9, 11, 15)


# ====================================
# PARAMETRI VISUALIZZAZIONE
# ====================================

# Colori per disegni (formato BGR)
COLOR_CROSSHAIR = (0, 255, 0)       # Verde mirino
COLOR_BBOX = (255, 0, 0)            # Blu riquadro
COLOR_TEXT = (0, 255, 255)          # Giallo testo
COLOR_TEXT_OK = (0, 255, 0)         # Verde quando rileva

# Spessore linee
LINE_THICKNESS = 2

# Dimensione mirino (in pixel dal centro)
CROSSHAIR_SIZE = 30


# ====================================
# MODALITÀ DEBUG
# ====================================

# Mostra finestra debug con maschera
SHOW_DEBUG = True

# Stampa coordinate su console (può essere verboso)
PRINT_COORDINATES = True

# Mostra FPS su video
SHOW_FPS = True

# Intervallo stampa console (ogni N frame, per ridurre output)
PRINT_EVERY_N_FRAMES = 10