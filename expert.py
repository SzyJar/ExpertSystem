import tkinter as tk
import os

class Expert:
    
    def __init__(self, master):
        self.data = master.data
        self.question = master.question
        self.category = master.category
        self.box = []
        self.answer = []

    def go_back(self):
        self.resultsFrame.destroy()

    def results(self, master):
        self.resultsFrame=tk.Frame(master, bg="#ffffff")
        self.resultsFrame.place(relwidth=1, relheight=1)
        self.backButton = tk.Button(self.resultsFrame, text="Back", padx=10, pady=10, font=("Tahoma 9 bold"),
                                fg="black", bg = "#cccccc", command=self.go_back)
        self.backButton.place(width=110, height=50, relx=0.45, rely=0.9)
        self.exactLabel = tk.Label(self.resultsFrame, text="Exact match:", bg="#ffffff", fg="#000000", font=("Tahoma 12 bold"), justify="left")
        self.exactLabel.place(height=25, x=10, y=10)
        self.exactList = tk.Listbox(self.resultsFrame,  bg ="#cccccc", fg="#000000", height=19, width=50,
                                    font=("Tahoma 12"), selectmode="single", relief="solid")
        self.exactList.place(width=1080, height=150, x=10, y=45)
        self.closeLabel = tk.Label(self.resultsFrame, text="Close match (Difference of one answer):", bg="#ffffff", fg="#000000", font=("Tahoma 12 bold"), justify="left")
        self.closeLabel.place(height=25, x=10, y=205)
        self.closeList = tk.Listbox(self.resultsFrame,  bg ="#cccccc", fg="#000000", height=19, width=50,
                                    font=("Tahoma 12"), selectmode="single", relief="solid")
        self.closeList.place(width=1080, height=150, x=10, y=240)

    def draw_radio_button(self, text, x, y):
        if x < 0.05:
            self.answer.append(tk.StringVar())
            self.categoryLabel = tk.Label(self.frame, text=self.category[len(self.answer)], bg="#ffffff",
                                     font=("Tahoma 9 bold"))
            self.categoryLabel.place(relx=x, rely=y - 0.03)
        self.box.append(tk.Radiobutton(self.frame, text=text, bg="#ffffff", font=("Tahoma 9"),
                                       value=str(text), variable=self.answer[-1], tristatevalue=0))
        self.box[-1].place(relx=x, rely=y, height = 30, width = 150)

    def type_check(self, input):
        try:
            a = float(input)
            return(True)
        except:
            return(False)

    def search(self, empty=''):
        self.mask = []
        # Make True / False mask
        for i in range(len(self.answer)):
            self.mask.append([])
            for j in range(len(self.data)):
                if self.answer[i].get() == empty or self.answer[i].get() == '':
                    self.mask[i].append(True)
                elif self.data[j][i+1] == self.answer[i].get():
                    self.mask[i].append(True)
                elif ' - ' in self.answer[i].get():
                    timeForPart2 = 0
                    part1 = ''
                    part2 = ''
                    for k in range(len(self.answer[i].get())):
                        if self.answer[i].get()[k] == '-':
                            timeForPart2 = 1
                        elif self.answer[i].get()[k] != ' ' and timeForPart2 == 0:
                            part1 = part1 + self.answer[i].get()[k]
                        elif self.answer[i].get()[k] != ' ' and timeForPart2 == 1:
                            part2 = part2 + self.answer[i].get()[k]
                    try:
                        part1float = float(part1)
                        part2float = float(part2)
                        if float(self.data[j][i+1]) >= part1float and float(self.data[j][i+1]) <= part2float:
                            self.mask[i].append(True)
                        else:
                            self.mask[i].append(False)                         
                    except:
                        self.mask[i].append(False)
                elif self.type_check(self.data[j][i+1]) and float(self.data[j][i+1]) == float(self.answer[i].get()):
                    self.mask[i].append(True)
                else:       
                    self.mask[i].append(False)
        # apply mask on data list
        for i in range(len(self.mask[0])):
            notMatch = 0
            notMatchCategory = []
            notMatchValue = []
            for j in range(len(self.mask)):
                if self.mask[j][i] == False:
                    notMatch = notMatch + 1
                    notMatchCategory.append(self.category[j + 1])
                    notMatchValue.append(self.data[i][j + 1])
                    lastJ = j
            if notMatch == 0:
                self.exactList.insert('end', self.data[i][0])
            if notMatch == 1:
                self.closeList.insert('end', f"{self.data[i][0]} ({notMatchCategory[-1]}: {self.answer[lastJ].get()} -> {notMatchValue[-1]})") 
        if self.exactList.size() == 0:
            self.exactList.insert('end', "None found")
        if self.closeList.size() == 0:
            self.closeList.insert('end', "None found")

    def edit_file(self, file):
        os.startfile(file)

    def main_UI(self, master, file, empty):
        self.canvas = tk.Canvas(master, height=600, width=1100, bg ="#ffffff")
        master.minsize(1100, 600)
        self.canvas.pack()
        self.frame=tk.Frame(master, bg="#ffffff")
        self.frame.place(relwidth=1,relheight=1)
        self.resultsButton = tk.Button(self.frame, text="Results", font=("Tahoma 9 bold"),
                                   fg="black", bg = "#cccccc", command=lambda: [self.results(master), self.search(empty)])
        self.resultsButton.place(width=110, height=50, relx=0.45, rely=0.9)
        self.editButton = tk.Button(self.frame, text="Edit data file", padx=10, pady=10, font=("Tahoma 9 bold"),
                                fg="black", bg = "#cccccc", command=lambda: self.edit_file(file))
        self.editButton.place(width=110, height=50, relx=0.60, rely=0.9)
        self.restartButton = tk.Button(self.frame, text="Reload data file", padx=10, pady=10, font=("Tahoma 9 bold"),
                                       fg="black", bg = "#cccccc", command=lambda:[
                                       master.destroy(),
                                       os.system('python main.py')])
        self.restartButton.place(width=110, height=50, relx=0.71, rely=0.9)
