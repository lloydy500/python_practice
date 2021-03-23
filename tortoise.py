import math

def race(v1, v2, g):
    # your code
    if v1 >= v2:
        return None   
    hours_exact = g / (v2 - v1)
    hours_show = int(hours_exact)
    minutes_exact = (hours_exact - hours_show) * 60
    minutes_show = int(minutes_exact)
    seconds_exact = (minutes_exact - minutes_show) * 60
    seconds_show = int(seconds_exact)

    return [hours_show, minutes_show, seconds_show]

print(race(720, 850, 70))
