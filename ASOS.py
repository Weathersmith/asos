import tkinter as tk
from tkinter import ttk
import time
import sys

root = tk.Tk()
#root.geometry('1080x720')
root.title('ASOS') #this is the main window
root.geometry('745x390')
root.configure(bg='black') #the background is black, letters are white or yellow

root.columnconfigure(1, weight=3)
root.rowconfigure(1, weight=3)
root.configure(padx=5, pady=5)

def get_time():   
    time_var = time.strftime("%H:%M:%S %m/%d/%yLST")
    clock_label.config(text=time_var)
    clock_label.after(1000, get_time)

#output of clock function will be in the clock label              
clock_label = tk.Label(root, font=('Terminal', 11), background='black', foreground='yellow' ) 
clock_label.grid(row=0, column=0, sticky='nw')

#ASOS can be adjusted to different locations, name will be here
location_label = tk.Label(root, text="Location Here!", font=('Terminal', 11), background='black', foreground='yellow', justify='right')
location_label.grid(row=0, column=1, sticky='ne', columnspan=12)

data_frame = tk.Frame(root, highlightbackground='blue', highlightthickness=2, background='black')
data_frame.grid(row=1, column=0, columnspan=12, sticky='nsew')

sky_label = tk.Label(data_frame, text="SKY", font=('Terminal', 11), background='black', foreground='white')
sky_label.grid(row=0, column=0, pady=5)

eq1 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq1.grid(row=0, column=1)

sky_textbox = tk.Entry(data_frame, background='black', foreground='white')
sky_textbox.grid(row=0, column=2, columnspan=12, sticky='ew', pady=5)

vis_label = tk.Label(data_frame, text="VISIBILITY", font=('Terminal', 11), background='black', foreground='white')
vis_label.grid(row=1, column=0, pady=5)

eq2 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq2.grid(row=1, column=1)

vis_textbox = tk.Entry(data_frame, background='black', foreground='white')
vis_textbox.grid(row=1, column=2, pady=5, sticky='w')


temp_td_label = tk.Label(data_frame, text="TEMP/DEWPT", font=('Terminal', 11), background='black', foreground='white')
temp_td_label.grid(row=1, column=3, pady=5)

eq3 = tk.Label(data_frame, text="=", font=('Terminal', 11), background='black', foreground='white')
eq3.grid(row=1, column=4)

temp_frame = tk.Frame(data_frame, background='black')
temp_frame.grid(row=1, column=5, columnspan=7, pady=5, sticky='w')

tempc_textbox = tk.Entry(temp_frame, background='black', foreground='white', width=5)
tempc_textbox.pack(side='left')

slash_label = tk.Label(temp_frame, text="/", font=('Terminal', 11), background='black', foreground='white')
slash_label.pack(side='left')

tdc_textbox = tk.Entry(temp_frame, background='black', foreground='white', width=5)
tdc_textbox.pack(side='left')

unit_label_c = tk.Label(temp_frame, text=" C ", font=('Terminal', 11), background='black', foreground='white')
unit_label_c.pack(side='left')

tempf_textbox = tk.Entry(temp_frame, background='black', foreground='white', width=5)
tempf_textbox.pack(side='left')

slash_label_2 = tk.Label(temp_frame, text="/", font=('Terminal', 11), background='black', foreground='white')
slash_label_2.pack(side='left')

tdf_textbox = tk.Entry(temp_frame, background='black', foreground='white', width=5)
tdf_textbox.pack(side='left')

unit_label_f = tk.Label(temp_frame, text=" F ", font=('Terminal', 11), background='black', foreground='white')
unit_label_f.pack(side='left')

rvr_label = tk.Label(data_frame, text="RVR", font=('Terminal', 11), background='black', foreground='white')
rvr_label.grid(row=3, column=0, pady=5)

eq4 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq4.grid(row=3, column=1)

rvr_textbox = tk.Entry(data_frame, background='black', foreground='white')
rvr_textbox.grid(row=3, column=2, pady=5, sticky='w')

wind_label = tk.Label(data_frame, text="WIND DIR/SPD", font=('Terminal', 11), background='black', foreground='white')
wind_label.grid(row=3, column=3, pady=5)

eq5 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq5.grid(row=3, column=4)

wind_textbox = tk.Entry(data_frame, background='black', foreground='white')
wind_textbox.grid(row=3, column=5, pady=5, sticky='w')

wx_label = tk.Label(data_frame, text="PRESENT WX", font=('Terminal', 11), background='black', foreground='white')
wx_label.grid(row=4, column=0, pady=5)

eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=1)

wx_textbox = tk.Entry(data_frame, background='black', foreground='white')
wx_textbox.grid(row=4, column=2, pady=5, sticky='w')

altmtr_label = tk.Label(data_frame, text="ALTIMETER", font=('Terminal', 11), background='black', foreground='white')
altmtr_label.grid(row=4, column=3, pady=5)

eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=4)

altmtr_textbox = tk.Entry(data_frame, background='black', foreground='white')
altmtr_textbox.grid(row=4, column=5, pady=5, sticky='w')

remarks_label = tk.Label(data_frame, text="REMARKS", font=('Terminal', 11), background='black', foreground='white' )
remarks_label.grid(row=5, column=0, pady=5)

eq7 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq7.grid(row=5, column=1)

remarks_placeholder = tk.Label(data_frame, text="AO2 SLPNO", font=('Terminal', 11), background='black', foreground='white' )
remarks_placeholder.grid(row=5, column=2, pady=5, sticky='w', columnspan=10)

report_prep_frame = tk.Frame(data_frame, background='black')
report_prep_frame.grid(row=6, column=0, columnspan=12, rowspan=2)

report_prep_label = tk.Label(report_prep_frame, font=('Terminal', 11), text="METAR KSLC 18008KT 10SM FEW045 SCT090 BKN180 OVC260 08/M01 A2988 RMK AO2 SLPNO T00811012",
                                 background='black', foreground='white', pady=30, padx=10)
report_prep_label.pack(side='left')



"""

def report_prep():
    pass

last_report_frame = tk.Frame(data_frame, background='black')
last_report_frame.grid(row=6, column=0, columnspan=10, rowspan=2)

last_report_label = tk.Label(report_prep_frame, font=('ARIAL', 12), text="METAR KSLC 17008KT 10SM FEW045 FEW090 SCT180 BKN260 07/00 A2988 RMK AO2 SLPNO T00741003",
                                 background='black', foreground='white', pady=10)
last_report_label.grid(column=0, row=1, sticky='w')

checking_space = tk.Label(data_frame, text="bottom of last report frame")
checking_space.grid(row=7, column=0)

"""

wx_vars = tk.Frame(data_frame, background='black')
wx_vars.grid(row=12, column=0, columnspan=9)

mag_wind = tk.Label(wx_vars, text="MAG WIND:", background='black', foreground='white', font=('Terminal', 11) )
mag_wind.grid(row=0, column=0)

rel_hum = tk.Label(wx_vars, text="RELATIVE HUMIDITY:", background='black', foreground='white', font=('Terminal', 11))
rel_hum.grid(row=1, column=0)

slp = tk.Label(wx_vars, text="SEA LEVEL PRESSURE:", background='black', foreground='white', font=('Terminal', 11))
slp.grid(row=2, column=0)

station_pressure = tk.Label(wx_vars, text="STATION PRESSURE:", background='black', foreground='white', font=('Terminal', 11) )
station_pressure.grid(row=0, column=1)

pressure_altitude = tk.Label(wx_vars, text="PRESSURE ALTITUDE:", background='black', foreground='white', font=('Terminal', 11))
pressure_altitude.grid(row=1, column=1)

density_altitude = tk.Label(wx_vars, text="DENSITY ALTITUDE:", background='black', foreground='white', font=('Terminal', 11))
density_altitude.grid(row=2, column=1)


def keypad_guide(text1, text2, text3, text4, text5, text6, text7, text8, text9):

    keypad_frame = tk.Frame(data_frame, background='black', highlightbackground='blue', highlightthickness=2)
    keypad_frame.grid(row=12, column=10, sticky='se', ipady=36, ipadx=36)

    label_1 = tk.Label(keypad_frame, text=text1, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_1.grid(row=2, column=0, sticky='nsew')

    label_2 = tk.Label(keypad_frame, text=text2, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_2.grid(row=2, column=1, sticky='nsew')

    label_3 = tk.Label(keypad_frame, text=text3, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_3.grid(row=2, column=2, sticky='nsew')

    label_4 = tk.Label(keypad_frame, text=text4, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_4.grid(row=1, column=0, sticky='nsew')

    label_5 = tk.Label(keypad_frame, text=text5, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_5.grid(row=1, column=1, sticky='nsew')

    label_6 = tk.Label(keypad_frame, text=text6, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_6.grid(row=1, column=2,  sticky='nsew')

    label_7 = tk.Label(keypad_frame, text=text7, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_7.grid(row=0, column=0, sticky='nsew')

    label_8 = tk.Label(keypad_frame, text=text8, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_8.grid(row=0, column=1, sticky='nsew')

    label_9 = tk.Label(keypad_frame, text=text9, font=('Terminal', 11), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
    label_9.grid(row=0, column=2, sticky='nsew')

    keypad_frame.grid_rowconfigure(0, weight=1)
    keypad_frame.grid_rowconfigure(1, weight=1)
    keypad_frame.grid_rowconfigure(2, weight=1)
    keypad_frame.grid_columnconfigure(0, weight=1)
    keypad_frame.grid_columnconfigure(1, weight=1)
    keypad_frame.grid_columnconfigure(2, weight=1)
    

keypad_guide("SIGN", "EDIT", "AUX", "REVUE", "TWR", " ", "PRINT", "GENOB", "CMD" )
get_time()
root.mainloop()
