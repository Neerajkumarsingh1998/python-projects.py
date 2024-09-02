import tkinter as tk
from time import strftime
from datetime import datetime
root=tk.Tk()
root.title("Digital clock")
def time():
    string=strftime('%H:%M:%S  %A  \n  %D %p')
    label.config(text=string)
    label.after(1000,time)
label=tk.Label(root,font=('calibri',50,'bold'),background='white',foreground='blue')
label.pack(anchor='center')
time()
root.mainloop()
