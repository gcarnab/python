import wx

class ModernGUI(wx.Frame):
    def __init__(self, parent, title):
        super(ModernGUI, self).__init__(parent, title=title, size=(400, 300))
        
        # Set a modern theme for the GUI
        wx.SystemOptions.SetOptionInt("mac.aquaButtonAppearance", 1)
        wx.SystemOptions.SetOptionInt("osx.openfiledialog.alwaysnative", 1)
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Label
        label = wx.StaticText(panel, label="Modern and Clean GUI", style=wx.ALIGN_CENTER)
        label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(label, 0, wx.EXPAND | wx.ALL, 10)
        
        # Button
        button = wx.Button(panel, label="Click Me!")
        vbox.Add(button, 0, wx.EXPAND | wx.ALL, 10)
        
        # Text Control
        text_ctrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        vbox.Add(text_ctrl, 0, wx.EXPAND | wx.ALL, 10)
        
        # List Control
        list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        list_ctrl.InsertColumn(0, "Items")
        list_ctrl.InsertItem(0, "Item 1")
        list_ctrl.InsertItem(1, "Item 2")
        vbox.Add(list_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        
        # Combo Box
        choices = ["Option 1", "Option 2", "Option 3"]
        combo_box = wx.ComboBox(panel, choices=choices, style=wx.CB_DROPDOWN)
        vbox.Add(combo_box, 0, wx.EXPAND | wx.ALL, 10)
        
        panel.SetSizer(vbox)
        
        self.Centre()
        self.Show(True)

if __name__ == "__main__":
    app = wx.App(False)
    frame = ModernGUI(None, "Modern GUI Example")
    app.MainLoop()
