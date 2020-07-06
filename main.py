import tkinter as tk
from tkinter import *
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main()
        self.menu()
        self.other()
    def main(self):
        # Button
        def sum():
            questions = {}
            score = 0

            for i in range(10):
                int_1 = random.randint(1,50)
                int_2 = random.randint(1,50)
                operator = "+"
                question = str(int_1)+" "+str(operator)+" "+str(int_2)
                answer = eval(question)
                question+= " = "

                questions.update({question:str(answer)})

            for q in questions.keys():
                user_answer = input(q)
                if questions.get(q) == str(user_answer):
                    score+=1
                    print("Correct!")
                else:
                    print("Incorrect!")

            if score < 5:
               print("Keep practicing! You only got "+str(score)+" right!")
            elif score == 10:
               print("Congratulation! All correct! ")
            else:
               print("You got "+str(score)+" right!")

        def substraction():
            questions = {}
            score = 0

            for i in range(10):
                int_1 = random.randint(1, 50)
                int_2 = random.randint(1, 50)
                operator = "-"
                question = str(int_1) + " " + str(operator) + " " + str(int_2)
                answer = eval(question)
                question += " = "

                questions.update({question: str(answer)})

            for q in questions.keys():
                user_answer = input(q)
                if questions.get(q) == str(user_answer):
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")

            if score < 5:
                print("Keep practicing! You only got " + str(score) + " right!")
            elif score == 10:
                print("Congratulation! All correct! ")
            else:
                print("You got " + str(score) + " right!")
        def multiplication():
            questions = {}
            score = 0

            for i in range(10):
                int_1 = random.randint(1, 50)
                int_2 = random.randint(1, 10)
                operator = "*"
                question = str(int_1) + " " + str(operator) + " " + str(int_2)
                answer = eval(question)
                question += " = "

                questions.update({question: str(answer)})

            for q in questions.keys():
                user_answer = input(q)
                if questions.get(q) == str(user_answer):
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")

            if score < 5:
                print("Keep practicing! You only got " + str(score) + " right!")
            elif score == 10:
                print("Congratulation! All correct! ")
            else:
                print("You got " + str(score) + " right!")
        def division():
            print("Remainder: All the answer should be rounded down.")
            questions = {}
            score = 0

            for i in range(10):
                int_1 = random.randint(25, 100)
                int_2 = random.randint(1, 10)
                operator = "//"
                question = str(int_1) + " " + str(operator) + " " + str(int_2)
                answer = eval(question)
                question += " = "

                questions.update({question: str(answer)})

            for q in questions.keys():
                user_answer = input(q)
                if questions.get(q) == str(user_answer):
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")

            if score < 5:
                print("Keep practicing! You only got " + str(score) + " right!")
            elif score == 10:
                print("Congratulation! All correct! ")
            else:
                print("You got " + str(score) + " right!")

        frame1 = Frame(root)
        frame2 = Frame(root)
        root.title("tkinter frame")

        label = Label(frame1, text="Click to get started", justify=LEFT)
        label.pack(side=LEFT)

        start1 = Button(frame2, text="+", command=sum, height=10, width=17)
        start1.pack()
        start2 = Button(frame2, text="-", command=substraction, height=10, widt=17)
        start2.pack()
        start3 = Button(frame2, text="x", command=multiplication, height=10, width=17)
        start3.pack()
        start4 = Button(frame2, text="/", command=division, height=10, width=17)
        start4.pack()

        frame1.pack(padx=1, pady=1)
        frame2.pack(padx=1, pady=1)

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
root.geometry("500x1000")

app.mainloop()



