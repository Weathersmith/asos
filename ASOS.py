import tkinter as tk
from tkinter import ttk
from time import strftime

root = tk.Tk()
root.title("ASOS") #this is the entire application


frame = tk.Frame(root)
frame.grid(row=0, column = 0, sticky="nsew")

time_and_location = tk.Frame(frame)
time_and_location.grid(row=0, column=0, sticky="new")

current_time = tk.Frame(time_and_location)
current_time.grid(row=0, column=0, sticky="w")

clock_label = tk.Label(current_time, text="", font=("Helvetica", 12))
def update_time():
    now_time = time.strftime('%H:%M:%S')
    clock_label.config(text=now_time)
    root.after(1000, update_time)

location = tk.Frame(time_and_location)
location.grid(row=0, column=1, sticky="e")

lbl = Label(current_time, font=('calibri', 12), background='black', foreground='yellow')

lbl.pack()

time()
root.mainloop()

