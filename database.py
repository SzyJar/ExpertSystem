import csv as csv
from tkinter import messagebox


class DataBase:

    def __init__(self, path):
        # read data from file
        self.data = []
        try:
            with open(path, "r", newline = '') as file:
                reader = csv.reader(file, delimiter = ';')
                for row in reader:
                    self.data.append(row)
        except:
            messagebox.showerror("Unable to load file", "An error occurred while loading the data file")
        self.category = self.data.pop(0)

    def generate_questions(self):
        # prepare data to make questions
        self.question = []
        for i in range(1, len(self.data[0])):
            self.question.append([])
            for j in range(len(self.data)):
                if j == 0:
                    self.question[i-1].append(self.data[j][i])
                elif j > 0 and not(self.data[j][i] in self.question[i-1]):
                    self.question[i-1].append(self.data[j][i])
        # convert data to float if possible (easier manipulation)
        for i in range(len(self.question)):
            for j in range(len(self.question[i])):
                try:
                    self.question[i][j] = float(self.question[i][j])
                except:
                    pass
        # sort answers to questions
        for i in range(len(self.question)):
            try:
                self.question[i].sort()
            except:
                messagebox.showwarning("Mismatch data type",
                                       f'"{self.category[i+1]}" - Category contains more than one data type.\n Possible data loss!')
            # if float data type - reduce number of answers to question (5 max)
            if len(self.question[i]) > 5 and type(self.question[i][0]) == float:
                if len(self.question[i]) > 5:
                    for j in range(0, len(self.question[i]), 1):
                        if (j + 4) < len(self.question[i]):
                            del self.question[i][j+1]
                            del self.question[i][j+1]
                            del self.question[i][j+1]
                            self.question[i][j] = str(self.question[i][j]) + ' - ' + str(self.question[i].pop(j + 1))
                        elif (j + 3) < len(self.question[i]):
                            del self.question[i][j+1]
                            del self.question[i][j+1]
                            self.question[i][j] = str(self.question[i][j]) + ' - ' + str(self.question[i].pop(j + 1))
                        elif (j + 2) < len(self.question[i]):
                            del self.question[i][j+1]
                            self.question[i][j] = str(self.question[i][j]) + ' - ' + str(self.question[i].pop(j + 1))
                        elif (j + 1) < len(self.question[i]):
                            self.question[i][j] = str(self.question[i][j]) + ' - ' + str(self.question[i].pop(j + 1))