import cv2
import numpy as np

# Importiamo tutte le configurazioni
import config_gpt as config 

# ===============================
# APERTURA WEBCAM
# ===============================

cap = cv2.VideoCapture(config.CAMERA_INDEX)

# Impostiamo la risoluzione
cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)

if not cap.isOpened():
    print("❌ Errore: impossibile aprire la webcam")
    exit()

print("✅ Webcam aperta correttamente")

# ===============================
# LOOP PRINCIPALE
# ===============================

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Errore nella lettura del frame")
        break

    # ===============================
    # PRE-PROCESSING
    # ===============================

    # Conversione in scala di grigi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Riduzione del rumore
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold binario
    _, thresh = cv2.threshold(
        blurred,
        config.THRESHOLD_VALUE,
        config.THRESHOLD_MAX,
        cv2.THRESH_BINARY
    )

    # ===============================
    # CONTORNI
    # ===============================

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        # Selezioniamo il contorno più grande
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        if area > config.MIN_OBJECT_AREA:
            # Momenti per calcolare il centroide
            M = cv2.moments(largest_contour)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # ===============================
                # DISEGNO
                # ===============================

                # Disegno contorno
                cv2.drawContours(
                    frame,
                    [largest_contour],
                    -1,
                    config.COLOR_CONTOUR,
                    2
                )

                # Mirino centrale
                cv2.drawMarker(
                    frame,
                    (cx, cy),
                    config.COLOR_MARKER,
                    cv2.MARKER_CROSS,
                    30,
                    2
                )

                # Testo coordinate
                text = f"X: {cx} px  Y: {cy} px"
                cv2.putText(
                    frame,
                    text,
                    (cx + 10, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    config.TEXT_SCALE,
                    config.COLOR_TEXT,
                    config.TEXT_THICKNESS
                )

                # ===============================
                # AREA OGGETTO (in pixel)
                # ===============================

                if config.SHOW_OBJECT_AREA:
                    area_text = f"Area: {int(area)} px^2"

                    cv2.putText(
                        frame,
                        area_text,
                        (cx + 10, cy + 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        config.TEXT_SCALE,
                        config.COLOR_TEXT,
                        config.TEXT_THICKNESS
                    )
                # ===============================
                # OUTPUT CONSOLE
                # ===============================
                print(f"Centro oggetto -> X: {cx} px | Y: {cy} px | Area: {int(area)} px^2")
    
        else:
            cv2.putText(
                frame,
                "Oggetto troppo piccolo",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

    else:
        cv2.putText(
            frame,
            "Nessun oggetto rilevato",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # ===============================
    # DISEGNO ASSI CARTESIANI
    # ===============================

    if config.SHOW_AXES:
        h, w, _ = frame.shape

        # Asse X (orizzontale)
        cv2.line(
            frame,
            (0, h // 2),
            (w, h // 2),
            config.AXIS_COLOR,
            config.AXIS_THICKNESS
        )

        # Asse Y (verticale)
        cv2.line(
            frame,
            (w // 2, 0),
            (w // 2, h),
            config.AXIS_COLOR,
            config.AXIS_THICKNESS
        )

        # Origine (0,0)
        cv2.putText(
            frame,
            "(0,0)",
            (5, 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            config.AXIS_TEXT_SCALE,
            config.AXIS_COLOR,
            1
        )

        # Etichetta asse X
        cv2.putText(
            frame,
            "X",
            (w - 15, h // 2 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            config.AXIS_TEXT_SCALE,
            config.AXIS_COLOR,
            1
        )

        # Etichetta asse Y
        cv2.putText(
            frame,
            "Y",
            (w // 2 + 5, 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            config.AXIS_TEXT_SCALE,
            config.AXIS_COLOR,
            1
        )

    # ===============================
    # VISUALIZZAZIONE
    # ===============================

    cv2.imshow(config.WINDOW_NAME, frame)

    # ESC per uscire
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ===============================
# CHIUSURA
# ===============================

cap.release()
cv2.destroyAllWindows()
print("👋 Programma terminato")
