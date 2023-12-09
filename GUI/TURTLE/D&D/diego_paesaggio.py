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

t.home()
t.write(t.pos())

#funzione che disegna erba
def disegna_erba():
    t.penup()
    t.home()
    
    colore_linea = "green"
    t.color(colore_linea)  # Imposta il colore della linea

    colore_fill = "#00e600"
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
    #t.color(colore_linea)  # Imposta il colore della linea
    t.pencolor(colore_linea)


    colore_fill = "#4d79ff"
    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)

    t.begin_fill()
    t.right(90)
    t.forward(height/4)
    t.left(90)
    t.pendown()
    t.forward(width/2)
    t.left(90)
    t.forward(height - height/4)  
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height - height/4)  
    t.left(90)
    t.forward(width/2)
    t.end_fill()

#funzione che disegna il sole
def disegna_sole(radius,rays_flag) :
    t.penup()  
    t.home()    
    
    colore_linea = "yellow"
    t.pencolor(colore_linea)  # Imposta il colore della linea
    
    colore_fill = "yellow"
    # Imposta il colore del riempimento
    t.fillcolor(colore_fill)
    t.goto(width/4,height/4)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    if rays_flag :
        # Disegna i raggi attorno al cerchio del sole
        t.penup()
        t.goto(width/4,height/4 + radius)
        t.pendown()
        t.color("yellow")  # Puoi cambiare il colore dei raggi se lo desideri
        t.pensize(1)
        for _ in range(36):  # 12 raggi
            t.forward(radius*1.5)
            t.backward(radius*1.5)
            t.left(10)  # Angolo tra i raggi


#disegna casa 
def disegna_casa() :
    t.penup()  
    t.home() 

    colore_linea = "#cc6600" #corpo casa 
    t.pencolor(colore_linea)  # Imposta il colore della linea

    colore_linea = "#cc6600"
    # Imposta il colore del riempimento
    t.goto(width/4,-height/4)
    
    colore_fill = "#ffbf80"
    #imposta il colore del riempimento
    t.fillcolor("#ffbf80")

    t.begin_fill()
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()













#===== DISEGNO FIGURE =====



disegna_erba()
disegna_cielo()
#disegna_sole(50,True)
disegna_casa()


#t.home()
#t.write(t.pos())

# Chiudi la finestra quando si fa clic sopra di essa
turtle.done()