import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("System ekspercki - silniki elektryczne")
root.resizable(width=False, height=False)

def exitAppCommand():
    quit()

canvas = tk.Canvas(root, height=500, width=500, bg ="#ffffff")
canvas.pack()

#################################################   frames
frame=tk.Frame(root, bg="#d0d0e1")
frame.place(relwidth=0.9,relheight=0.9, relx=0.05, rely=0.05)

exitAppFrame=tk.Frame(root, bg="#33001a")
exitAppFrame.place(relwidth=0.1,relheight=0.07, relx=0.8, rely=0.8)

nextQFrame=tk.Frame(root, bg="#33001a")
nextQFrame.place(relwidth=0.2,relheight=0.07, relx=0.4, rely=0.8)
##############################################   Buttons
exitApp = tk.Button(exitAppFrame, text="Wyjscie", padx=10, pady=10, fg="black", bg = "#cccccc", command=exitAppCommand)
exitApp.pack()

nextQ = tk.Button(nextQFrame, text="Nastepne pytanie", padx=10, pady=10, fg="black", bg = "#cccccc")
nextQ.pack()

root.mainloop()