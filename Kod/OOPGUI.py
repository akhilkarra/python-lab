from Tkinter import *
root = Tk()
root.title("OOP GUI")
root.geometry("400x100")
class App(Frame):
    ''' A GUI with a button and 2 labels '''
    def _init_(self,master):
        ''' This Initializes the Frame'''
        Frame._init_(self,master)
        self.grid()
        self.button_clicks = 0
app = App(root)
app.grid()
label1.grid()
label2 = Label(app,text = "This GUI was made using Object-Oriented Programming")
label2.grid()
button = Button(app, text = "Press Me"
button.grid()
print "0"
button.update_count

root.mainloop()

      
        