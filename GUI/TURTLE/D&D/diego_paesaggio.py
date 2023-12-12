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
t.speed(0)  # 0 è la massima velocità

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

t.penup()
t.left(90)
t.forward(600)
t.pendown()
t.left(90)
t.forward(400)
t.left(90)
t.forward(600)
t.left(90)
t.forward(800)
t.left(90)
t.forward(600)
t.left(90)
t.forward(400)

t.end_fill()

#========================================

colore_linea = "yellow"
t.color(colore_linea)  # Imposta il colore della linea

colore_fill = "yellow"
# Imposta il colore del riempimento
t.fillcolor(colore_fill)

t.begin_fill()

t.penup()
t.goto(250,350)
t.pendown()
t.circle(50)


t.end_fill()

#===== DISEGNO FIGURE =====

#disegna_erba()
disegna_cielo()
#disegna_sole()


#===== DISEGNO FIGURE =====



disegna_erba()
disegna_cielo()
#disegna_sole(50,True)
disegna_casa()


#t.home()
#t.write(t.pos())

# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()