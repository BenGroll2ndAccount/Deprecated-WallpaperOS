def time_to_dec(timestring):
    hour = int(timestring.split(":")[0])
    minute = int(timestring.split(":")[1])
    timefloat : float = hour
    timefloat += minute / 60
    return timefloat

print(time_to_dec("17:30"))