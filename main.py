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
        self.title = tk.Button(self)
        self.title["text"] = "Math Quiz"
        self.title.pack(side="top")

        self.credit = tk.Button(self)
        self.credit["text"] = "credit by William & Alan"
        self.credit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()