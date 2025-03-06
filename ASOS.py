import tkinter as tk
from tkinter import ttk
import time
import sys

root = tk.Tk()
root.geometry('785x475')
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
clock_label = tk.Label(root, font=('Terminal', 11), background='black', foreground='yellow' ) 
clock_label.grid(row=0, column=0, sticky='nw')

#ASOS can be adjusted to different locations, name will be here
location_label = tk.Label(root, text="Location Here!", font=('Terminal', 11), background='black', foreground='yellow', justify='right')
location_label.grid(row=0, column=1, sticky='ne', columnspan=12)
#this is the box most every screen will populate within
data_frame = tk.Frame(root, highlightbackground='blue', highlightthickness=2, background='black')
data_frame.grid(row=1, column=0, columnspan=12, sticky='nsew')

#the following is for the edit screen
#starting with sky condition
sky_label = tk.Label(data_frame, text="SKY", font=('Terminal', 11), background='black', foreground='white')
sky_label.grid(row=0, column=0, pady=5)
eq1 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq1.grid(row=0, column=1)
sky_textbox = tk.Entry(data_frame, background='gray13', foreground='white', state='normal', disabledbackground='black', highlightthickness=0)
sky_textbox.grid(row=0, column=2, columnspan=11, sticky='ew', pady=5)

#visibility
vis_label = tk.Label(data_frame, text="VISIBILITY", font=('Terminal', 11), background='black', foreground='white')
vis_label.grid(row=1, column=0, pady=5)
eq2 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq2.grid(row=1, column=1)
vis_textbox = tk.Entry(data_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black', highlightthickness=0)
vis_textbox.grid(row=1, column=2, pady=5, sticky='w')

#temperature and dewpoint
temp_td_label = tk.Label(data_frame, text="TEMP/DEWPT", font=('Terminal', 11), background='black', foreground='white')
temp_td_label.grid(row=1, column=3, pady=5)
eq3 = tk.Label(data_frame, text="=", font=('Terminal', 11), background='black', foreground='white')
eq3.grid(row=1, column=4)
temp_frame = tk.Frame(data_frame, background='black')
temp_frame.grid(row=1, column=5, columnspan=7, pady=5, sticky='w')

tempc_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled', disabledbackground='black', highlightthickness=0)
tempc_textbox.pack(side='left')
slash_label = tk.Label(temp_frame, text="/", font=('Terminal', 11), background='black', foreground='white')
slash_label.pack(side='left')
tdc_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled', disabledbackground='black', highlightthickness=0)
tdc_textbox.pack(side='left')
unit_label_c = tk.Label(temp_frame, text=" C ", font=('Terminal', 11), background='black', foreground='white')
unit_label_c.pack(side='left')
tempf_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled', disabledbackground='black', highlightthickness=0)
tempf_textbox.pack(side='left')
slash_label_2 = tk.Label(temp_frame, text="/", font=('Terminal', 11), background='black', foreground='white')
slash_label_2.pack(side='left')
tdf_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled', disabledbackground='black', highlightthickness=0)
tdf_textbox.pack(side='left')
unit_label_f = tk.Label(temp_frame, text=" F ", font=('Terminal', 11), background='black', foreground='white')
unit_label_f.pack(side='left')

#Runway Visual Range (RVR)
rvr_label = tk.Label(data_frame, text="RVR", font=('Terminal', 11), background='black', foreground='white')
rvr_label.grid(row=3, column=0, pady=5)
eq4 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq4.grid(row=3, column=1)
rvr_textbox = tk.Entry(data_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black', highlightthickness=0)
rvr_textbox.grid(row=3, column=2, pady=5, sticky='w')

#winds
wind_label = tk.Label(data_frame, text="WIND DIR/SPD", font=('Terminal', 11), background='black', foreground='white')
wind_label.grid(row=3, column=3, pady=5)
eq5 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq5.grid(row=3, column=4)
wind_textbox = tk.Entry(data_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black', highlightthickness=0)
wind_textbox.grid(row=3, column=5, pady=5, sticky='w')

#present weather/obstructions
wx_label = tk.Label(data_frame, text="PRESENT WX", font=('Terminal', 11), background='black', foreground='white')
wx_label.grid(row=4, column=0, pady=5)
eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=1)
wx_textbox = tk.Entry(data_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black', highlightthickness=0)
wx_textbox.grid(row=4, column=2, pady=5, sticky='w')

#altimeter/barometric pressure
altmtr_label = tk.Label(data_frame, text="ALTIMETER", font=('Terminal', 11), background='black', foreground='white')
altmtr_label.grid(row=4, column=3, pady=5)
eq6 = tk.Label(data_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=4)
altmtr_textbox = tk.Entry(data_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black', highlightthickness=0)
altmtr_textbox.grid(row=4, column=5, pady=5, sticky='w')

#remarks... these will be populated based on data and entries in other screens
remarks_label = tk.Label(data_frame, text="REMARKS", font=('Terminal', 11), background='black', foreground='white' ).grid(row=5, column=0, pady=5)
eq7 = tk.Label(data_frame, text="=", background='black', foreground='white').grid(row=5, column=1)
remarks_placeholder = tk.Label(data_frame, text="AO2 SLPNO", font=('Terminal', 11), background='black', foreground='white' ).grid(row=5, column=2, pady=5, sticky='w', columnspan=10)

#This is the frame where the METAR shown is what will be transmitted, and can change every minute based on data and inputs
report_prep_frame = tk.Frame(data_frame, background='black')
report_prep_frame.grid(row=6, column=0, columnspan=12, rowspan=2)
report_prep_label = tk.Label(report_prep_frame, font=('Terminal', 11), text="METAR KSLC 010554 18008KT 1 1/2SM RA BR FEW045CB SCT090 BKN180 OVC260 08/M01 A2988 RMK AO2 SLPNO CB VC NE MOV N T00811012",
                                   background='black', foreground='white', pady=30, padx=10, wraplength=750, justify='left')
report_prep_label.pack(side='left')


"""

def report_prep():
    pass

last_report_frame = tk.Frame(data_frame, background='black')
last_report_frame.grid(row=7, column=0, columnspan=10, rowspan=2)

last_report_label = tk.Label(report_prep_frame, font=('ARIAL', 12), text="METAR KSLC 010654 17008KT 10SM FEW045 FEW090 SCT180 BKN260 07/00 A2988 RMK AO2 SLPNO T00741003",
                                 background='black', foreground='white', pady=10)
last_report_label.grid(column=0, row=1, sticky='w')

checking_space = tk.Label(data_frame, text="bottom of last report frame")
checking_space.grid(row=7, column=0)

"""

#this is a separate frame in the edit screen which can show wx variables, logged in users, and other info
#for now, this is just showing the weather variables section
wx_vars = tk.Frame(data_frame, background='black')
wx_vars.grid(row=12, column=0, columnspan=9)

#one minute observation winds
mag_wind_label = tk.Label(wx_vars, text="MAG WIND: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=0, column=0, sticky='w')
mag_wind_value = tk.Label(wx_vars, text="270/09G27", background='black', foreground='white', font=('Terminal', 11)).grid(row=0, column=1)

#current relative humidity
rel_hum_label = tk.Label(wx_vars, text="RELATIVE HUMIDITY: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=1, column=0, sticky='w')
rel_hum_value = tk.Label(wx_vars, text="70%", background='black', foreground='white', font=('Terminal', 11)).grid(row=1, column=1)

#various pressure vales, starting with sea level pressure, unadjusted station pressure, altitude compared to sea level, and comparable altitude for a density in a standard atmosphere
slp_label = tk.Label(wx_vars, text="SEA LEVEL PRESSURE: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=2, column=0, sticky='w')
slp_value = tk.Label(wx_vars, text="1013.25", background='black', foreground='white', font=('Terminal', 11)).grid(row=2, column=1)

station_pressure_label = tk.Label(wx_vars, text="STATION PRESSURE: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=0, column=2, sticky='w')
station_pressure_value = tk.Label(wx_vars, text="29.59", background='black', foreground='white', font=('Terminal', 11)).grid(row=0, column=3)

pressure_altitude_label = tk.Label(wx_vars, text="PRESSURE ALTITUDE: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=1, column=2, sticky='w')
pressure_altitude_value = tk.Label(wx_vars, text="4221", background='black', foreground='white', font=('Terminal', 11)).grid(row=1, column=3)

density_altitude_label = tk.Label(wx_vars, text="DENSITY ALTITUDE: ", background='black', foreground='white', font=('Terminal', 11)).grid(row=2, column=2, sticky='w')
density_altitude_value = tk.Label(wx_vars, text="6070", background='black', foreground='white', font=('Terminal', 11)).grid(row=2, column=3)


#this keypad is present on all screens. based on the screen, what each key says and where it will direct to changes
#like those old text adventure games, but you dont have to draw a map yourself to keep track of things
#wx_zorg

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
    
#when starting up the system, this is the default keypad setup
keypad_guide("SIGN", "EDIT", "AUX", "REVUE", "TWR", " ", "PRINT", "GENOB", "CMD" )
get_time()
root.mainloop()
