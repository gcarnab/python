# 🤖 GC DIY_VISION - Progetto Didattico

Questo progetto nasce con lo scopo di insegnare agli studenti delle scuole superiori le basi della **Computer Vision** e dell'**Intelligenza Artificiale** applicata alla robotica. 

Il sistema utilizza una webcam Logitech e il modello **YOLOv11** per identificare oggetti su un piano di lavoro, calcolarne le coordinate reali (in mm) e prepararli per una futura manipolazione tramite braccio robotico (Arduino/ESP32).

---

## 🛠️ Prerequisiti Hardware
* **Webcam:** Logitech (o qualsiasi webcam USB) montata su un supporto perpendicolare al piano (vista Nadir).
* **PC:** Windows 11 con VS Code installato.
* **Area di lavoro:** Un piano di colore uniforme per facilitare il contrasto.

## 💻 Configurazione Ambiente Software

Segui questi passaggi per configurare l'ambiente di sviluppo in modo pulito:

1. **Clona il repository (o scarica i file):**
   ```bash
   git clone [https://github.com/tuo-username/progetto-ai-vision.git](https://github.com/tuo-username/progetto-ai-vision.git)
   cd progetto-ai-vision
2. **VSCODE**
    - python.exe -m pip install --upgrade pip
    - python -m venv venv
    - .\venv\Scripts\activate
    - pip install -r requirements.txt
    - python -m pip list - (ASSICURATI CHE VENV SIA ATTIVO!)

    