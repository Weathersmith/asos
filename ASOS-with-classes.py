import tkinter as tk
from tkinter import ttk
import time
import sys

root = tk.Tk()
#root.geometry('1080x720')
root.title('ASOS') #this is the main window
root.configure(bg='black') #the background is black, letters are white or yellow

root.columnconfigure(1, weight=3)
root.rowconfigure(1, weight=3)
root.configure(padx=5, pady=5)

def get_time():   
    time_var = time.strftime("%H:%M:%S %m/%d/%yLST")
    clock_label.config(text=time_var)
    clock_label.after(1000, get_time)

#output of clock function will be in the clock label              
clock_label = tk.Label(root, font=('Terminal', 12), background='black', foreground='yellow' ) 
clock_label.grid(row=0, column=0, sticky='nw')

#ASOS can be adjusted to different locations, name will be here
location_label = tk.Label(root, text="Location Here!", font=('Terminal', 12), background='black', foreground='yellow', justify='right')
location_label.grid(row=0, column=1, sticky='ne', columnspan=12)

data_frame = tk.Frame(root, highlightbackground='blue', highlightthickness=2, background='black')
data_frame.grid(row=1, column=0, columnspan=12, sticky='nsew')

def editScreenEntries(name, row_position, column_position):
    
    
    entry_label = tk.Label(data_frame, text=name, background='black', foreground='white')
    entry_label.grid(row=row_position, column=column_position)

    eq = tk.Label(data_frame, text="=", background='black', foreground='white')
    eq.grid(row=row_position, column=column_position + 1)

    entry_textbox = tk.Entry(data_frame, background='black', foreground='white', width=75)
    entry_textbox.grid(row=row_position, column=column_position + 2)


def tempDewpoint(name, row_position, column_position):

    temp_td_label = tk.Label(data_frame, text=name, font=('Terminal', 12), background='black', foreground='white')
    temp_td_label.grid(row=row_position, column = column_position)

    eq = tk.Label(data_frame, text="=", background='black', foreground='white')
    eq.grid(row=row_position, column=column_position + 1)

    tempc_textbox = tk.Entry(data_frame, background='black', foreground='white', width=5)
    tempc_textbox.grid(row=row_position, column=column_position + 2)

    slash_label = tk.Label(data_frame, text="/", background='black', foreground='white')
    slash_label.grid(row=row_position, column=column_position + 3)

    tdc_textbox = tk.Entry(data_frame, background='black', foreground='white', width=5)
    tdc_textbox.grid(row=row_position, column=column_position + 4)

    unit_label_c = tk.Label(data_frame, text=" C ", font=('Terminal', 12), background='black', foreground='white')
    unit_label_c.grid(row=row_position, column=column_position + 5)

    tempf_textbox = tk.Entry(data_frame, background='black', foreground='white', width=5)
    tempf_textbox.grid(row=row_position, column=column_position + 6)

    slash_label_2 = tk.Label(data_frame, text="/", background='black', foreground='white')
    slash_label_2.grid(row=row_position, column=column_position + 7)

    tdf_textbox = tk.Entry(data_frame, background='black', foreground='white', width=5)
    tdf_textbox.grid(row=row_position, column=column_position + 8)

    unit_label_f = tk.Label(data_frame, text=" F ", font=('Terminal', 12), background='black', foreground='white')
    unit_label_f.grid(row=row_position, column=column_position + 9)

def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * (5/9))

def celsius_to_fahrenheit(celsius):
    return ((celsius*(5/9)) + 32)


sky_condition = editScreenEntries("SKY", 0, 0)
visibility = editScreenEntries("VISIBILITY", 2, 0)
temp_dewpoint = tempDewpoint("TEMP/DEWPT", 2, 3)
rvr = editScreenEntries("RVR", 3, 0)
wind = editScreenEntries("WIND DIR/SPD", 3, 3)
present_wx = editScreenEntries("PRESENT WX", 4, 0)
altimeter = editScreenEntries("ALTIMETER", 4, 3)

get_time()
root.mainloop()
