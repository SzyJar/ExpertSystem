import tkinter as tk
import os

class Expert:
    
    def __init__(self, data, question):
        self.data = data
        self.question = question
        self.box = []
        self.answer = []

    def go_back(self):
        self.resultsFrame.destroy()

    def results_UI(self, master):
        self.resultsFrame=tk.Frame(master, bg="#ffffff")
        self.resultsFrame.place(relwidth=1, relheight=1)
        self.buttonFrame=tk.Frame(self.resultsFrame, bg="#ffffff")
        self.buttonFrame.place(width=100, height=100, relx=0.45, rely=0.9)
        self.backButton = tk.Button(self.buttonFrame, text="Back", padx=10, pady=10,
                                fg="black", bg = "#cccccc", command=self.go_back)
        self.backButton.pack()

    def draw_radio_button(self, text, x, y):
        if x < 0.05:
            self.answer.append(tk.StringVar())
        self.box.append(tk.Radiobutton(self.frame, text=text, bg="#ffffff", font=("Tahoma 9 bold"),
                                       variable=self.answer[-1], value=str(text), tristatevalue=0))
        self.box[-1].place(relx=x, rely=y, height = 30, width = 150)

    def edit_file(self, file):
        os.startfile(file)

    def draw_UI(self, master, file):
        self.canvas = tk.Canvas(master, height=600, width=1100, bg ="#ffffff")
        self.canvas.pack()
        self.frame=tk.Frame(master, bg="#ffffff")
        self.frame.place(relwidth=1,relheight=1)
        self.buttonFrame=tk.Frame(master, bg="#ffffff")
        self.buttonFrame.place(width=100, height=100, relx=0.45, rely=0.9)
        self.resultsButton = tk.Button(self.buttonFrame, text="Results", padx=10,
                                  pady=10, fg="black", bg = "#cccccc", command=lambda: self.results_UI(master))
        self.resultsButton.pack()
        self.editFrame=tk.Frame(master, bg="#ffffff")
        self.editFrame.place(width=200, height=100, relx=0.6, rely=0.9)
        self.editButton = tk.Button(self.editFrame, text="Edit current data file", padx=10, pady=10,
                                fg="black", bg = "#cccccc", command=lambda: self.edit_file(file))
        self.editButton.pack()