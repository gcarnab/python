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

    # Esempio di utilizzo della funzione per disegnare una retta da (50, 50) a (200, 150)
    disegna_retta(t,-50, -50, 50, 50, "yellow")

    # Esempio di utilizzo della funzione per disegnare un cerchio con centro in (50, 50) e raggio 100
    disegna_cerchio(t, 20, 20, 100, "blue")

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

    # Chiudi la finestra quando si fa clic sopra di essa
    #turtle.done()

def disegna_cerchio(t, x, y, raggio, colore_linea):
    # Crea una tartaruga
    #t = turtle.Turtle()

    # Imposta la velocità della tartaruga
    #t.speed(0)  # 0 è la massima velocità
    t.color(colore_linea)  # Imposta il colore della linea

    # Sposta la tartaruga al punto di inizio del cerchio
    t.penup()
    t.goto(x, y - raggio)
    t.pendown()

    # Disegna il cerchio
    t.circle(raggio)

    # Disegna un punto al centro del cerchio
    t.penup()
    t.goto(x, y)  # Sposta la tartaruga al centro del cerchio
    t.dot(5, colore_linea)  # Disegna un punto rosso al centro del cerchio
    
    # Chiudi la finestra quando si fa clic sopra di essa
    #turtle.done()


# Esempio di utilizzo della funzione con parametri specifici
disegna_cartesiano(x=0, y=0, lunghezza_assi=300, colore_assi="black", spessore_assi=2, dimensione_griglia=0)

