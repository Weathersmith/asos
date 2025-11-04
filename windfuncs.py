# a module that contains all wind calculations for use in the asos.py module (main)

#wind direction, per ASOS User Guide pg 14
# a 2-minute average of 5-second wind averages every minute (i.e. 24 samples each minute)
#reported to the nearest 10 degrees, reported relative to true north for the METAR

def five_second_wind_average(one_second_wind_directions):
    
    return (sum(one_second_wind_directions) / 5)

def two_minute_wind_average(five_second_wind_average):
    
    two_minute_average = 0
    two_minute_directions = []
    if len(two_minute_directions) < 24:
        two_minute_directions.append(five_second_wind_average)
    elif len(two_minute_directions) == 24:
        two_minute_average = sum(two_minute_directions)/24
        del two_minute_directions[0:12] #clears list of the oldest minute of obs
        return two_minute_average
    else:
        print("there are negative or over 24 items in the list")




    