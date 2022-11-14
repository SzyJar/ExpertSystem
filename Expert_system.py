import tkinter as tk

class reguly:
    def __init__(self):
        self.napiecie = 0
    def wybierzNapiecie(self, input):
        self.napiecie = input
        
class silnik:
    def __init__(self):
        self.napiecie = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.x5 = 0
    def pobierzDane():
        pass



root = tk.Tk()
root.title("System ekspercki - silniki elektryczne")
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=500, width=500, bg ="#ffffff")
canvas.pack()
#############################################  results frame

def results():
    resultsFrame=tk.Frame(root, bg="#d0d0e1")
    resultsFrame.place(relwidth=0.9,relheight=0.9, relx=0.05, rely=0.05)
    buttonFrame=tk.Frame(resultsFrame, bg="#d0d0e1")
    buttonFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)
    def goBack():
        resultsFrame.destroy()
    backButton = tk.Button(buttonFrame, text="Powrot", padx=10, pady=10, fg="black", bg = "#cccccc", command=goBack)
    backButton.pack()
    
################################################# main frame

frame=tk.Frame(root, bg="#d0d0e1")
frame.place(relwidth=0.9,relheight=0.9, relx=0.05, rely=0.05)

nextQFrame=tk.Frame(root, bg="#d0d0e1")
nextQFrame.place(relwidth=0.2, relheight=0.07, relx=0.4, rely=0.8)

resultsButton = tk.Button(nextQFrame, text="Wyniki", padx=10, pady=10, fg="black", bg = "#cccccc", command=results)
resultsButton.pack()

############################################
root.mainloop()