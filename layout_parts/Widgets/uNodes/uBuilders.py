from layout_parts.Widgets.uNodes.uTextBox import uTEXTBOX
from layout_parts.Widgets.uNodes.uTouchArea import uTOUCHAREA
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.unode_util.helperclasses import Task
from layout_parts.Widgets.uNodes.uControllerNodes import *
from notifier import NotifyService
import datetime



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



def CalendarEntrys(date : str, parentwidget):
    true_time = not parentwidget.settings["stretch_time"]
    earliest_time = get_weeks_earliest_and_latest_time()[0]
    latest_time = get_weeks_earliest_and_latest_time()[1]
    tasks_for_today : list = NotifyService.get("tasks.per_day")
    if not date in tasks_for_today.keys():
        return [uLABEL("Keine Tasks")]
    tasks = []
    for task in tasks_for_today[str(date)]:
        tasks.append(Task(
            key = task["key"],
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
        tasksitems.append(
            uTOUCHAREA(
            parentwidget=parentwidget,
            funcname="Task",
            args=[tasko],
            child = uCARD(
            thickness=3,
            flex = time_to_dec(t.endtime) - time_to_dec(t.time) if t.endtime != None else 1,
            filled = str(datetime.date.today()) == t.date and isInTime,
            rounding = 7,
            child = uCOLUMN(
                children = [uLABEL(text, highlight = (not isInTime or not str(datetime.date.today()) == t.date )) for text in t.title.split(" ")]
                )
            )
            )
        )
        tasksitems.append(uLABEL(t.endtime) if t.endtime != None else uEMPTY())
        last_time = time_to_dec(t.endtime) if t.endtime != None else last_time + 1
        last_task = t
    tasksitems.append(uEMPTY(flex = (latest_time - last_time - 1) if true_time else 0))
    return tasksitems

def buildSettingsEntrys(parentwidget, data : uCCSETTINGSdata, pagenumber):
    returnlist = [uEMPTY() for i in range(data.max_items_per_page)]
    for item in range(len(data.pagedata[pagenumber - 1])):
        words = data.pagedata[pagenumber - 1][item]["name"].split("_")
        labelname = ""
        for word in words:
            labelname = labelname + " " +  word.capitalize()


        returnlist[item] = uROW(
            children = [
                uLABEL(labelname),
                build_controller_for_setting(parentwidget, data = data.pagedata[pagenumber - 1][item])
            ]
        )
    parentwidget.notify("update")
    return returnlist

def build_controller_for_setting(parentwidget, data : dict):
    if data["type"] == "checkbox":
        return uCHECKBOX(
            level = 4,
            widget_to_notify=parentwidget,
            initial_status=data["value"],
            name="SETTING." + data["name"]
        )
    else:
        return uEMPTY()

def buildTaskCreationElements(taskdata : Task, parentwidget):
    returnwidget = uCOLUMN(
        flex = 4,
        divider_thickness=2,
        children = []
    )
    widgets = []
    widgets.append(uROW(
        children = [
        uLABEL("Date"),
        uPBOX(
            uTEXTBOX(funcname = "datePicker", parentwidget=parentwidget),
            modH = 90,
            modV = 80
            )]
    ))
    widgets.append(uROW(
        children = [
        uLABEL("(Start-) Time"),
        uPBOX(
            uTEXTBOX(funcname = "timePicker", parentwidget=parentwidget),
            modH = 90,
            modV = 80
            )]
    ))
    widgets.append(uROW(
        children = [
        uLABEL("(End-) Time"),
        uPBOX(
            uTEXTBOX(funcname = "endPicker", parentwidget=parentwidget),
            modH = 90,
            modV = 80
            )]
    ))
    widgets.append(uROW(
        children = [
        uLABEL("Description"),
        uPBOX(
            uTEXTBOX(funcname = "descriptionPicker", parentwidget=parentwidget),
            modH = 90,
            modV = 80
        )]
    ))
    widgets.append(uROW(
        children = [
        uLABEL("Tags"),
        uLABEL("N/I")]
    ))
    returnwidget.children = widgets
    return returnwidget


