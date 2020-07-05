import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main()
        self.menu()
        self.other()
    def main(self):
        pass
    def menu(self):
        # Menubar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        #creating file menu
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="Exit", command=self.exit)
        #creating help menu
        helpmenu = tk.Menu(menubar)
        helpmenu.add_command(label="Help")

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
    def other(self):
        self.title = tk.Label(self)
        self.title["text"] = "Math Quiz"
        self.title.pack(side="top")
        self.title.config(font=("Math Quiz", 44))

        self.credit = tk.Label(self)
        self.credit["text"] = "credit by William & Alan"
        self.credit.pack(side="bottom")
        self.credit.config(font=("credit by William & Alan", 12))

    def exit(self):
        exit()

root = tk.Tk()
app = Application(master=root)
root.title("Math QUIZ")
root.geometry("500x500")
def getstart():
    print("Here we go")
frame1 = Frame(root)
frame2 = Frame(root)
root.title("tkinter frame")

label= Label(frame1,text="Click to get started",justify=LEFT)
label.pack(side=LEFT)

hi_there = Button(frame2,text="Here we go ~",command=getstart)
hi_there.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=1,pady=100)


app.mainloop()



