import turtle

#======= SETTINGS =======#
#VARIABILI GLOBALI
width = 600
height = 600

# Imposta le dimensioni della finestra grafica
turtle.setup(width, height)

# Crea una tartaruga
t = turtle.Turtle()

# Imposta la velocità della tartaruga
t.speed(1)  # 0 è la massima velocità

t.home()
t.write(t.pos())

#funzione che disegna erba
def disegna_erba():
    t.penup()
    t.home()
    
    colore_linea = "green"
    t.color(colore_linea)  # Imposta il colore della linea

    colore_fill = "green"
    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)

    t.begin_fill()
    t.right(90)
    t.forward(height/4)
    t.pendown()
    t.left(90)
    t.forward(width/2)
    t.right(90)
    t.forward(height/4)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height/4)
    t.right(90)
    t.forward(width/2)
    t.end_fill()

#funzione che disegna il cielo
def disegna_cielo() :
    t.penup()  
    t.home()

    colore_linea = "blue"
    t.color(colore_linea)  # Imposta il colore della linea

    colore_fill = "blue"
    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)

    t.begin_fill()
    t.right(90)
    t.forward(height/4)
    t.left(90)
    t.pendown()
    t.forward(width/2)
    t.right(90)
    t.forward(height/4)  
    t.right(90)
    t.forward(width)
    t.left(90)
    t.forward(height/2)

    t.end_fill()

#funzione che disegna il sole
def disegna_sole() :
    t.penup()  
    t.home()    

    colore_linea = "yellow"
    t.color(colore_linea)  # Imposta il colore della linea

    colore_fill = "yellow"
    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)

    t.begin_fill()

    t.forward(width/4)
    t.left(90)
    t.forward(height)


    t.end_fill()

#===== DISEGNO FIGURE =====

#disegna_erba()
disegna_cielo()
#disegna_sole()


# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()