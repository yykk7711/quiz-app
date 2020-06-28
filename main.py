import tkinter as tk

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
        pass
    def other(self):
        self.title = tk.Label(self)
        self.title["text"] = "Math Quiz"
        self.title.pack(side="top")
        self.title.config(font=("Math Quiz", 44))

        self.credit = tk.Label(self)
        self.credit["text"] = "credit by William & Alan"
        self.credit.pack(side="bottom")
        self.credit.config(font=("credit by William & Alan", 12))
root = tk.Tk()
app = Application(master=root)
root.title("Math QUIZ")
root.geometry("500x500")
#Menubar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Exit", command = root.quit)

helpmenu = tk.Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help")

menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "Help", menu = helpmenu)

app.mainloop()

