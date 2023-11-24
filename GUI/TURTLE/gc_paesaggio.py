import turtle
import random

def disegna_cielo(screen_width,screen_height, fill_color):
    turtle.penup()  
    turtle.goto(-(screen_width - 10)/2, (screen_height - 10 )/2)
    turtle.pencolor("black")
    turtle.write(turtle.pos())
    turtle.pencolor(fill_color)
    turtle.color(fill_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screen_width - 15)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
        turtle.forward(screen_height/1.5)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
    turtle.end_fill()

def disegna_erba(screen_width,screen_height, fill_color):
    turtle.penup()
    turtle.goto(-(screen_width/2 - 5), - screen_height/5.6)
    turtle.color(fill_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screen_width - 15)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
        turtle.forward(screen_height/3.3)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
    turtle.end_fill()

def disegna_prato(screen_width, screen_height):
    turtle.penup()
    #turtle.home()
    turtle.goto(-(screen_width/2 - 5), - screen_height/5.6)
    turtle.pendown()
    turtle.color("lightgreen")
    turtle.begin_fill()
    grass_range = int(screen_width/10)
    for _ in range(grass_range):
        for _ in range(3):
            turtle.forward(10)
            turtle.left(120)
        turtle.forward(10)    
    turtle.end_fill()

def disegna_sole(screen_width, screen_height, fill_color, rays_flag):
    turtle.penup()
    turtle.goto(-screen_width / 3, screen_height / 3.2)
    turtle.pendown()
    
    # Disegna il cerchio del sole
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    if rays_flag :
        # Disegna i raggi attorno al cerchio del sole
        turtle.penup()
        turtle.goto(-screen_width / 3, screen_height / 3.2 + 50)
        turtle.pendown()
        turtle.color("yellow")  # Puoi cambiare il colore dei raggi se lo desideri
        
        for _ in range(36):  # 12 raggi
            turtle.forward(70)
            turtle.backward(70)
            turtle.left(10)  # Angolo tra i raggi

def disegna_nuvola(screen_width, screen_height, raggio, numero_curve, lunghezza_curva,fill_flag):
    turtle.penup()
    turtle.goto(screen_width/3 + 10 , screen_height/3 + 10)
    turtle.pendown()
    turtle.color("white")
    if fill_flag :
        turtle.begin_fill()  # Inizia il riempimento
    for _ in range(numero_curve):
        turtle.circle(raggio, random.randint(100, 200))
        #turtle.circle(raggio)
        turtle.left(180)
        turtle.circle(-raggio, random.randint(100, 100))
        #turtle.circle(-raggio)
        turtle.left(180)

        # Posizionati casualmente per creare una forma più naturale
        turtle.penup()
        turtle.left(random.uniform(0, 30))
        turtle.forward(lunghezza_curva)
        turtle.right(random.uniform(0, 30))
        turtle.pendown()
    if fill_flag :
            turtle.end_fill()  # Completa il riempimento

def disegna_casa(screen_width, screen_height):

    # disegno corpo
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.color("#C4A484")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(120)
        turtle.right(90)
    turtle.end_fill()

    # disegno porta
    turtle.penup()
    turtle.goto(60, -70)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

    # disegno finestra
    turtle.penup()
    turtle.goto(20, -20)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

    # disegno tetto
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(120)
        turtle.left(120)
    turtle.end_fill()

def disegna_albero(screen_width,screen_height):

    # disegno tronco
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    
    #disegno chioma
    turtle.penup()
    turtle.goto(-195, -85)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()



def disegna_mucca(screen_width,screen_height, fill_color):

    turtle.color(fill_color)

    # Testa della mucca
    turtle.penup()
    turtle.goto(-100, -150)
    turtle.pendown()
    turtle.circle(10)

    # Corpo della mucca
    turtle.penup()
    turtle.goto(-100, -150)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # disegno gamba    
    turtle.penup()    
    turtle.goto(-90, -170)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # disegno gamba    
    turtle.penup()    
    turtle.goto(-60, -170)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # Macchie della mucca
    turtle.penup()
    turtle.goto(-90, -165)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(3):
        turtle.circle(5)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.end_fill()

def main():

    #=== SETTINGS ===
    turtle.speed(0)
    screen_width=500
    screen_height=500
    turtle.setup(width=screen_width,height=screen_height)
    #turtle.setup(width=700,height=700)

    #=== FIGURES ===
    disegna_cielo(screen_width,screen_height, "blue")
    disegna_erba(screen_width,screen_height, "green")
    disegna_prato(screen_width, screen_height)
    disegna_sole(screen_width,screen_height, "yellow", True)
    disegna_nuvola(screen_width,screen_height, 30, 5, 10, False)
    disegna_nuvola(screen_width,screen_height, 30, 10, 20, False)
    disegna_nuvola(screen_width,screen_height, 30, 15, 30, False)
    disegna_casa(screen_width,screen_height)
    disegna_albero(screen_width,screen_height)
    disegna_mucca(screen_width,screen_height, "white")

    # mostra centro assi
    turtle.penup()
    turtle.home()
    turtle.color("orange")
    turtle.dot(10)
    turtle.color("white")
    turtle.write(turtle.pos())

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
