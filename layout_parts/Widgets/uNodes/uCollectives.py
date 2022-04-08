from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uCard import uCARD
from notifier import NotifyService
import datetime

class Task():
    def __init__(self, title : str, date : str = None, time : str = None, endtime : str = None, category : str = None, description : str = None):
        self.date = date
        self.time = time
        self.category = category
        self.title = title
        self.description = description
        self.endtime = endtime


def cCALENDAR_COLUMN_TIME_MARKER(weekday : int = None):
    weekday_real = NotifyService.get("timing.weekday")
    if weekday_real == weekday:
        return uCOLUMN(
            children=[
                uEMPTY()
            ]
        )
    else:
        return uEMPTY(flex = 0)



def CalendarEntrys(date : str, settings):
    print(settings)
    true_time = settings["true-time"]
    earliest_time = get_weeks_earliest_and_latest_time()[0]
    latest_time = get_weeks_earliest_and_latest_time()[1]
    tasks_for_today : list = NotifyService.get("tasks.per_day")
    if not date in tasks_for_today.keys():
        return [uLABEL("Keine Tasks")]
    tasks = []
    for task in tasks_for_today[str(date)]:
        tasks.append(Task(
            date = task["date"],
            time = task["time"],
            endtime = task["endtime"],
            category=task["category"],
            title = task["title"],
            description= task["description"]
        ))
    if len(tasks) == 0:
        return [uLABEL("Keine Tasks")]
    last_time = earliest_time + 1
    tasksitems = []
    last_task = None
    for tasko in tasks:
        t : Task = tasko
        if t.time == None and t.date != None:
            tasksitems.append(uLABEL(t.title))
            last_time += 1
        time_now = datetime.datetime.now()
        timenowstring = str(time_now.hour) + ":" + str(time_now.minute)
        isInTime = False
        if t.time != None:
            if t.endtime != None:
                isInTime = time_to_dec(t.time) < time_to_dec(timenowstring) and time_to_dec(t.endtime) > time_to_dec(timenowstring)
            else:
                isInTime = time_to_dec(t.time) < time_to_dec(timenowstring)
        if last_task != None:
            if t.time == last_task.endtime:
                tasksitems.append(uEMPTY(flex = (time_to_dec(t.time) - last_time) if true_time else 0))
            else:
                tasksitems.append(uEMPTY(flex = (time_to_dec(t.time) - last_time) if true_time else 0)) 
                tasksitems.append(uLABEL(t.time))
        else:
            tasksitems.append(uEMPTY(flex = (time_to_dec(t.time) - last_time) if true_time else 0 ))
            tasksitems.append(uLABEL(t.time))
        tasksitems.append(uCARD(
            thickness=3,
            flex = time_to_dec(t.endtime) - time_to_dec(t.time) if t.endtime != None else 1,
            filled = str(datetime.date.today()) == t.date and isInTime,
            rounding = 7,
            child = uCOLUMN(
                children = [uLABEL(text, highlight = (not isInTime or not str(datetime.date.today()) == t.date )) for text in t.title.split(" ")]
            )
        )
    )
        tasksitems.append(uLABEL(t.endtime) if t.endtime != None else uEMPTY())
        last_time = time_to_dec(t.endtime) if t.endtime != None else last_time + 1
        last_task = t
    tasksitems.append(uEMPTY(flex = (latest_time - last_time - 1) if true_time else 0))
    return tasksitems
