import wx

# Imposta le dimensioni della finestra grafica
app = wx.App()
frame = wx.Frame(None, title="Asse cartesiano", size=(600, 400))

# Crea un canvas
canvas = wx.Panel(frame)

# Imposta il colore del pennello
canvas.SetForegroundColour("black")

# Disegna l'asse x
for i in range(-200, 201):
    if i == 0:
        canvas.SetPen(wx.Pen(width=2))
    else:
        canvas.SetPen(wx.Pen(width=1))
    canvas.DrawLine(i, 0, i, 400)
'''
# Disegna l'asse y
for i in range(-100, 101):
    if i == 0:
        canvas.SetPen(wx.Pen(width=2))
    else:
        canvas.SetPen(wx.Pen(width=1))
    canvas.DrawLine(0, i, 400, i)

# Disegna le etichette dell'asse x
for i in range(-200, 201, 50):
    canvas.SetFont(wx.Font("Arial", 10))
    canvas.DrawText(str(i), i, 375)

# Disegna le etichette dell'asse y
for i in range(-100, 101, 25):
    canvas.SetFont(wx.Font("Arial", 10))
    canvas.DrawText(str(i), 375, i)
'''
# Mostra la finestra grafica
frame.Show()
app.MainLoop()
