import datetime
def time_to_dec(timestring):
    hour = int(timestring.split(":")[0])
    minute = int(timestring.split(":")[1])
    timefloat : float = hour
    timefloat += minute / 60
    return timefloat

def get_date_based_on_weekday(current_date, assigned_weekday):
    current_date = datetime.date.today()
    current_weekday = current_date.weekday()
    if assigned_weekday == current_weekday:
        return current_date
    elif assigned_weekday > current_weekday:
        return current_date + datetime.timedelta(days = assigned_weekday - current_weekday)
    else:
        return current_date - datetime.timedelta(days = current_weekday - assigned_weekday)

