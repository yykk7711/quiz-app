import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main()
        self.command()
        self.other()
    def main(self):
        pass
    def command(self):
        pass
    def other(self):
        pass
root = tk.Tk()
app = Application(master=root)
app.mainloop()