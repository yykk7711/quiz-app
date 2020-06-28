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
        pass
root = tk.Tk()
app = Application(master=root)

root.geometry("500x500")
#Menubar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

app.mainloop()

