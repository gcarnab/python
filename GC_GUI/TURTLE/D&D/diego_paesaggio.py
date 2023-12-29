import turtle
import random

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



#funzione che disegna il cielo
def disegna_cielo() :
    t.penup()  
    t.home()
    colore_linea = "#000000"
    t.pencolor(colore_linea)  # Imposta il colore della linea

    colore_fill = "#FFFF00"
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


def test(line_color, fill_color) :
    t.pencolor(line_color)    
    t.fillcolor(fill_color)
    t.home()
    t.write(t.pos())
    shapes = ["turtle", "arrow", "circle"]
    selected_shape = random.choice(shapes)
    #print("selected_shape= ", selected_shape)
    t.shape(selected_shape)



#===== MAIN =====
test("#FFFF00","#FF6600")

#============ CALL FUNCTIONS ===============
#disegna_cielo()




# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()