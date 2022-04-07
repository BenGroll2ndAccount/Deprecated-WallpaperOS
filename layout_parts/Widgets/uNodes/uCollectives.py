
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

def time_to_dec(timestring):
    hour = int(timestring.split(":")[0])
    minute = int(timestring.split(":")[1])
    timefloat : float = hour
    timefloat += minute / 60
    return timefloat

def CalendarEntrys(date, truetime : bool = True):
    earliest_time = "7:00"
    tasks_for_today : list = NotifyService.get("tasks.per_day")
    tasks = []
    for task in tasks_for_today[date]:
        tasks.append(Task(
            date = task["date"],
            time = task["time"],
            endtime = task["endtime"],
            category=task["category"],
            title = task["title"],
            description= task["description"]
        ))
    last_time = time_to_dec(earliest_time) - 1
    tasksitems = []
    for tasko in tasks:
        t : Task = tasko
        if t.time == None and t.date != None:
            tasksitems.append(uLABEL(t.title))
            last_time += 1
        time_now = datetime.datetime.now()
        timenowstring = str(time_now.hour) + ":" + str(time_now.minute)
        in_time = time_to_dec(timenowstring) > time_to_dec(t.time) and (time_to_dec(timenowstring) < time_to_dec(t.endtime) if t.endtime != None else True)
        tasksitems.append(uEMPTY(flex = time_to_dec(t.time) - last_time - 2))
        tasksitems.append(uLABEL(str(time_to_dec(t.time) - last_time - 2)))
        tasksitems.append(uLABEL(str(time_to_dec(t.endtime) - time_to_dec(t.time) if t.endtime != None else 1)))
        tasksitems.append(uLABEL(t.time))
        tasksitems.append(uCARD(
            thickness=3,
            flex = time_to_dec(t.endtime) - time_to_dec(t.time) if t.endtime != None else 1,
            filled = datetime.date.today() == t.date and in_time,
            rounding = 7,
            child = uCOLUMN(
                children = [uLABEL(text) for text in t.title.split(" ")]
            )
            )
        )
        tasksitems.append(uLABEL(t.endtime) if t.endtime != None else uEMPTY())
        last_time = t.endtime if t.endtime != None else last_time + 1
    return tasksitems

