import math

def make_readable(seconds):

    #make variables for hours, minutes seconds by dividing by 
    #divide by 60**2 to get and take the 'floor' integer
    #take the remainder and times by 60 to get take the floor to get mins
    #take the remainder of that and round for seconds

    hours_exact = seconds / (60 ** 2)
    hours_show = math.floor(seconds / (60 ** 2))
    minutes_exact = (hours_exact - hours_show) * 60
    minutes_show = math.floor((hours_exact - hours_show) * 60)
    seconds_exact = (minutes_exact - minutes_show) * 60
    seconds_show = round(seconds_exact)

    return "{:02}:{:02}:{:02}".format(hours_show, minutes_show, seconds_show)

print(make_readable(45500))