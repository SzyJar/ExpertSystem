import tkinter as tk

from database import DataBase


root = tk.Tk()
root.title("Expert system - electrical engines")
root.resizable(width=False, height=False)

class Expert:
    
    def __init__(self, data, question):
        self.data = data
        self.question = question

    def go_back(self):
            self.resultsFrame.destroy()

    def results(self, master):
            self.resultsFrame=tk.Frame(master, bg="#d0d0e1")
            self.resultsFrame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
            self.buttonFrame=tk.Frame(self.resultsFrame, bg="#d0d0e1")
            self.buttonFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)
            self.backButton = tk.Button(self.buttonFrame, text="Back", padx=10, pady=10,
                                   fg="black", bg = "#cccccc", command=self.go_back)
            self.backButton.pack()

    def draw_UI(self, master):
        
        self.canvas = tk.Canvas(master, height=600, width=1100, bg ="#ffffff")
        self.canvas.pack()

        self.frame=tk.Frame(master, bg="#d0d0e1")
        self.frame.place(relwidth=1,relheight=1)

        self.resultsFrame=tk.Frame(master, bg="#d0d0e1")
        self.resultsFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)

        self.resultsButton = tk.Button(self.resultsFrame, text="Results", padx=10,
                                  pady=10, fg="black", bg = "#cccccc", command=self.results(master))
        self.resultsButton.pack()

        for i in range(len(self.question)):
            x = 10 # x pos for first question
            spacingX = 200 # spacing for questions
            y = 10 # y pos for first question
            spacingY = 30 # spacing for questions

            #use list instead of declaring every radio box manually!

            if i == 0:
                self.question_0 = 0
                self.boxValue_0_0 = tk.Radiobutton(self.frame, text=self.question[i][0],
                                                   variable=self.question_0, value=0)
                self.boxValue_0_0.place(x=x, y=y, height = 30, width = 100)
                if len(self.question[i]) > 1:
                    
                    self.boxValue_0_1 = tk.Radiobutton(self.frame, text=self.question[i][1],
                                                       variable=self.question_0, value=0)
                    self.boxValue_0_1.place(x=110, y=y, height = 30, width = 100)
                if len(self.question[i]) > 2:
                    self.boxValue_0_2 = tk.Radiobutton(self.frame, text=self.question[i][2],
                                                       variable=self.question_0, value=0)
                    self.boxValue_0_2.place(x=210, y=y, height = 30, width = 100)
                if len(self.question[i]) > 3:
                    self.boxValue_0_3 = tk.Radiobutton(self.frame, text=self.question[i][3],
                                                       variable=self.question_0, value=0)
                    self.boxValue_0_3.place(x=310, y=y, height = 30, width = 100)
                if len(self.question[i]) > 4:
                    self.boxValue_0_4 = tk.Radiobutton(self.frame, text=self.question[i][4],
                                                       variable=self.question_0, value=0)
                    self.boxValue_0_4.place(x=410, y=y, height = 30, width = 100)
            elif i == 1:
                self.question_1 = 0
                self.boxValue_1_0 = tk.Radiobutton(self.frame, text=self.question[i][0],
                                                   variable=self.question_0, value=0)
                if len(self.question[i]) > 1:
                    self.boxValue_1_0.place(x=10, y=y+spacingY, height = 30, width = 100)
                    self.boxValue_1_1 = tk.Radiobutton(self.frame, text=self.question[i][1],
                                                       variable=self.question_0, value=0)
                if len(self.question[i]) > 2:
                    self.boxValue_1_1.place(x=110, y=y+spacingY, height = 30, width = 100)
                    self.boxValue_1_2 = tk.Radiobutton(self.frame, text=self.question[i][2],
                                                       variable=self.question_0, value=0)
                    self.boxValue_1_2.place(x=210, y=y+spacingY, height = 30, width = 100)
                if len(self.question[i]) > 3:
                    self.boxValue_1_3 = tk.Radiobutton(self.frame, text=self.question[i][3],
                                                       variable=self.question_0, value=0)
                    self.boxValue_1_3.place(x=310, y=y+spacingY, height = 30, width = 100)
                if len(self.question[i]) > 4:
                    self.boxValue_1_4 = tk.Radiobutton(self.frame, text=self.question[i][4],
                                                       variable=self.question_0, value=0)
                    self.boxValue_1_4.place(x=410, y=y+spacingY, height = 30, width = 100)


engines = DataBase('data\silniki.csv')
engines.generate_questions()

expert = Expert(engines.data, engines.question)
expert.draw_UI(root)

root.mainloop()