#from typing import Dict, List
import json
import os

def jget(filename : str, setting_name : str):
    with open(str(os.path.dirname(os.path.abspath(__file__)))+ r"/" + filename + ".json", "r") as jfile:
        try:
            return json.loads(jfile.read())[setting_name]
        except:
            return None

def jdumpget(filename : str, settings):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
        try:
            output = {}
            data = json.loads(jfile.read())
            for key in settings():
                output[key] = data[key]
            return output
        except:
            return None

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
    print(path)
    with open(path + "/" + filename + ".json", "r") as jfile:
        directory : dict = json.loads(jfile.read())
        return directory.keys()

class NOTIFIER():
    def __init__(self):
        self.allowed_prefixes = ["user", "layout", "debug", "ram", "timing"]
        for key in get_all_keys(filename="usersettings"):
            setattr(self, "Listeners_user_" + key, [])
        for key in get_all_keys(filename="debugsettings"):
            setattr(self, "Listeners_debug_" + key, [])
        for key in get_all_keys(filename="ramdata"):
            setattr(self, "Listeners_ram_" + key, [])
        for key in get_all_keys(filename="timing"):
            setattr(self, "Listeners_timing_" + key, [])
        

    def get(self, name : str):
        if name.split(".")[0] not in self.allowed_prefixes:
            raise ValueError(name.split(".")[0] + " not in allowed prefixes")
        if name.split(".")[0] == "debug":
            return jget(filename="debugsettings", setting_name = name.split(".")[1])
        elif name.split(".")[0] == "user":
            return jget(filename="usersettings", setting_name = name.split(".")[1])
        elif name.split(".")[0] == "ram":
            return jget(filename="ramdata", setting_name=name.split(".")[1])
        elif name.split(".") == "layout":
            return jget(filename="layouts", setting_name=self.get("ram.currently_loaded_layout"))["settings"][name.split(".")[1]]
        elif name.split(".") == "timing":
            return jget(filename="timing", setting_name=name.split(".")[1])
        
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

    def dumpchange(self, changes : dict):
        prefixes = []
        for key in changes.keys():
            prefix = key.split(".")[0]
            prefixes.append(prefix)
            suffix = key.split(".")[1]
            value = changes[key]
            changes.pop(key)
            changes[suffix] == value
            if prefix not in self.allowed_prefixes:
                raise ValueError(prefix + " not in allowed prefixes.")
            for listener in getattr(self, "Listeners_" + prefix + "_" + suffix):
                listener.notify(key, changes[key])
        if not prefixes.count(prefixes[0]) == len(prefixes):
            raise ValueError("All prefixes in dumpchange need to be the same.")
        else:
            if prefixes[0] == "user":
                jdumpset("usersettings", changes)

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


global NotifyService
NotifyService : NOTIFIER = NOTIFIER()

