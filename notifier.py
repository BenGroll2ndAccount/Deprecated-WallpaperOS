#from typing import Dict, List
import json
import os

def jget(filename : str, setting_name : str):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + + r"/" + filename + ".json", "r") as jfile:
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
        self.allowed_prefixes = ["user", "layout"]
        for key in get_all_keys(filename="usersettings"):
            setattr(self, "Listeners_user_" + key, [])
        
    def change(self, name : str, value):
        prefix = name.split(".")[0]
        suffix = name.split(".")[1]
        if prefix not in self.allowed_prefixes:
            raise ValueError(prefix + " not in allowed prefixes.")
        for listener in getattr(self, "Listeners_" + prefix + "_" + suffix):
            listener.notify(name, value)
        if prefix == "user":
            jset("usersettings", name, value)

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
        listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name)
        for listener in listeners:
            listening.append(listener)
    
    def removeListeners(self, name:str, removers : list):
        listening : list = getattr(self, "Listeners_" + name.split(".")[0] + "_" + name)
        for listener in removers:
            listening.remove(removers)


global NotifyService
NotifyService = None

def _initialize_notifier_():
    global NotifyService
    NotifyService = NOTIFIER