import turtle
import random

# funzione che disegna il cielo
def disegna_cielo(screen_width,screen_height, fill_color):
    turtle.penup()  
    turtle.goto(-screen_width/2, screen_height/2)
    #turtle.pencolor("black")
    #turtle.write(turtle.pos())
    turtle.pencolor(fill_color)
    turtle.color(fill_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screen_width)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
        turtle.forward(screen_height - screen_height/4)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
    turtle.end_fill()

# funzione che disegna l'erba
def disegna_erba(screen_width,screen_height, fill_color):
    turtle.penup()
    turtle.goto(-screen_width/2, - screen_height/4)
    turtle.color(fill_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screen_width)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
        turtle.forward(screen_height/4)
        turtle.right(90)
        #turtle.pencolor("black")
        #turtle.write(turtle.pos())
        #turtle.pencolor(fill_color)
    turtle.end_fill()

# funzione che disegna il prato
def disegna_prato(screen_width, screen_height, fill_color):
    turtle.penup()
    #turtle.home()
    turtle.goto(-(screen_width/2), - screen_height/4)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    grass_range = int(screen_width/10)
    for _ in range(grass_range):
        for _ in range(3):
            turtle.forward(10)
            turtle.left(120)
        turtle.forward(10)    
    turtle.end_fill()

# funzione che disegna il sole
def disegna_sole(screen_width, screen_height, fill_color, rays_flag):
    turtle.penup()
    sun_x = - screen_width / 4
    sun_y = screen_height / 4
    radius = 50
    turtle.goto(sun_x, sun_y)
    turtle.pendown()
    
    # Disegna il cerchio del sole
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    if rays_flag :
        # Disegna i raggi attorno al cerchio del sole
        turtle.penup()
        turtle.goto(sun_x, sun_y + radius )
        turtle.pendown()
        turtle.color("yellow")  # Puoi cambiare il colore dei raggi se lo desideri
        
        for _ in range(36):  # 12 raggi
            turtle.forward(70)
            turtle.backward(70)
            turtle.left(10)  # Angolo tra i raggi

# funzione che disegna una spirale
def disegna_spirale(screen_width, screen_height, radius, fill_color) :
    turtle.penup()
    turtle.goto(screen_width/5, screen_height/5)
    turtle.pendown()
    turtle.pencolor(fill_color)
    turtle.pensize(2)
    
    # Loop for printing spiral circle 
    for i in range(50): 
        turtle.circle(radius + i, 50) 

    # Loop for printing concentric circles 
    #for i in range(10): 
    #    turtle.circle(radius * i) 
    #    turtle.up() 
    #    turtle.sety((radius * i)*(-1)) 
    #    turtle.down() 

# funzione che disegna una nuvola
def disegna_nuvola(screen_width, screen_height, raggio, numero_curve, lunghezza_curva,fill_flag):
    turtle.penup()
    turtle.goto(screen_width/3, screen_height/3)
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

# funzione che disegna una casa
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

# funzione che disegna una albero
def disegna_albero(screen_width,screen_height):

    # disegno tronco
    turtle.penup()
    turtle.goto(-screen_width/3, -screen_height/6)
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
    turtle.goto(-screen_width/3 + 5, -screen_height/6)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

# funzione che disegna una mucca
def disegna_mucca(screen_width,screen_height, fill_color):

    # Testa della mucca
    turtle.penup()
    turtle.goto(-screen_width/3.6 , -screen_height/4)
    turtle.color(fill_color)
    turtle.pendown()
    turtle.circle(10)

    # Corpo della mucca
    turtle.penup()
    turtle.goto(-screen_width/3.6 , -screen_height/4)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # disegno gamba    
    turtle.penup()    
    turtle.goto(-screen_width/3.6 , -screen_height/3.5)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # disegno gamba    
    turtle.penup()    
    turtle.goto(-screen_width/4.6 , -screen_height/3.5)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)

    # Macchie della mucca
    turtle.penup()
    turtle.goto(-screen_width/3.8 , -screen_height/3.6)
    turtle.color("black")
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.circle(5)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.end_fill()

def disegna_albero_natale(screen_width, screen_height, base, balls_flag):

    # Disegna il triangolo più grande.
    turtle.pencolor("lightgreen")
    turtle.penup()
    turtle.goto(-screen_width/4 , -screen_height/4)        
    turtle.begin_fill()
    turtle.fillcolor("green")
    turtle.pendown()
    for _ in range(3):
        turtle.forward(base)
        turtle.left(120)
        turtle.forward(base)
    turtle.end_fill()
    if balls_flag :
        disegna_pallina(10)
        turtle.penup()
        turtle.goto(-screen_width/4 + 25, -screen_height/4)  
        disegna_pallina(10)

    # Disegna il triangolo medio
    turtle.penup()
    turtle.goto(-screen_width/4 , -screen_height/4 + base)   
    turtle.pendown()   
    turtle.fillcolor("green")
    turtle.begin_fill()  
    base = base / 1.2   
    for _ in range(3):
        turtle.forward(base)
        turtle.left(120)
        turtle.forward(base)
    turtle.end_fill()
    if balls_flag :
        disegna_pallina(10)
        turtle.penup()
        turtle.goto(-screen_width/4 + 25, -screen_height/4 + base)   
        disegna_pallina(10)

    # Disegna il triangolo piccolo
    turtle.penup()
    turtle.goto(-screen_width/4 , -screen_height/4 + base*2.5)   
    turtle.pendown()   
    turtle.fillcolor("green")
    turtle.begin_fill()  
    base = base / 2   
    for _ in range(3):
        turtle.forward(base)
        turtle.left(120)
        turtle.forward(base)
    turtle.end_fill()
    if balls_flag :
        disegna_pallina(10)
        turtle.penup()
        turtle.goto(-screen_width/4 + 25, -screen_height/4 + base*4)   
        disegna_pallina(10)

    # disegno tronco
    turtle.penup()
    turtle.goto(-screen_width/3.9, -screen_height/4)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def disegna_pallina(radius):
    turtle.pendown()
    colore = random.choice(["yellow", "blue", "gold", "purple", "lightgreen", "black", "grey"])
    turtle.fillcolor(colore)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def disegna_pacchi(screen_width, screen_height, numero_pacchi, dimensioni_pacchi):
    turtle.penup()
    turtle.goto(-screen_width/3, -screen_height/3)
    turtle.pendown()

    for _ in range(numero_pacchi):
        colore = random.choice(["red", "lightgreen", "blue", "yellow"])
        lunghezza, larghezza, altezza = dimensioni_pacchi
        turtle.fillcolor(colore)
        turtle.pencolor("black")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(lunghezza)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(35)
        turtle.pendown()



def main():

    #=== SETTINGS ===
    turtle.speed(0)
    screen_width=640
    screen_height=480
    turtle.setup(width=screen_width,height=screen_height)
    turtle.Screen().title("GC Landscape")
    
    #=== FIGURES ===
    disegna_cielo(screen_width,screen_height, "blue")
    disegna_erba(screen_width,screen_height, "green")
    disegna_prato(screen_width, screen_height,"lightgreen")
    disegna_sole(screen_width,screen_height, "yellow", True)
    #disegna_spirale(screen_width,screen_height, 5, "orange")
    disegna_nuvola(screen_width,screen_height, 30, 10, 10, False)
    disegna_nuvola(screen_width,screen_height, 30, 10, 20, False)
    disegna_nuvola(screen_width,screen_height, 30, 15, 30, False)
    disegna_casa(screen_width,screen_height)
    #disegna_albero(screen_width,screen_height)
    #disegna_mucca(screen_width,screen_height, "white")
    disegna_albero_natale(screen_width,screen_height,50, True)
    disegna_pacchi(screen_width,screen_height, 3, (20, 20, 20))

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
