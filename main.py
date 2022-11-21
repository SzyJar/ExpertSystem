import tkinter as tk

from database import DataBase
from expert import Expert

root = tk.Tk()

# Application settings
dataFilePath = 'data\silniki.csv'
root.title("Expert system\t\t" + dataFilePath)
disableQuestionText = 'Show all'
###

engines = DataBase(dataFilePath)
engines.generate_questions()

expert = Expert(engines)
expert.main_UI(root, dataFilePath, disableQuestionText)

for i in range(len(engines.question)):
    x = 0.01 # x pos for first question
    spacingX = 0.166 # spacing for questions
    y = 0.05 # y pos for first question
    spacingY = 0.1 # spacing for questions
    
    for j in range(len(engines.question[i])):
        expert.draw_radio_button(engines.question[i][j],x + spacingX * j,
                                 y + spacingY * i)
    # last radio box - disable question
    expert.draw_radio_button(disableQuestionText,x + spacingX * 5,
                                 y + spacingY * i)

root.mainloop()