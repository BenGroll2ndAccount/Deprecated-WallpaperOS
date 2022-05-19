#from typing import Dict, List
import json
import os
from layout_parts.Widgets.uNodes.unode_util.helperclasses import uPoint

def jget(filename : str, setting_name : str):
    with open(str(os.path.dirname(os.path.abspath(__file__)))+ r"/" + filename + ".json", "r") as jfile:
        try:
            return json.loads(jfile.read())[setting_name]
        except:
            return None

def jdumpget(filename : str, settings):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
        output = {}
        data = json.loads(jfile.read())
        for key in settings:
            output[key] = data[key]
        return output
        
def jset(filename : str, setting_name : str, setting_value):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
        directory = json.loads(jfile.read())
        directory[setting_name] = setting_value
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "w") as jfile:
        json.dump(directory, jfile)

def jdumpset(filename : str, settings):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
        directory = json.loads(jfile.read())
        for setting in settings.keys():
            directory[setting] = settings[setting]
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "w") as jfile:
        json.dump(directory, jfile)

def get_all_keys(filename : str):
    path = str(os.path.dirname(os.path.abspath(__file__)))
    with open(path + "/" + filename + ".json", "r") as jfile:
        directory : dict = json.loads(jfile.read())
        return directory.keys()

class NOTIFIER():
    def __init__(self):
        self.allowed_prefixes = ["user", "layout", "debug", "ram", "timing", "tasks", "event"]
        self.all_filenames_for_cache = ["usersettings", "debugsettings", "ramdata", "timing", "tasks", "event"]
        self.loadcache(self.all_filenames_for_cache)

    def reloadcache(self):
        self.loadcache(self.all_filenames_for_cache)

    def loadcache(self, filenames):
        #Usersettings
        if "usersettings" in filenames:
            usersettings_keys = get_all_keys(filename="usersettings")
            usersettings_data = jdumpget(filename="usersettings", settings = usersettings_keys)
            for key in usersettings_data:
                setattr(self, "user."+key, usersettings_data[key])
                setattr(self, "Listeners_user_" + key, [])
        #Debugsettings
        if "debugsettings" in filenames:
            debug_keys = get_all_keys(filename="debugsettings")
            debug_data = jdumpget(filename="debugsettings", settings = debug_keys)
            for key in debug_data:
                setattr(self, "debug."+key, debug_data[key])
                setattr(self, "Listeners_debug_" + key, [])
        if "ramdata" in filenames:
        #Ramdata
            ram_keys = get_all_keys(filename="ramdata")
            ram_data = jdumpget(filename="ramdata", settings = ram_keys)
            for key in ram_data:
                setattr(self, "ram."+key, ram_data[key])
                setattr(self, "Listeners_ram_" + key, [])
        #Timing
        if "timing" in filenames:
            timing_keys = get_all_keys(filename="timing")
            timing_data = jdumpget(filename="timing", settings = timing_keys)
            for key in timing_data:
                setattr(self, "timing."+key, timing_data[key])  
                setattr(self, "Listeners_timing_" + key, [])    
        if "tasks" in filenames:
            tasks = jget("schedule", setting_name="tasks")
            schedule = {}
            for task in tasks:
                date = task["date"]
                if date in schedule.keys():
                    day : list = schedule[date]
                    day.append(task)
                    schedule[date] = day
                else:
                    schedule[date] = [task]
            setattr(self, "tasks.per_day", schedule)  
            setattr(self, "Listeners_tasks.per_day", [])
 
        if "event" in filenames:
            available_events = ["touching", "redraw", "reload_layout"]
            for event in available_events:
                setattr(self, "Subscribers_" + event, [])

    def trigger_layout_reload(self):
        self.Subscribers_reload_layout[0].notify("reload_layout")

    def register_event(self, name : str, *args):
        listeners = getattr(self, "Subscribers_" + name)
        if name == "touching":
            print("----------------")
            affected_listeners = []
            for listener in listeners:
                touchpoint : uPoint = uPoint(x = args[0][0], y = args[0][1])
                if listener.affected_by_touch(point=touchpoint):
                    affected_listeners.append(listener)
            if len(affected_listeners) > 0:
                highest_level_listener = affected_listeners[0]
                for listener in affected_listeners:
                    if listener.level > highest_level_listener.level:
                        highest_level_listener = listener
                highest_level_listener.notify("event." + name)
            
        if name == "redraw":
            for listener in listeners:
                listener.notify("event." + name, *args)


    def subscribe_to_event(self, subscriber, eventname):
        slist = getattr(self, "Subscribers_" + eventname)
        slist.append(subscriber)
        setattr(self, "Subscribers_" + eventname, slist)

    def get(self, name : str):
        if name.split(".")[0] in self.allowed_prefixes:
            return getattr(self, name)
        else:
            raise ValueError(name + " not in allowed prefixes.")
        
    def change(self, name : str, value):
        prefix = name.split(".")[0]
        suffix = name.split(".")[1]
        if prefix not in self.allowed_prefixes:
            raise ValueError(prefix + " not in allowed prefixes.")
        for listener in getattr(self, "Listeners_" + prefix + "_" + suffix):
            listener.notify(name, value)
        if prefix == "user":
            jset("usersettings", name, value)
        if name == "ramdata.widget_request_redraw":
            self.os.draw()
            jset("ramdata", "widget_request_redraw", False)
        setattr(self, name, value)

    def dumpchange(self, filename, changes : dict):
        jdumpset(filename, changes)
        self.loadcache(filenames=[filename])

    def addListeners(self, name : str, listeners : list):
        listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name.split(".")[1])
        for listener in listeners:
            listening.append(listener)
    
    def removeListeners(self, name:str, removers : list):
        listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name.split(".")[1])
        for listener in removers:
            listening.remove(removers)

    def addListener(self, listener, names : list):
        for name in names:
            listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name.split(".")[1])
            listening.append(listener)

    def removeListener(self, listener, names : list):
        for name in names:
            listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name.split(".")[1])
            listening.remove(listener)

    @property
    def layoutdata(self):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/layouts.json", "r") as jfile:
            layoutdata = json.loads(jfile.read())[self.get("ram.currently_loaded_layout")]
        return layoutdata

    @property
    def defaultwidgetsettings(self):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/widgetsettingsdefault.json", "r") as jfile:
            settings = json.loads(jfile.read())
        return settings
    
    def writeNewWidgetSettings(self, widgetname, settingsdict):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/layouts.json", "r") as jfile:
            file = json.loads(jfile.read())
        file[self.get("ram.currently_loaded_layout")]["widget-cluster-map"][widgetname]["parameters"]["settings"] = settingsdict
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/layouts.json", "w") as jfile:
            json.dump(file, jfile)

global NotifyService
NotifyService : NOTIFIER = NOTIFIER()

