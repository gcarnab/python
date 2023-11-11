import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(300, 200))

        #self.Centre()
        self.Move((200, 250))


def main():

    app = wx.App()
    ex = Example(None, title='Centering')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()