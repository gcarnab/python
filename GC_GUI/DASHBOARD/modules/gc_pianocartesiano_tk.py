import tkinter as tk
from tkinter import Label, StringVar

def disegna_cartesiano(x, y, lunghezza_assi, colore_assi, spessore_assi, dimensione_griglia):
    # Creazione della finestra
    root = tk.Tk()
    root.title("Piano Cartesiano")

    # Dimensioni del canvas
    larghezza = lunghezza_assi + dimensione_griglia * 2
    altezza = lunghezza_assi + dimensione_griglia * 2

    # Creazione del canvas
    canvas = tk.Canvas(root, width=larghezza, height=altezza)
    canvas.pack()

    # Disegna la griglia
    for i in range(-larghezza//2, larghezza//2, dimensione_griglia):
        canvas.create_line(i + larghezza//2, 0, i + larghezza//2, altezza, fill="lightgray", dash=(2, 2))
        canvas.create_line(0, i + larghezza//2, larghezza, i + larghezza//2, fill="lightgray", dash=(2, 2))

    # Disegna gli assi x e y
    canvas.create_line(dimensione_griglia, altezza/2, larghezza-dimensione_griglia, altezza/2,
                       fill=colore_assi, width=spessore_assi)  # Asse x
    canvas.create_line(larghezza/2, dimensione_griglia, larghezza/2, altezza-dimensione_griglia,
                       fill=colore_assi, width=spessore_assi)  # Asse y

    # Etichette degli assi
    canvas.create_text(larghezza - dimensione_griglia, altezza/2 - dimensione_griglia, text="X", anchor="se", font=("Arial", 12, "bold"))
    canvas.create_text(larghezza/2 + dimensione_griglia, dimensione_griglia, text="Y", anchor="nw", font=("Arial", 12, "bold"))

    # Frecce degli assi
    canvas.create_line(larghezza-dimensione_griglia-10, altezza/2-5, larghezza-dimensione_griglia, altezza/2, fill=colore_assi, width=spessore_assi)  # Freccia asse x
    canvas.create_line(larghezza-dimensione_griglia-10, altezza/2+5, larghezza-dimensione_griglia, altezza/2, fill=colore_assi, width=spessore_assi)  # Freccia asse x
    canvas.create_line(larghezza/2-5, dimensione_griglia+10, larghezza/2, dimensione_griglia, fill=colore_assi, width=spessore_assi)  # Freccia asse y
    canvas.create_line(larghezza/2+5, dimensione_griglia+10, larghezza/2, dimensione_griglia, fill=colore_assi, width=spessore_assi)  # Freccia asse y

    # Funzione per convertire coordinate cartesiane in coordinate del canvas
    def converti_coordinate(x, y):
        x_canvas = larghezza/2 + x
        y_canvas = altezza/2 - y
        return x_canvas, y_canvas
      
    # Disegna un punto al centro del piano cartesiano
    x_centro, y_centro = x, y  # Coordinate del centro del piano cartesiano
    x_centro_canvas, y_centro_canvas = converti_coordinate(x_centro, y_centro)
    canvas.create_oval(x_centro_canvas-3, y_centro_canvas-3, x_centro_canvas+3, y_centro_canvas+3, fill="black")  # Disegna un punto nero
    
    # Variabili per le coordinate del centro degli assi
    x_centro_var = StringVar()
    y_centro_var = StringVar()
    x_centro_var.set("X: {}".format(x))
    y_centro_var.set("Y: {}".format(y))

    # Etichette per le coordinate del centro degli assi
    label_x_centro = Label(root, textvariable=x_centro_var, font=("Arial", 5, "italic"))
    label_y_centro = Label(root, textvariable=y_centro_var, font=("Arial", 5, "italic"))

    # Posiziona le etichette delle coordinate del centro degli assi
    #label_x_centro.place(x=x_centro_canvas, y=y_centro_canvas)
    #label_y_centro.place(x=x_centro_canvas, y=y_centro_canvas)

    #================> FIGURE <=================#

    #========> Funzione per disegnare una retta <==========#

    def disegna_retta(punto1, punto2, colore, spessore):
        x1, y1 = punto1
        x2, y2 = punto2
        x1_canvas, y1_canvas = converti_coordinate(x1, y1)
        x2_canvas, y2_canvas = converti_coordinate(x2, y2)
        canvas.create_line(x1_canvas, y1_canvas, x2_canvas, y2_canvas, fill=colore, width=spessore)

    # Esempio: Disegna una retta sul piano cartesiano
    punto1 = (-50, 50)  # Coordinate del primo punto della retta
    punto2 = (50, -50)  # Coordinate del secondo punto della retta
    colore_retta = "green"  # Colore della retta
    spessore_retta = 1  # Spessore della retta
    disegna_retta(punto1, punto2, colore_retta, spessore_retta)

    #========> Funzione per disegnare una cerchio <==========#

    # Funzione per disegnare un cerchio
    def disegna_cerchio(centro, raggio, colore_linea, spessore_linea, colore_riempimento, fill_flag):
        x_centro, y_centro = centro
        x_centro_canvas, y_centro_canvas = converti_coordinate(x_centro, y_centro)
        x1, y1 = x_centro_canvas - raggio, y_centro_canvas - raggio
        x2, y2 = x_centro_canvas + raggio, y_centro_canvas + raggio
        if fill_flag:
            canvas.create_oval(x1, y1, x2, y2, outline=colore_linea, width=spessore_linea, fill=colore_riempimento)
        else:
            canvas.create_oval(x1, y1, x2, y2, outline=colore_linea, width=spessore_linea)

    # Esempio: Disegna un cerchio sul piano cartesiano
    centro_cerchio = (50, -30)  # Coordinate del centro del cerchio
    raggio_cerchio = 40  # Raggio del cerchio
    colore_linea_cerchio = "blue"  # Colore della linea del cerchio
    spessore_linea_cerchio = 2  # Spessore della linea del cerchio
    colore_riempimento_cerchio = "yellow"  # Colore di riempimento del cerchio
    fill_flag_cerchio = True  # True se il cerchio deve essere riempito, False altrimenti
    disegna_cerchio(centro_cerchio, raggio_cerchio, colore_linea_cerchio, spessore_linea_cerchio, colore_riempimento_cerchio, fill_flag_cerchio)

    # Esecuzione del loop principale
    root.mainloop()

'''
# Funzione principale (main)
if __name__ == "__main__":

    # Parametri per la funzione disegna_cartesiano
    x, y = 0, 0  # Coordinate del centro del piano cartesiano
    lunghezza_assi = 500  # Lunghezza degli assi x e y
    colore_assi = "black"  # Colore degli assi
    spessore_assi = 2  # Spessore degli assi
    dimensione_griglia = 10  # Dimensione della griglia

    # Chiamata alla funzione disegna_cartesiano con i parametri specificati
    disegna_cartesiano(x, y, lunghezza_assi, colore_assi, spessore_assi, dimensione_griglia)
'''