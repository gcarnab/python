# Modulo 1 TURTLE
import turtle

#======= SETTINGS =======#

# Imposta il ritardo a 500 millisecondi (0.5 secondi)
#turtle.delay(200)

# Imposta le dimensioni della finestra grafica
turtle.setup(width=800, height=800)

#======= FUNCTIONS =======#

def disegna_cartesiano(x, y, lunghezza_assi, colore_assi, spessore_assi, dimensione_griglia):
    # Crea una tartaruga
    t = turtle.Turtle()

    # Imposta la velocità della tartaruga
    t.speed(0)  # 0 è la massima velocità

    # Nascondi la freccia
    t.hideturtle()

    # Disegna la griglia
    if dimensione_griglia > 0 :
        t.penup()
        t.color("lightgray")  # Colore della griglia
        for i in range(-lunghezza_assi, lunghezza_assi + dimensione_griglia, dimensione_griglia):
            t.goto(i + x, lunghezza_assi + y)
            t.pendown()
            t.setheading(270)  # Orientamento verso il basso
            t.forward(2 * lunghezza_assi)
            t.penup()

            t.goto(x - lunghezza_assi, i + y)
            t.pendown()
            t.setheading(0)  # Orientamento verso destra
            t.forward(2 * lunghezza_assi)
            t.penup()

    # Disegna l'asse y con etichetta
    t.penup()
    t.goto(x, y - lunghezza_assi)  # Posizione iniziale per l'asse y
    t.pendown()
    t.setheading(90)  # Imposta l'orientamento verso l'alto
    t.pensize(spessore_assi)  # Imposta lo spessore della linea
    t.color(colore_assi)  # Imposta il colore della linea
    t.forward(2 * lunghezza_assi)  # Disegna l'asse y
    t.stamp()  # Crea un timbro della tartaruga come freccia per l'asse
    t.write("Y", align="right", font=("Arial", 14, "normal"))

    # Disegna l'asse x con etichetta
    t.penup()
    t.goto(x - lunghezza_assi, y)  # Posizione iniziale per l'asse x
    t.pendown()
    t.setheading(0)  # Imposta l'orientamento verso destra
    t.forward(2 * lunghezza_assi)  # Disegna l'asse x
    t.stamp()  # Crea un timbro della tartaruga come freccia per l'asse 
    t.write("X", align="center", font=("Arial", 14, "normal"))

    # Disegna il centro con etichetta
    t.penup()
    t.goto(x, y)  # Posizione del centro
    t.pendown()
    t.dot(5, 'red')  # Disegna un punto colorato al centro
    t.write(f"({x}, {y})", align="left", font=("Arial", 12, "normal"))

    #================> FIGURE <=================#

    # Esempio di utilizzo della funzione per disegnare una retta
    #disegna_retta(t,-50, -50, 50, 50, "yellow")

    # Esempio di utilizzo della funzione per disegnare un rettangolo 
    #disegna_rettangolo(t, -100, -100, 100, 100, "red", "yellow", True)

    # Esempio di utilizzo della funzione per disegnare un cerchio con centro in (50, 50) e raggio 100
    #disegna_cerchio(t, -100, 100, 50, "blue", "orange", True)

    # Esempio di utilizzo della funzione per disegnare un triangolo 
    #disegna_triangolo_con_punto(t, 0, 100, 100, 200, 200, 100, "red", "yellow",True)


    #============================================#

    # Chiudi la finestra quando si fa clic sopra di essa
    turtle.done()


def disegna_retta(t, x1, y1, x2, y2, colore_linea):
    # Crea una tartaruga
    #t = turtle.Turtle()

    # Imposta la velocità della tartaruga
    #t.speed(0)  # 0 è la massima velocità
    t.color(colore_linea)  # Imposta il colore della linea

    # Sposta la tartaruga alla posizione iniziale
    t.penup()
    t.goto(x1, y1)
    t.pendown()

    # Disegna la retta fino alla posizione finale
    t.goto(x2, y2)

    t.home() # ritorno all'origine

    # Chiudi la finestra quando si fa clic sopra di essa
    #turtle.done()

def disegna_cerchio(t, x, y, raggio, colore_linea, colore_fill,fill_flag):
    # Crea una tartaruga
    #t = turtle.Turtle()

    # Imposta la velocità della tartaruga
    #t.speed(0)  # 0 è la massima velocità
    t.color(colore_linea)  # Imposta il colore della linea

    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)

    # To draw a filled shape, start with this call
    if fill_flag :
        t.begin_fill()

    # Sposta la tartaruga al punto di inizio del cerchio
    t.penup()
    t.goto(x, y - raggio)
    t.pendown()

    # Disegna il cerchio
    t.circle(raggio)

    # Termina il riempimento del cerchio
    if fill_flag :
        t.end_fill()

    # Disegna un punto al centro del cerchio
    t.penup()
    t.goto(x, y)  # Sposta la tartaruga al centro del cerchio
    t.write(t.pos())
    t.dot(5, 'yellow')  # Disegna un punto rosso al centro del cerchio
    
    t.home() # ritorno all'origine

    # Chiudi la finestra quando si fa clic sopra di essa
    #turtle.done()

#Il centro di un triangolo può essere calcolato come la media aritmetica delle coordinate dei suoi vertici
def calcola_centro_triangolo(x1, y1, x2, y2, x3, y3):
    centro_x = (x1 + x2 + x3) / 3
    centro_y = (y1 + y2 + y3) / 3
    return centro_x, centro_y

def disegna_triangolo_con_punto(t, x1, y1, x2, y2, x3, y3, colore_linea, colore_riempimento, fill_flag):
    # Crea una tartaruga
    #t = turtle.Turtle()

    # Imposta il colore della linea e del riempimento
    t.color(colore_linea, colore_riempimento)

    # Imposta la velocità della tartaruga
    t.speed(0)  # 0 è la massima velocità

    # Calcola le coordinate del centro del triangolo
    centro_x, centro_y = calcola_centro_triangolo(x1, y1, x2, y2, x3, y3)

    # Sposta la tartaruga al punto di inizio del triangolo
    t.penup()
    t.goto(x1, y1)
    t.pendown()

    # Inizia il riempimento del triangolo
    if fill_flag : 
        t.begin_fill()

    # Disegna il triangolo
    t.goto(x2, y2)
    t.write(t.pos())
    t.goto(x3, y3)
    t.write(t.pos())
    t.goto(x1, y1)
    t.write(t.pos())

    # Termina il riempimento del triangolo
    if fill_flag : 
        t.end_fill()

    # Disegna un punto al centro del triangolo
    t.penup()
    t.goto(centro_x, centro_y)  # Sposta la tartaruga al centro del triangolo
    t.write(t.pos())
    t.dot(5, "black")  # Disegna un punto nero al centro del triangolo

    # Chiudi la finestra quando si fa clic sopra di essa
    turtle.done()

def disegna_rettangolo(t, x, y, larghezza, altezza, colore_linea, colore_riempimento, fill_flag):
    # Crea una tartaruga
    #t = turtle.Turtle()

    # Imposta il colore della linea e del riempimento
    t.color(colore_linea, colore_riempimento)

    # Imposta la velocità della tartaruga
    #t.speed(0)  # 0 è la massima velocità

    # Sposta la tartaruga al punto iniziale del rettangolo
    t.penup()
    t.goto(x - larghezza / 2, y - altezza / 2)
    t.pendown()

    # Inizia il riempimento del rettangolo
    if fill_flag :
        t.begin_fill()

    # Disegna il rettangolo
    for _ in range(2):
        t.forward(larghezza)  # Lato orizzontale
        t.left(90)  # Angolo di 90 gradi per girare a sinistra
        t.forward(altezza)  # Lato verticale
        t.left(90)  # Angolo di 90 gradi per girare a sinistra

    # Termina il riempimento del rettangolo
    if fill_flag :
        t.end_fill()

    # Disegna un punto al centro 
    t.penup()
    t.goto(x, y)  # Sposta la tartaruga al centro
    t.write(t.pos())
    t.dot(5, 'black')  # Disegna un punto al centro

    # Chiudi la finestra quando si fa clic sopra di essa
    #turtle.done()



#================> MAIN <=================#

# Esempio di utilizzo della funzione con parametri specifici
#disegna_cartesiano(x=0, y=0, lunghezza_assi=300, colore_assi="black", spessore_assi=2, dimensione_griglia=0)



