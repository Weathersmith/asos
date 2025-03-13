import tkinter as tk
from tkinter import ttk
import time

#global variables
entries_state = 0

window = tk.Tk()
window.geometry('1200x900')
window.resizable(0, 0)
window.title('ASOS') #this is the main window

window.configure(bg='black') #the background is black, letters are white or yellow


clock_and_location_frame = tk.Frame(window, background='black')
clock_and_location_frame.pack(side='top', fill = 'both')
clock_and_location_frame.grid_columnconfigure(0, weight = 1)
clock_and_location_frame.grid_columnconfigure(1, weight = 1)

#where all of the entry fields, data, and useful stuff shows up
oid_frame = tk.Frame(window, background='black', highlightbackground='blue', highlightthickness=2)
oid_frame.pack(side = 'top', fill = 'both', expand = 'True')


#breaking down the screen into three main fields to build within
entry_frame = tk.Frame(oid_frame, background='black')
entry_frame.pack(side = 'top', fill = 'both', expand = 'True')

parent_report_frame = tk.Frame(oid_frame, background='black')
parent_report_frame.pack(side = 'top', fill = 'both', expand = 'True')

keypad_misc_frame = tk.Frame(oid_frame, background='black')
keypad_misc_frame.pack(side = 'top', fill = 'both')


#report frame gets broken down into the prepped field and the last reported field
prep_report_frame = tk.Frame(parent_report_frame, background = 'gray25')
prep_report_frame.pack(side = 'top', fill = 'x', padx = 5, expand = 'True')

last_report_frame = tk.Frame(parent_report_frame, background = 'black')
last_report_frame.pack(side = 'top', fill = 'x', padx = 5, expand = 'True')

#frame for miscellaneous content such as wx variables, sign in prompt, logged in users, etc
misc_frame = tk.Frame(keypad_misc_frame, background='black')
misc_frame.pack(side = 'left', fill = 'both', expand = 'True', ipady=25)

keypad_frame = tk.Frame(keypad_misc_frame, background='black',)
keypad_frame.pack(side = 'left', fill = 'both')
        

#this is where the stuff that fill in the frames created above begins
def get_time():   
    time_var = time.strftime("%H:%M:%S %m/%d/%yLST")
    clock_label.config(text=time_var)
    clock_label.after(1000, get_time)

#output of clock function will be in the clock label              
clock_label = tk.Label(clock_and_location_frame, font=('Terminal', 15), background='black', foreground='yellow' ) 
clock_label.grid(row=0, column=0, sticky='w')


#ASOS can be adjusted to different locations, name will be here
location_label = tk.Label(clock_and_location_frame, text="Location Here!", font=('Terminal', 15), background='black',
                          foreground='yellow', justify='right')
location_label.grid(row=0, column=1, sticky='e')


#stuff for the entry frame
sky_label = tk.Label(entry_frame, text="SKY", font=('Terminal', 15), background='black', foreground='white')
sky_label.grid(row=0, column=0, pady=5)
eq1 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq1.grid(row=0, column=1)
sky_textbox = tk.Entry(entry_frame, background='gray20', foreground='white', state='disabled', disabledbackground='black',
                       highlightthickness=0, font=('Terminal', 15))
sky_textbox.grid(row=0, column=2, columnspan=12, sticky='w', pady=5)
entry_frame.grid_columnconfigure(0, weight=0)
entry_frame.grid_columnconfigure(1, weight=0)
entry_frame.grid_columnconfigure(2, weight=1)

#visibility
vis_label = tk.Label(entry_frame, text="VISIBILITY", font=('Terminal', 15), background='black', foreground='white')
vis_label.grid(row=1, column=0, pady=5)
eq2 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq2.grid(row=1, column=1)
vis_textbox = tk.Entry(entry_frame, background='dark gray', foreground='white', state='disabled', disabledbackground='black',
                       highlightthickness=0, font=('Terminal', 15))
vis_textbox.grid(row=1, column=2, pady=5, sticky='w')

#temperature and dewpoint
temp_td_label = tk.Label(entry_frame, text="TEMP/DEWPT", font=('Terminal', 15), background='black', foreground='white')
temp_td_label.grid(row=1, column=3, pady=5)
eq3 = tk.Label(entry_frame, text="=", font=('Terminal', 15), background='black', foreground='white')
eq3.grid(row=1, column=4)
temp_frame = tk.Frame(entry_frame, background='black')
temp_frame.grid(row=1, column=5, columnspan=7, pady=5, sticky='w')

tempc_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled',
                         disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
tempc_textbox.pack(side='left')
slash_label = tk.Label(temp_frame, text="/", font=('Terminal', 15), background='black', foreground='white')
slash_label.pack(side='left')
tdc_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled',
                       disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
tdc_textbox.pack(side='left')
unit_label_c = tk.Label(temp_frame, text=" C ", font=('Terminal', 15), background='black', foreground='white')
unit_label_c.pack(side='left')
tempf_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled',
                         disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
tempf_textbox.pack(side='left')
slash_label_2 = tk.Label(temp_frame, text="/", font=('Terminal', 15), background='black', foreground='white')
slash_label_2.pack(side='left')
tdf_textbox = tk.Entry(temp_frame, background='dark gray', foreground='white', width=5, state='disabled',
                       disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
tdf_textbox.pack(side='left')
unit_label_f = tk.Label(temp_frame, text=" F ", font=('Terminal', 15), background='black', foreground='white')
unit_label_f.pack(side='left')

#Runway Visual Range (RVR)
rvr_label = tk.Label(entry_frame, text="RVR", font=('Terminal', 15), background='black', foreground='white')
rvr_label.grid(row=3, column=0, pady=5)
eq4 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq4.grid(row=3, column=1)
rvr_textbox = tk.Entry(entry_frame, background='dark gray', foreground='white', state='disabled',
                       disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
rvr_textbox.grid(row=3, column=2, pady=5, sticky='w')

#winds
wind_label = tk.Label(entry_frame, text="WIND DIR/SPD", font=('Terminal', 15), background='black', foreground='white')
wind_label.grid(row=3, column=3, pady=5)
eq5 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq5.grid(row=3, column=4)
wind_textbox = tk.Entry(entry_frame, background='dark gray', foreground='white', state='disabled',
                        disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
wind_textbox.grid(row=3, column=5, pady=5, sticky='w')

#present weather/obstructions
wx_label = tk.Label(entry_frame, text="PRESENT WX", font=('Terminal', 15), background='black', foreground='white')
wx_label.grid(row=4, column=0, pady=5)
eq6 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=1)
wx_textbox = tk.Entry(entry_frame, background='dark gray', foreground='white', state='disabled',
                      disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
wx_textbox.grid(row=4, column=2, pady=5, sticky='w')

#altimeter/barometric pressure
altmtr_label = tk.Label(entry_frame, text="ALTIMETER", font=('Terminal', 15), background='black', foreground='white')
altmtr_label.grid(row=4, column=3, pady=5)
eq6 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq6.grid(row=4, column=4)
altmtr_textbox = tk.Entry(entry_frame, background='dark gray', foreground='white', state='disabled',
                          disabledbackground='black', highlightthickness=0, font=('Terminal', 15))
altmtr_textbox.grid(row=4, column=5, pady=5, sticky='w')

#remarks... these will be populated based on data and entries in other screens
remarks_label = tk.Label(entry_frame, text="REMARKS", font=('Terminal', 15), background='black', foreground='white' )
remarks_label.grid(row=5, column=0, pady=5)
eq7 = tk.Label(entry_frame, text="=", background='black', foreground='white')
eq7.grid(row=5, column=1)
remarks_placeholder = tk.Label(entry_frame, text="AO2 SLPNO", font=('Terminal', 15), background='black', foreground='white' )
remarks_placeholder.grid(row=5, column=2, pady=5, sticky='w', columnspan=10)


#the following are placeholder labels for the prep report frame and the last report frames

report_prep_label = tk.Label(prep_report_frame, font=('Terminal', 15), text="METAR KSLC 010554 18008KT 1 1/2SM RA BR FEW045CB SCT090 BKN180 OVC260 08/M01 A2988 RMK AO2 SLPNO CB VC NE MOV N T00820012", background = 'gray25', foreground='white', pady=30, padx=10, wraplength=900, justify='left')
report_prep_label.grid(row=0, column = 0, sticky = 'w', ipadx = 10)
last_report_label = tk.Label(last_report_frame, font=('Terminal', 15), text="METAR KSLC 010654 17008KT 10SM FEW045 FEW090 SCT180 BKN260 07/00 A2988 RMK AO2 SLPNO T00741003", background='black', foreground='white', pady=30, padx=10, wraplength=900, justify='left')
last_report_label.grid(column=0, row=0, sticky='w', ipadx = 10)

#the following is the packing frames for the misc frame
centering_frame = tk.Frame(misc_frame, background='black')
centering_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=1)

#frames so that the labels and data line up how I want
wind_frame = tk.Frame(centering_frame, background = 'black')
wind_frame.grid(column=0, row=0, sticky='w')

relhum_frame = tk.Frame(centering_frame, background = 'black')
relhum_frame.grid(column=0, row=1, sticky='w')

slp_frame = tk.Frame(centering_frame, background = 'black')
slp_frame.grid(column=0, row=2, sticky='w')

station_pressure_frame = tk.Frame(centering_frame, background = 'black')
station_pressure_frame.grid(column=1, row=0, sticky='e')

pressure_altitude_frame = tk.Frame(centering_frame, background = 'black')
pressure_altitude_frame.grid(column=1, row=1, sticky='e')

density_altitude_frame = tk.Frame(centering_frame, background = 'black')
density_altitude_frame.grid(column=1, row=2, sticky='e')


#now the content to fill in those frames
mag_wind_label = tk.Label(wind_frame, text="MAG WIND: ", background='black', foreground='white', font=('Terminal', 15),
                          anchor='w', justify='left')
mag_wind_label.pack(side='left')
mag_wind_value = tk.Label(wind_frame, text="270/09G27", background='black', foreground='white', font=('Terminal', 15))
mag_wind_value.pack(side='left', fill='both')

station_pressure_value = tk.Label(station_pressure_frame, text="29.59", background='black', foreground='white',
                                  font=('Terminal', 15))
station_pressure_value.pack(side='right')
station_pressure_label = tk.Label(station_pressure_frame, text="STATION PRESSURE: ", background='black', foreground='white',
                                  font=('Terminal', 15))
station_pressure_label.pack(side='right')

relative_humidity_label = tk.Label(relhum_frame, text="RELATIVE HUMIDITY: ", background='black',
                                   foreground='white', font=('Terminal', 15))
relative_humidity_label.pack(side='left')
relative_humidity_value = tk.Label(relhum_frame, text="70%", background='black', foreground='white',
                                   font=('Terminal', 15))
relative_humidity_value.pack(side='left', fill='both')

pressure_altitude_value = tk.Label(pressure_altitude_frame, text="4221", background='black', foreground='white',
                                   font=('Terminal', 15))
pressure_altitude_value.pack(side='right')
pressure_altitude_label = tk.Label(pressure_altitude_frame, text="PRESSURE ALTITUDE: ", background='black',
                                   foreground='white', font=('Terminal', 15))
pressure_altitude_label.pack(side='right')

slp_label = tk.Label(slp_frame, text="SEA LEVEL PRESSURE: ", background='black', foreground='white', font=('Terminal', 15))
slp_label.pack(side='left')
slp_value = tk.Label(slp_frame, text="1020.25", background='black', foreground='white', font=('Terminal', 15))
slp_value.pack(side='left', fill='both')

density_altitude_value = tk.Label(density_altitude_frame, text="6070", background='black', foreground='white',
                                  font=('Terminal', 15))
density_altitude_value.pack(side='right')
density_altitude_label = tk.Label(density_altitude_frame, text="DENSITY ALTITUDE: ", background='black', foreground='white',
                                  font=('Terminal', 15))
density_altitude_label.pack(side='right')


keypad = tk.Frame(keypad_frame, background='black', highlightbackground='blue', highlightthickness=2)
keypad.grid(row=0, column=0, ipady=75, ipadx=75)
key_label_1 = tk.Label(keypad, text="SIGN", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_1.grid(row=2, column=0, sticky='nsew')
key_label_2 = tk.Label(keypad, text="EDIT", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_2.grid(row=2, column=1, sticky='nsew')
key_label_3 = tk.Label(keypad, text="AUX", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_3.grid(row=2, column=2, sticky='nsew')
key_label_4 = tk.Label(keypad, text="REVUE", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_4.grid(row=1, column=0, sticky='nsew')
key_label_5 = tk.Label(keypad, text="TWR", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_5.grid(row=1, column=1, sticky='nsew')
key_label_6 = tk.Label(keypad, text=" ", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_6.grid(row=1, column=2,  sticky='nsew')
key_label_7 = tk.Label(keypad, text="PRINT", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_7.grid(row=0, column=0, sticky='nsew')
key_label_8 = tk.Label(keypad, text="GENOB", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_8.grid(row=0, column=1, sticky='nsew')
key_label_9 = tk.Label(keypad, text="CMD", font=('Terminal', 15), background='black', highlightbackground='blue', highlightthickness=1, foreground='white')
key_label_9.grid(row=0, column=2, sticky='nsew')

keypad.grid_rowconfigure(0, weight=1)
keypad.grid_rowconfigure(1, weight=1)
keypad.grid_rowconfigure(2, weight=1)
keypad.grid_columnconfigure(0, weight=1)
keypad.grid_columnconfigure(1, weight=1)
keypad.grid_columnconfigure(2, weight=1)

current_oid_screen = "edit"
current_keypad = "edit"
revue_keypad = ("RPT", "SENSR", "DAILY", "MONTH", "LOGS", "SITE", "EXIT", " ", " ")
edit_keypad = ("SIGN", "EDIT", "AUX", "REVUE", "TWR", " ", "PRINT", "GENOB", "CMD" )



is_it_on = 0

def enable_entries():
    
    global is_it_on
    sky_textbox.config(state='normal')
    vis_textbox.config(state='normal')
    tempc_textbox.config(state='normal')
    tdc_textbox.config(state='normal')
    tempf_textbox.config(state='normal')
    tdf_textbox.config(state='normal')
    rvr_textbox.config(state='normal')
    wind_textbox.config(state='normal')
    wx_textbox.config(state='normal')
    altmtr_textbox.config(state='normal')
    is_it_on = 1
    print("I think it got enabled: " +  str(is_it_on))
    
def disable_entries():    
    
    global is_it_on
    entry_frame.focus()
    sky_textbox.config(state='disabled')
    vis_textbox.config(state='disabled')
    tempc_textbox.config(state='disabled')
    tdc_textbox.config(state='disabled')
    tempf_textbox.config(state='disabled')
    tdf_textbox.config(state='disabled')
    rvr_textbox.config(state='disabled')
    wind_textbox.config(state='disabled')
    wx_textbox.config(state='disabled')
    altmtr_textbox.config(state='disabled')
    is_it_on = 0
    print("I think it got disabled: " +  str(is_it_on))

def enable_or_disable(event):
    global current_oid_screen
    global is_it_on
    if current_oid_screen == "edit":
        if is_it_on == 0:
            enable_entries()
        elif is_it_on == 1:
            disable_entries()


window.bind('<F1>', enable_or_disable)

def celsius_to_fahrenheit(num):
    
    faht = round((num * (9.0/5.0)) + 32.0, 1)
    return faht
    
def fahrenheit_to_celsius(num):
    
    celt = round((5.0/9.0)*(num-32), 1)
    return celt
    

def show_temp_f_equivalent(event):
    
    tempf_textbox.delete(0, 'end')
    temp_c_input = float(tempc_textbox.get())
    tempf_textbox.insert(0, celsius_to_fahrenheit(temp_c_input)) 
    
def show_temp_c_equivalent(event):
    tempc_textbox.delete(0, 'end')
    temp_f_input = float(tempf_textbox.get())
    tempc_textbox.insert(0, fahrenheit_to_celsius(temp_f_input))
    
def show_td_f_equivalent(event):
    tdf_textbox.delete(0, 'end')
    tdc_input = float(tdc_textbox.get())
    tdf_textbox.insert(0, celsius_to_fahrenheit(tdc_input)) 
    
tempc_textbox.bind('<Return>', show_temp_f_equivalent)
tempf_textbox.bind('<Return>', show_temp_c_equivalent)
tdc_textbox.bind('<Return>', show_td_f_equivalent)
       





#def change_keypad(keypad_condition):
#        keypad_guide("RPT", "SENSR", "DAILY", "MONTH", "LOGS", "SITE", "EXIT", " ", " ")
#        print("key was pressed")
        
#window.bind('<F1>', change_keypad(keypad_setup))
    
#when starting up the system, this is the default keypad setup
#keypad_guide("SIGN", "EDIT", "AUX", "REVUE", "TWR", " ", "PRINT", "GENOB", "CMD" )
get_time()
window.mainloop()
