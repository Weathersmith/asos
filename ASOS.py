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
clock_label = tk.Label(root, font=('Arial', 12), background='black', foreground='yellow' ) 
clock_label.grid(row=0, column=0, sticky='nw')


#ASOS can be adjusted to different locations, name will be here
location_label = tk.Label(root, text="Location Here!", font=('Arial', 12), background='black', foreground='yellow', justify='right')
location_label.grid(row=0, column=1, sticky='ne', columnspan=12)


data_frame = tk.Frame(root, highlightbackground='blue', highlightthickness=2, background='black')
data_frame.grid(row=1, column=0, columnspan=12, sticky='nsew')


sky_label = tk.Label(data_frame, text="SKY", font=('Arial', 12), background='black', foreground='white')
sky_label.grid(row=0, column=0)

eq1 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq1.grid(row=0, column=1)

sky_textbox = tk.Entry(data_frame, background='black', foreground='white')
sky_textbox.grid(row=0, column=2)


vis_label = tk.Label(data_frame, text="VISIBILITY", font=('Arial', 12), background='black', foreground='white')
vis_label.grid(row=1, column=0)

eq2 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq2.grid(row=1, column=1)

vis_textbox = tk.Entry(data_frame, background='black', foreground='white')
vis_textbox.grid(row=1, column=2)

temp_td_label = tk.Label(data_frame, text="TEMP/DEWPT", font=('Arial', 12), background='black', foreground='white')
temp_td_label.grid(row=1, column = 3)

eq3 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq3.grid(row=1, column=4)

tempc_textbox = tk.Entry(data_frame, background='black', foreground='white')
tempc_textbox.grid(row=1, column=5)

slash_label = tk.Label(data_frame, text="/", background='black', foreground='white')
slash_label.grid(row=1, column=6)

tdc_textbox = tk.Entry(data_frame, background='black', foreground='white')
tdc_textbox.grid(row=1, column=7)

unit_label_c = tk.Label(data_frame, text=" C ", font=('Arial', 12), background='black', foreground='white')
unit_label_c.grid(row=1, column=8)

tempf_textbox = tk.Entry(data_frame, background='black', foreground='white')
tempf_textbox.grid(row=1, column=9)

slash_label_2 = tk.Label(data_frame, text="/", background='black', foreground='white')
slash_label_2.grid(row=1, column=10)

tdf_textbox = tk.Entry(data_frame, background='black', foreground='white')
tdf_textbox.grid(row=1, column=11)

unit_label_f = tk.Label(data_frame, text=" F ", font=('Arial', 12), background='black', foreground='white')
unit_label_f.grid(row=1, column=12)

rvr_label = tk.Label(data_frame, text="RVR", font=('Arial', 12), background='black', foreground='white')
rvr_label.grid(row=3, column=0)

eq4 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq4.grid(row=3, column=1)

rvr_textbox = tk.Entry(data_frame, background='black', foreground='white')
rvr_textbox.grid(row=3, column=2)

wind_label = tk.Label(data_frame, text="WIND DIR/SPD", font=('Arial', 12), background='black', foreground='white')
wind_label.grid(row=3, column=3)

eq5 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq5.grid(row=3, column=4)

wind_textbox = tk.Entry(data_frame, background='black', foreground='white')
wind_textbox.grid(row=3, column=5)

wx_label = tk.Label(data_frame, text="PRESENT WX", font=('Arial', 12), background='black', foreground='white')
wx_label.grid(row=4, column=0)

eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=1)

wx_textbox = tk.Entry(data_frame, background='black', foreground='white')
wx_textbox.grid(row=4, column=2)

altmtr_label = tk.Label(data_frame, text="ALTIMETER", font=('Arial', 12), background='black', foreground='white')
altmtr_label.grid(row=4, column=3)

eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=4)

altmtr_textbox = tk.Entry(data_frame, background='black', foreground='white')
altmtr_textbox.grid(row=4, column=5)

report_prep_frame = tk.Frame(data_frame, background='black')
report_prep_frame.grid(row=5, column=0, columnspan=10, rowspan=2)

report_prep_label = tk.Label(report_prep_frame, font=('ARIAL', 12), text="METAR KSLC 18008KT 10SM FEW045 SCT090 BKN180 OVC260 08/M01 A2988 RMK AO2 SLPNO T00811012",
                                 background='black', foreground='white', pady=10)
report_prep_label.grid(column=0, row=0, sticky='w')

def report_prep():
    pass

last_report_frame = tk.Frame(data_frame, background='black')
last_report_frame.grid(row=6, column=0, columnspan=10, rowspan=2)

last_report_label = tk.Label(report_prep_frame, font=('ARIAL', 12), text="METAR KSLC 17008KT 10SM FEW045 FEW090 SCT180 BKN260 07/00 A2988 RMK AO2 SLPNO T00741003",
                                 background='black', foreground='white', pady=10)
last_report_label.grid(column=0, row=1, sticky='w')

checking_space = tk.Label(data_frame, text="bottom of last report frame")
checking_space.grid(row=7, column=0)





get_time()
root.mainloop()


