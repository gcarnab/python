import wx
import wx.lib.colourselect as csel
import random

class CirclePanel(wx.Panel):
    def __init__(self, parent):
        super(CirclePanel, self).__init__(parent)
        self.circle_color = wx.Colour(255, 0, 0)  # Initial circle color (red)
        self.Bind(wx.EVT_PAINT, self.on_paint)
    
    def set_circle_color(self, color):
        self.circle_color = color
        self.Refresh()
    
    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(self.circle_color))
        circle_radius = min(self.GetSize().width, self.GetSize().height) // 2
        circle_center = wx.Point(self.GetSize().width // 2, self.GetSize().height // 2)
        dc.DrawCircle(circle_center.x, circle_center.y, circle_radius)

class CircleFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CircleFrame, self).__init__(parent, title=title, size=(300, 300))
        
        panel = wx.Panel(self)
        
        self.circle_panel = CirclePanel(panel)
        self.circle_panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set background color
        
        color_picker_label = wx.StaticText(panel, label="Choose Circle Color:", pos=(10, 10))
        self.color_picker = csel.ColourSelect(panel, colour=self.circle_panel.circle_color, pos=(140, 10))
        self.Bind(csel.EVT_COLOURSELECT, self.on_color_change, self.color_picker)
        
        random_color_button = wx.Button(panel, label="Random Color", pos=(10, 50))
        self.Bind(wx.EVT_BUTTON, self.on_random_color, random_color_button)
        
        self.Centre()
        self.Show(True)
    
    def on_color_change(self, event):
        color = self.color_picker.GetColour()
        self.circle_panel.set_circle_color(color)
    
    def on_random_color(self, event):
        random_color = wx.Colour(random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255))
        self.circle_panel.set_circle_color(random_color)

app = wx.App(False)
frame = CircleFrame(None, "Random Color Circle Plotter")
app.MainLoop()
