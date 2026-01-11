import cv2
import numpy as np
import config_gemini as config # Importiamo il nostro file di configurazione locale

def main():
    # Inizializzazione Webcam usando il parametro da config
    cap = cv2.VideoCapture(config.CAMERA_INDEX)

    if not cap.isOpened():
        print(f"ERRORE: Webcam con indice {config.CAMERA_INDEX} non trovata.")
        return

    print("--- SISTEMA DI VISIONE MODULARE AVVIATO ---")
    print("Premi 'ESC' per uscire.")

    while True:
        ret, frame = cap.read()

        # --- DISEGNO ASSI CARTESIANI (ORIGINE 0,0 IN ALTO A SINISTRA) ---
        height, width = frame.shape[:2]

        # Disegna Asse X (Orizzontale in alto)
        cv2.line(frame, (0, 5), (width, 5), config.COLOR_AXES, 2)
        cv2.putText(frame, "X", (width - 25, 25), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, config.COLOR_AXES, 2)

        # Disegna Asse Y (Verticale a sinistra)
        cv2.line(frame, (5, 0), (5, height), config.COLOR_AXES, 2)
        cv2.putText(frame, "Y", (15, height - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, config.COLOR_AXES, 2)

        # Segnaposto Origine (0,0)
        cv2.putText(frame, "(0,0)", (12, 25), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, config.COLOR_AXES, 1)
        
        if not ret: break

        # 1. TRASFORMAZIONE COLORE
        # Convertiamo in HSV per isolare meglio l'oggetto bianco
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 2. CREAZIONE MASCHERA
        # Usiamo i range definiti nel file config
        lower = np.array(config.LOWER_WHITE)
        upper = np.array(config.UPPER_WHITE)
        mask = cv2.inRange(hsv, lower, upper)

        # 3. FILTRAGGIO MORFOLOGICO
        # Rimuove piccoli punti bianchi (rumore) per pulire la maschera
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # 4. RICERCA CONTORNI
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Identifichiamo il contorno più grande nell'inquadratura
            c = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(c)

            # Filtriamo per area minima (da config)
            if area > config.MIN_AREA:
                # --- CALCOLO DIMENSIONI E ORIENTAMENTO ---
                # Trova il rettangolo ruotato che racchiude l'oggetto
                rect = cv2.minAreaRect(c)
                (cx, cy), (w_px, h_px), angle = rect
                
                # Conversione dimensioni: Pixel -> Millimetri
                width_mm = round(w_px * config.PIXEL_TO_MM, 1)
                height_mm = round(h_px * config.PIXEL_TO_MM, 1)
                
                # Otteniamo i 4 angoli del rettangolo per poterlo disegnare
                box = cv2.boxPoints(rect)
                box = np.int0(box) # Converte in interi per il disegno

                # --- DISEGNO E FEEDBACK ---
                # 1. Disegna il rettangolo ruotato (Giallo)
                cv2.drawContours(frame, [box], 0, (0, 255, 255), 2)
                
                # 2. Disegna il mirino centrale (Rosso)
                cv2.drawMarker(frame, (int(cx), int(cy)), config.COLOR_POINTER, cv2.MARKER_CROSS, 20, 2)

                # 3. Scrivi le dimensioni reali sopra l'oggetto
                testo_dim = f"W: {width_mm}mm  H: {height_mm}mm"
                cv2.putText(frame, testo_dim, (int(cx) - 80, int(cy) + 40), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                
                # 4. Scrivi l'angolo di rotazione (utile per la pinza del robot)
                cv2.putText(frame, f"Ang: {round(angle, 1)}deg", (int(cx) - 80, int(cy) + 60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 100, 0), 2)


                # Calcolo dei Momenti per trovare il centro geometrico (Baricentro)
                # La formula matematica è: Cx = M10/M00, Cy = M01/M00
                M = cv2.moments(c)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                    # Conversione Coordinate: Pixel -> Millimetri
                    mm_x = round(cx * config.PIXEL_TO_MM, 1)
                    mm_y = round(cy * config.PIXEL_TO_MM, 1)

                    # --- DISEGNO E FEEDBACK ---
                    # Disegna il contorno e il mirino (croce)
                    cv2.drawContours(frame, [c], -1, config.COLOR_CONTOUR, 2)
                    cv2.drawMarker(frame, (cx, cy), config.COLOR_POINTER, cv2.MARKER_CROSS, 20, 2)

                    # Scrivi coordinate sull'immagine
                    testo = f"X:{mm_x}mm Y:{mm_y}mm"
                    cv2.putText(frame, testo, (cx - 60, cy - 25), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, config.COLOR_TEXT, 2)

                    # Output in console per debugging/Arduino
                    print(f"Oggetto Rilevato -> X: {mm_x}mm, Y: {mm_y}mm (Area: {int(area)}px) | {width_mm}x{height_mm} mm | Angolo: {round(angle, 1)}°")

                    # Output console
                    #print(f"Rilevato: {width_mm}x{height_mm} mm | Angolo: {round(angle, 1)}°")

        # Visualizzazione finestre
        cv2.imshow("Visione Robotica (Frame)", frame)
        # cv2.imshow("Maschera Binaria (Debug)", mask) # Utile per vedere cosa "capisce" l'algoritmo
        #0xFF == ord('q')
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()