from Tkinter import *
root = Tk()
root.title("Simple GUI")
root.geometry("400x100")
app = Frame(root)
app.grid()
label1 = Label(app, text = "HELLO!")
label1.grid()
label2 = Label(app,text = "This GUI was made using Procedural Programming")
label2.grid()
button = Button(app, text = "Press Me")
button.grid()
button.update_count

def update_count(self):
    '''Increases clicks by 1 '''
    num = print 0
    self.button_clicks += 1
    self.num["text"] = 0 + str(self.button_clicks)
print "self.update_count"
root.mainloop()