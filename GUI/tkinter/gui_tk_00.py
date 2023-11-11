import wx

class MyFrame(wx.Frame):
    def __init__(self, title):
        super().__init__(None, title=title)

        # Create a panel
        panel = wx.Panel(self)

        # Create a button
        button = wx.Button(panel, label="Click Me!")
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Layout the widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button, 0, wx.ALIGN_CENTER)
        panel.SetSizer(sizer)

        # Center the frame
        self.Centre()

    def on_button_click(self, event):
        print("Button clicked!")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame("My GUI")
    frame.Show()
    app.MainLoop()
