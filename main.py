import tkinter as tk

from database import DataBase
from expert import Expert


root = tk.Tk()
root.title("Expert system - electrical engines")

# Data file path
dataFile = 'data\silniki.csv'

engines = DataBase(dataFile)
engines.generate_questions()

expert = Expert(engines.data, engines.question)
expert.draw_UI(root, dataFile)

for i in range(len(engines.question)):
    x = 0.01 # x pos for first question
    spacingX = 0.2 # spacing for questions
    y = 0.01 # y pos for first question
    spacingY = 0.1 # spacing for questions
    
    for j in range(len(engines.question[i])):
        expert.draw_radio_button(engines.question[i][j],x + spacingX * j,
                                 y + spacingY * i)

root.mainloop()