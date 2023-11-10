import turtle

#======= SETTINGS =======#

# Imposta il ritardo a 500 millisecondi (0.5 secondi)
#turtle.delay(200)

# Imposta le dimensioni della finestra grafica
turtle.setup(width=800, height=800)


# Crea una tartaruga
t = turtle.Turtle()

# Imposta la velocità della tartaruga
t.speed(1)  # 0 è la massima velocità




t.goto(-60,-60)
t.penup()
t.goto(0,0)
t.pendown()
t.goto(60,-60)
t.right(90)   
t.forward(100)
t.right(90)
t.forward(120)
t.right(90)
t.forward(100)
t.right(90)
t.forward(120)





# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()

