"""
========================================
SISTEMA DI VISIONE ARTIFICIALE - MAIN
========================================

Rileva oggetti tramite webcam, mostra mirino e coordinate.

Controlli tastiera:
- ESC: Chiudi programma
- SPAZIO: Pausa/Riprendi
- 'c': Cattura screenshot
- 'd': Modalità debug ON/OFF
- 'r': Rileva ROSSO
- 'b': Rileva BIANCO
- 'v': Rileva VERDE
- 'z': Rileva BLU

Autore: Progetto Didattico Visione Artificiale
"""

import cv2
import numpy as np
import time
import config_claude as config  # Importa il file di configurazione 

# Banner iniziale
print("=" * 60)
print("  SISTEMA DI VISIONE ARTIFICIALE")
print("  Progetto Didattico - Scuole Superiori")
print("=" * 60)
print(f"✓ OpenCV versione: {cv2.__version__}")
print(f"✓ Modalità rilevamento: {config.MODALITA}")
print("=" * 60)


class SistemaVisioneArtificiale:
    """
    Sistema completo per rilevamento oggetti e calcolo coordinate.
    """
    
    def __init__(self):
        """Inizializza webcam e variabili."""
        print("\n🔧 Inizializzazione sistema...")
        
        # Stato sistema
        self.paused = False
        self.debug_mode = config.SHOW_DEBUG
        self.frame_count = 0
        self.screenshot_count = 0
        
        # Modalità colore attuale
        self.modalita = config.MODALITA
        self.aggiorna_range_colore()
        
        # FPS tracking
        self.fps = 0
        self.fps_time = time.time()
        self.fps_frame_count = 0
        
        # Ultima rilevazione (per ridurre print console)
        self.ultima_rilevazione = None
        
        # Apri webcam
        self.camera = cv2.VideoCapture(config.CAMERA_INDEX)
        
        if not self.camera.isOpened():
            raise Exception("❌ ERRORE: Impossibile aprire webcam!")
        
        # Configura webcam
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
        self.camera.set(cv2.CAP_PROP_FPS, config.CAMERA_FPS)
        
        print("✓ Webcam inizializzata!")
        print(f"  - Risoluzione: {config.CAMERA_WIDTH}x{config.CAMERA_HEIGHT}")
        print(f"  - Cercando oggetti: {self.modalita}")
        print("\n" + "=" * 60)
        print("CONTROLLI:")
        print("  ESC    = Esci")
        print("  SPAZIO = Pausa")
        print("  c      = Screenshot")
        print("  d      = Debug ON/OFF")
        print("  r/b/v/z = Cambia colore (Rosso/Bianco/Verde/Blu)")
        print("=" * 60 + "\n")
    
    
    def aggiorna_range_colore(self):
        """Aggiorna i range HSV in base alla modalità corrente."""
        if self.modalita in config.COLOR_RANGES:
            self.color_lower = config.COLOR_RANGES[self.modalita]["lower"]
            self.color_upper = config.COLOR_RANGES[self.modalita]["upper"]
        else:
            # Default: bianco
            self.color_lower = config.COLOR_RANGES["BIANCO"]["lower"]
            self.color_upper = config.COLOR_RANGES["BIANCO"]["upper"]
    
    
    def pixel_to_mm(self, x_pixel, y_pixel):
        """
        Converte coordinate pixel → millimetri.
        
        Args:
            x_pixel: coordinata X in pixel
            y_pixel: coordinata Y in pixel
            
        Returns:
            tuple: (x_mm, y_mm) coordinate in millimetri
        """
        # Calcola offset dall'origine
        delta_x = x_pixel - config.ORIGIN_X
        delta_y = config.ORIGIN_Y - y_pixel  # Inverti Y (schermo vs robot)
        
        # Converti in mm
        x_mm = delta_x * config.MM_PER_PIXEL
        y_mm = delta_y * config.MM_PER_PIXEL
        
        return (x_mm, y_mm)
    
    
    def rileva_oggetto(self, frame):
        """
        Rileva oggetto nel frame usando filtro colore.
        
        Args:
            frame: immagine BGR dalla webcam
            
        Returns:
            tuple: (cx, cy, area, contorno) se trovato, None altrimenti
        """
        # STEP 1: Converti BGR → HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # STEP 2: Applica blur per ridurre rumore
        hsv_blur = cv2.GaussianBlur(hsv, (config.BLUR_KERNEL, config.BLUR_KERNEL), 0)
        
        # STEP 3: Crea maschera binaria (bianco = colore target)
        maschera = cv2.inRange(hsv_blur, self.color_lower, self.color_upper)
        
        # STEP 4: Pulizia morfologica
        kernel = np.ones((5, 5), np.uint8)
        maschera = cv2.morphologyEx(maschera, cv2.MORPH_OPEN, kernel, iterations=2)
        maschera = cv2.morphologyEx(maschera, cv2.MORPH_CLOSE, kernel, iterations=2)
        
        # Mostra maschera se debug attivo
        if self.debug_mode:
            cv2.imshow("🔧 DEBUG - Maschera Colore", maschera)
        
        # STEP 5: Trova contorni
        contorni, _ = cv2.findContours(maschera, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contorni) == 0:
            return None
        
        # STEP 6: Trova contorno più grande
        contorno_max = max(contorni, key=cv2.contourArea)
        area = cv2.contourArea(contorno_max)
        
        # STEP 7: Verifica dimensione
        if not (config.MIN_AREA < area < config.MAX_AREA):
            return None
        
        # STEP 8: Calcola centro (centroide)
        M = cv2.moments(contorno_max)
        if M["m00"] == 0:  # Evita divisione per zero
            return None
        
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        
        return (cx, cy, area, contorno_max)
    
    
    def disegna_mirino(self, frame, x, y):
        """
        Disegna mirino a croce sul punto (x, y).
        
        Args:
            frame: immagine su cui disegnare
            x, y: coordinate centro mirino
        """
        size = config.CROSSHAIR_SIZE
        color = config.COLOR_CROSSHAIR
        thickness = config.LINE_THICKNESS
        
        # Croce
        cv2.line(frame, (x - size, y), (x + size, y), color, thickness)
        cv2.line(frame, (x, y - size), (x, y + size), color, thickness)
        
        # Cerchio centrale
        cv2.circle(frame, (x, y), 8, color, thickness)
        cv2.circle(frame, (x, y), 3, color, -1)  # Centro pieno
    
    
    def disegna_origine(self, frame):
        """Disegna punto origine robot per riferimento."""
        ox, oy = config.ORIGIN_X, config.ORIGIN_Y
        
        # Croce piccola
        cv2.line(frame, (ox-10, oy), (ox+10, oy), (255, 255, 255), 1)
        cv2.line(frame, (ox, oy-10), (ox, oy+10), (255, 255, 255), 1)
        
        # Etichetta
        cv2.putText(frame, "ORIGINE (0,0)", (ox+15, oy-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    
    
    def disegna_info(self, frame, x_px, y_px, x_mm, y_mm, area):
        """
        Disegna tutte le informazioni su frame.
        
        Args:
            frame: immagine
            x_px, y_px: coordinate pixel
            x_mm, y_mm: coordinate millimetri
            area: area oggetto
        """
        font = cv2.FONT_HERSHEY_SIMPLEX
        y_offset = 30
        
        # Header
        cv2.rectangle(frame, (0, 0), (640, 150), (0, 0, 0), -1)  # Sfondo nero
        
        # Modalità colore
        testo_modo = f"Modalita: {self.modalita}"
        cv2.putText(frame, testo_modo, (10, y_offset), font, 0.7, (255, 255, 255), 2)
        y_offset += 30
        
        # Coordinate pixel
        testo_px = f"Pixel:  X={x_px:4d}px  Y={y_px:4d}px"
        cv2.putText(frame, testo_px, (10, y_offset), font, 0.6, config.COLOR_TEXT, 2)
        y_offset += 30
        
        # Coordinate millimetri (IMPORTANTE!)
        testo_mm = f"Robot:  X={x_mm:7.1f}mm  Y={y_mm:7.1f}mm"
        cv2.putText(frame, testo_mm, (10, y_offset), font, 0.7, config.COLOR_TEXT_OK, 2)
        y_offset += 30
        
        # Area
        testo_area = f"Area: {int(area):6d} px^2"
        cv2.putText(frame, testo_area, (10, y_offset), font, 0.6, config.COLOR_TEXT, 2)
        
        # FPS
        if config.SHOW_FPS:
            testo_fps = f"FPS: {self.fps:.1f}"
            cv2.putText(frame, testo_fps, (10, frame.shape[0] - 10),
                        font, 0.6, (255, 255, 255), 2)
    
    
    def stampa_console(self, x_mm, y_mm, x_px, y_px, area):
        """
        Stampa coordinate su console VSCode.
        
        Args:
            x_mm, y_mm: coordinate millimetri
            x_px, y_px: coordinate pixel
            area: area oggetto
        """
        # Stampa solo ogni N frame per non intasare console
        if self.frame_count % config.PRINT_EVERY_N_FRAMES == 0:
            print(f"🎯 OGGETTO RILEVATO | "
                  f"Pixel: X={x_px:4d} Y={y_px:4d} | "
                  f"Robot: X={x_mm:7.1f}mm Y={y_mm:7.1f}mm | "
                  f"Area={int(area):6d}px²")
    
    
    def calcola_fps(self):
        """Calcola FPS reali."""
        self.fps_frame_count += 1
        if self.fps_frame_count >= 30:
            tempo_ora = time.time()
            self.fps = self.fps_frame_count / (tempo_ora - self.fps_time)
            self.fps_time = tempo_ora
            self.fps_frame_count = 0
    
    
    def gestisci_tastiera(self, frame):
        """
        Gestisce input tastiera.
        
        Returns:
            bool: False per uscire, True per continuare
        """
        key = cv2.waitKey(1) & 0xFF
        
        # ESC = esci
        if key == 27:
            print("\n👋 Chiusura programma...")
            return False
        
        # SPAZIO = pausa
        elif key == ord(' '):
            self.paused = not self.paused
            print(f"⏸  {'IN PAUSA' if self.paused else 'RIPRESO'}")
        
        # 'c' = screenshot
        elif key == ord('c'):
            filename = f"screenshot_{self.screenshot_count:03d}.jpg"
            cv2.imwrite(filename, frame)
            self.screenshot_count += 1
            print(f"📸 Screenshot salvato: {filename}")
        
        # 'd' = debug
        elif key == ord('d'):
            self.debug_mode = not self.debug_mode
            print(f"🔧 Debug: {'ON' if self.debug_mode else 'OFF'}")
            if not self.debug_mode:
                cv2.destroyWindow("🔧 DEBUG - Maschera Colore")
        
        # Cambi colore
        elif key == ord('r'):
            self.modalita = "ROSSO"
            self.aggiorna_range_colore()
            print(f"🔴 Modalità: ROSSO")
        
        elif key == ord('b'):
            self.modalita = "BIANCO"
            self.aggiorna_range_colore()
            print(f"⚪ Modalità: BIANCO")
        
        elif key == ord('v'):
            self.modalita = "VERDE"
            self.aggiorna_range_colore()
            print(f"🟢 Modalità: VERDE")
        
        elif key == ord('z'):
            self.modalita = "BLU"
            self.aggiorna_range_colore()
            print(f"🔵 Modalità: BLU")
        
        return True
    
    
    def esegui(self):
        """Loop principale del programma."""
        try:
            while True:
                # Leggi frame
                ret, frame = self.camera.read()
                
                if not ret:
                    print("❌ Errore lettura frame!")
                    break
                
                # Incrementa contatore
                self.frame_count += 1
                
                # Se non in pausa, processa
                if not self.paused:
                    # Disegna origine robot
                    self.disegna_origine(frame)
                    
                    # Rileva oggetto
                    risultato = self.rileva_oggetto(frame)
                    
                    if risultato is not None:
                        x_px, y_px, area, contorno = risultato
                        
                        # Converti in mm
                        x_mm, y_mm = self.pixel_to_mm(x_px, y_px)
                        
                        # Disegna contorno (se debug)
                        if self.debug_mode:
                            cv2.drawContours(frame, [contorno], -1, config.COLOR_BBOX, 2)
                        
                        # Disegna mirino
                        self.disegna_mirino(frame, x_px, y_px)
                        
                        # Disegna info
                        self.disegna_info(frame, x_px, y_px, x_mm, y_mm, area)
                        
                        # Stampa console
                        if config.PRINT_COORDINATES:
                            self.stampa_console(x_mm, y_mm, x_px, y_px, area)
                    
                    else:
                        # Nessun oggetto rilevato
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        testo = f"Nessun oggetto {self.modalita} rilevato"
                        cv2.putText(frame, testo, (10, 30), font, 0.8, (0, 0, 255), 2)
                        
                        # Suggerimento
                        hint = f"Premi: r=Rosso b=Bianco v=Verde z=Blu"
                        cv2.putText(frame, hint, (10, 60), font, 0.5, (255, 255, 255), 1)
                
                else:
                    # Mostra PAUSA
                    cv2.putText(frame, "IN PAUSA - Premi SPAZIO",
                                (config.CAMERA_WIDTH//2 - 150, config.CAMERA_HEIGHT//2),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                
                # Calcola FPS
                self.calcola_fps()
                
                # Mostra frame
                cv2.imshow("Sistema Visione Artificiale - Premi ESC per uscire", frame)
                
                # Gestisci tastiera
                if not self.gestisci_tastiera(frame):
                    break
        
        finally:
            # Pulizia
            self.camera.release()
            cv2.destroyAllWindows()
            print("\n✓ Risorse liberate")
            print("=" * 60)
            print("Programma terminato correttamente")
            print("=" * 60)


# ====================================
# MAIN
# ====================================

if __name__ == "__main__":
    try:
        sistema = SistemaVisioneArtificiale()
        sistema.esegui()
        
    except KeyboardInterrupt:
        print("\n⚠ Interrotto da utente (Ctrl+C)")
    
    except Exception as e:
        print(f"\n❌ ERRORE: {e}")
        print("\nControlla:")
        print("  1. Webcam collegata")
        print("  2. Nessun altro programma usa la webcam")
        print("  3. Drivers webcam installati")
        print("  4. Permessi accesso webcam su Windows")
    
    finally:
        print("\n👋 Arrivederci!")