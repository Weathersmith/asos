#the following is for allowing a user to log in and input some required info
#info includes station name and elevation
#the initial login is for an admin. As long as the system is not closed out, unique users can log in and out
#initial functionality will be started here and implemented into main at a later time
#this will be handled in command line

print("Welcome to the ASOS")
settings_configured = False

valid_user_creds = {"CWO": 'WEATHER', "AMOC": 'somethingbroke', "METOC": 'GetItDone'}

while settings_configured == False:
    user = input("username: ")
    password_good = False
    if user in valid_user_creds:
        while password_good == False:
            password = input("password: ")
            if valid_user_creds[user] == password:
                password_good = True
        location = input("Station name: ")
        icao = input("Station ICAO: ")
        elevation = input("Station Elevation (number and unit): ")
        print("This display will be for " + location + " with the identifier " + icao + " at an elevation of " + elevation + ".")
        settings_configured = True

    




"""
if user in valid_user_creds:
    password = input("password: ")
    if valid_user_creds[user] == password:
        location = input("Station name: ")
        icao = input("Station ICAO: ")
        elevation = input("Station Elevation (number and unit): ")
        print("This display will be for " + location + " with the identifier " + icao + " at an elevation of " + elevation + ".")
        is_correct = input("Is this correct? (Y or N) ")

    elif not valid_user_creds[user] == password:
        print("invalid password")
elif user not in valid_user_creds:
    print("invalid user name")
"""