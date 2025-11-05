# a module that contains all wind calculations for use in the asos.py module (main)

#wind direction, per ASOS User Guide pg 14
# a 2-minute average of 5-second wind averages every minute (i.e. 24 samples each minute)
#reported to the nearest 10 degrees, reported relative to true north for the METAR

def five_second_wind_dir_average(one_second_wind_directions): #assumes a list, 5 in length, is passed in
    
    return (sum(one_second_wind_directions) / 5)

def five_second_wind_speed_average(one_second_wind_speed): #assumes a list, 5 in length, is passed in

    return (sum(one_second_wind_speed)/ 5)

def two_minute_wind_average(five_second_wind_dir_average, five_second_wind_spd_average):
    
    wind_dir_and_speed = []
    two_minute_dir_avg = 0
    two_minute_directions = []
    if len(two_minute_directions) < 24:
        two_minute_directions.append(five_second_wind_dir_average)
    elif len(two_minute_directions) == 24:
        two_minute_dir_avg = sum(two_minute_directions)/24
        del two_minute_directions[0:12] #clears list of the oldest minute of obs
        wind_dir_and_speed[0] = two_minute_dir_avg
    else:
        print("there are negative numbers or over 24 items in the list")

    two_minute_spd_avg = 0
    two_minute_speeds = []
    if len(two_minute_speeds) < 24:
        two_minute_speeds.append(five_second_wind_spd_average)
    elif len(two_minute_speeds) == 24:
        two_minute_spd_avg = sum(two_minute_speeds)/24
        del two_minute_speeds[0] #clears oldest wind speed so it can be updated in five seconds
        wind_dir_and_speed[1] = two_minute_spd_avg
    else:
        print("there are negative numbers or over 24 items in the speed list")

    return wind_dir_and_speed

