import datetime
from notifier import NotifyService

def get_weeks_earliest_and_latest_time():
    current_date = datetime.date.today()
    current_weekday = datetime.date.today().weekday()
    weeks_dates = []
    for weekday in range(7):
        if weekday < current_weekday:
            weeks_dates.append(str(current_date - datetime.timedelta(days = current_weekday - weekday)))
        elif weekday == current_weekday:
            weeks_dates.append(str(current_date))
        else:
            weeks_dates.append(str(current_date + datetime.timedelta(days = weekday - current_weekday)))
    tasks = NotifyService.get("tasks.per_day")
    this_week_tasks = []
    if weeks_dates[0] in tasks.keys():
        for task in tasks[weeks_dates[0]]:
            this_week_tasks.append(task)
    if weeks_dates[1] in tasks.keys():
        for task in tasks[weeks_dates[1]]:
            this_week_tasks.append(task)
    if weeks_dates[2] in tasks.keys():
        for task in tasks[weeks_dates[2]]:
            this_week_tasks.append(task)
    if weeks_dates[3] in tasks.keys():
        for task in tasks[weeks_dates[3]]:
            this_week_tasks.append(task)
    if weeks_dates[4] in tasks.keys():
        for task in tasks[weeks_dates[4]]:
            this_week_tasks.append(task)
    if weeks_dates[5] in tasks.keys():
        for task in tasks[weeks_dates[5]]:
            this_week_tasks.append(task)
    if weeks_dates[6] in tasks.keys():
        for task in tasks[weeks_dates[6]]:
            this_week_tasks.append(task)
    earliest_time = 24
    latest_time = 0
    for task in this_week_tasks:
        if "time" in task.keys() and time_to_dec(task["time"]) < earliest_time:
            earliest_time = time_to_dec(task["time"])
        if "endtime" in task.keys() and time_to_dec(task["endtime"]) > latest_time:
            latest_time = time_to_dec(task["endtime"])
    return [earliest_time - 2, latest_time + 2]

def get_date_based_on_weekday(assigned_weekday):
    current_date = datetime.date.today()
    current_weekday = current_date.weekday()
    if assigned_weekday == current_weekday:
        return str(current_date)
    elif assigned_weekday > current_weekday:
        return str(current_date + datetime.timedelta(days = assigned_weekday - current_weekday))
    else:
        return str(current_date - datetime.timedelta(days = current_weekday - assigned_weekday))

def time_to_dec(timestring):
    hour = int(timestring.split(":")[0])
    minute = int(timestring.split(":")[1])
    timefloat : float = hour
    timefloat += minute / 60
    return timefloat

