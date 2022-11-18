import tkinter as tk

class Question:
    def __init__(self):
        self.Value = 0
    def getQuestion(self):
        pass
    def question(self, y):
        self.Value = input
        self.boxValue_0 = tk.Radiobutton(frame, text="0-0", variable=self.Value, value=0)
        self.boxValue_0.place(x=10, y=y, height = 30, width = 100)
        self.boxValue_1 = tk.Radiobutton(frame, text="1", variable=self.Value, value=1)
        self.boxValue_1.place(x=110, y=y, height = 30, width = 100)
        self.boxValue_2 = tk.Radiobutton(frame, text="2", variable=self.Value, value=2)
        self.boxValue_2.place(x=210, y=y, height = 30, width = 100)
        self.boxValue_3 = tk.Radiobutton(frame, text="3", variable=self.Value, value=3)
        self.boxValue_3.place(x=310, y=y, height = 30, width = 100)
    
        
class Engine:
    def __init__(self):
        self.Voltage = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.x5 = 0
    def getData():
        pass



root = tk.Tk()
root.title("Expert system - electrical engines")
#root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=500, width=500, bg ="#ffffff")
canvas.pack()

#############################################  results frame

def results():
    resultsFrame=tk.Frame(root, bg="#d0d0e1")
    resultsFrame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
    buttonFrame=tk.Frame(resultsFrame, bg="#d0d0e1")
    buttonFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)
    def goBack():
        resultsFrame.destroy()
    backButton = tk.Button(buttonFrame, text="Back", padx=10, pady=10, fg="black", bg = "#cccccc", command=goBack)
    backButton.pack()
    
################################################# main frame

frame=tk.Frame(root, bg="#d0d0e1")
frame.place(relwidth=1,relheight=1)

resultsFrame=tk.Frame(root, bg="#d0d0e1")
resultsFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)

resultsButton = tk.Button(resultsFrame, text="Results", padx=10, pady=10, fg="black", bg = "#cccccc", command=results)
resultsButton.pack()

############################################
voltage = Question()
voltage.question(50)

root.mainloop()