import turtle



# Imposta le dimensioni della finestra grafica
turtle.setup(width=500, height=500)

# Crea una tartaruga
t = turtle.Turtle()

# Imposta la velocità della tartaruga
t.speed(0)  # 0 è la massima velocità

t.home()
t.write(t.pos())



t.fillcolor("green")
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




















































turtle.done()