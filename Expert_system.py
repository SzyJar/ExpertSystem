import tkinter as tk
from tkinter import filedialog, Text
import os


root =tk.Tk(screenName = "System ekspercki")

def exitApp():
    quit()

canvas = tk.Canvas(root, height=500, width=500, bg ="#ffffff")
canvas.pack()

frame=tk.Frame(root, bg="#33001a")
frame.place(relwidth=0.9,relheight=0.9, relx=0.05, rely=0.05)

exitApp = tk.Button(root, text="Wyjscie", padx=10, pady=10, fg="white", bg = "black", command=exitApp)
exitApp.pack()

root.mainloop()