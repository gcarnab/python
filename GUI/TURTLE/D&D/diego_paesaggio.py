import turtle
#======= SETTINGS =======#

# Imposta il ritardo a 500 millisecondi (0.5 secondi)
#turtle.delay(200)

# Imposta le dimensioni della finestra grafica
turtle.setup(width=800, height=800)


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

t.penup()
t.right(90)
t.forward(200)
t.pendown()
t.left(90)
t.forward(400)
t.right(90)
t.forward(150)
t.right(90)
t.forward(800)
t.right(90)
t.forward(150)
t.right(90)
t.forward(400)

t.end_fill()

#==================================================

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













# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()