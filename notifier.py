from typing import Dict
import json
import os

def jget(filename : str, setting_name : str):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + + rf"\{filename}.json", "r") as jfile:
        try:
            return json.loads(jfile.read())[setting_name]
        except:
            return None

def jdumpget(filename : str, settings):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "r") as jfile:
        try:
            output = {}
            data = json.loads(jfile.read())
            for key in settings():
                output[key] = data[key]
            return output
        except:
            return None

def jset(filename : str, setting_name : str, setting_value):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "r") as jfile:
        directory = json.loads(jfile.read())
        directory[setting_name] = setting_value
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "w") as jfile:
        json.dump(directory, jfile)

def jdumpset(filename : str, settings):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "r") as jfile:
        directory = json.loads(jfile.read())
        for setting in settings.keys():
            directory[setting] = settings[setting]
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "w") as jfile:
        json.dump(directory, jfile)

def get_all_keys(filename : str):
    with open(str(os.path.dirname(os.path.abspath(__file__))) + rf"\{filename}.json", "r") as jfile:
        directory : Dict = json.loads(jfile.read())
        return directory.keys()

class NOTIFIER():
    def __init__(self):
        for key in get_all_keys(filename="usersettings"):
            setattr(self, "Listeners_user_" + key, [])
        
    def change(self, name : str, value):
        prefix = name.split(".")[0]
        suffix = name.split(".")[1]
        allowed_prefixes = ["user", "layout"]
        if prefix not in allowed_prefixes:
            raise ValueError(prefix + " not in allowed prefixes.")
        for listener in getattr(self, "Listeners_" + prefix + "_" + suffix):
            listener.notify(name, )
        