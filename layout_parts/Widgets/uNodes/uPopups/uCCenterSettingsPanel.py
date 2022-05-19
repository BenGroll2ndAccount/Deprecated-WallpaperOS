from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from notifier import NotifyService
from layout_parts.Widgets.uNodes.uPopups.uPopup import uPOPUP
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.bodies import BODIES
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
import json


class uCCSETTINGS(uPOPUP):
    @tlog
    def __init__(self, parentwidget):
        self.parentwidget = parentwidget
        self.body = uEMPTY()
        self.__node_init__(listening=[], level = 0)
        self.hasSomethingChanged = False
        
    def load_data(self):
        widgetdata = NotifyService.layoutdata["widget-cluster-map"][self.parentwidget.widgetname]["parameters"]["settings"]
        defaults = NotifyService.defaultwidgetsettings[self.parentwidget.widgetname.split("_")[0]]
        final_settings_data = {}
        for defaultkey in defaults.keys():
            if defaults[defaultkey]["access"] == "page":
                if defaultkey in widgetdata.keys():
                    final_settings_data[defaultkey] = {"type" : defaults[defaultkey]["type"], "value" : widgetdata[defaultkey], "name" : defaultkey}
                else:
                    final_settings_data[defaultkey] = {"type" : defaults[defaultkey]["type"], "value" : defaults[defaultkey]["value"], "name" : defaultkey}
        #Pagination
        total_settings = len(final_settings_data.keys())
        vertical_clusters = self.constraint.height / NotifyService.get("debug.display-cluster_resolution")
        settings_per_page = int(vertical_clusters) - 1
        pages_required = int(total_settings / settings_per_page)
        if pages_required < (total_settings / settings_per_page):
            pages_required += 1
        self.total_pages = pages_required
        pages = []
        keys = []
        total_idx = 0
        for key in final_settings_data.keys():
            keys.append(key)
        for page in range(pages_required):
            pagedata = []
            for single in range(settings_per_page):
                if not total_idx >= len(keys):
                    pagedata.append(final_settings_data[keys[page + single]])
                    total_idx += 1
            pages.append(pagedata)
        self.data = uCCSETTINGSdata(current_page=1, maxpages = pages_required, max_items_per_page=settings_per_page, pagedata = pages)
        self.notify("init")

    def updatebody(self):
        self.body = BODIES.ControlCenterSettingsPanel(self, data=self.data)
        self.body.constrainmod(self.constraint)
        NotifyService.register_event("redraw", self.parentwidget.widgetname)

    def saveDataToFile(self):
        returndict = {}
        for page in self.data.pagedata:
            for entry in page:
                returndict[entry["name"]] = entry["value"]
        layoutdata = NotifyService.layoutdata
        layoutdata["widget-cluster-map"][self.parentwidget.widgetname]["parameters"]["settings"] = returndict
        NotifyService.writeNewWidgetSettings(self.parentwidget.widgetname, returndict)


    def notify(self, string:str):
        origstring = string
        string = '%s' % string  
        print("@Begin notify @CCenterSettings : " + string)
        if string.startswith("SETTING."):
            self.hasSomethingChanged = True
            string = string.split(".")
            name = string[1]
            operation = string[2]
            olddata = self.data.copy
            #print(olddata.pagedata)
            #print(name)
            correct_pageidx = 0
            correct_settingidx = 0
            for pageidx in range(len(olddata.pagedata)):
                for settingidx in range(len(olddata.pagedata[pageidx])):
                    if olddata.pagedata[pageidx][settingidx]["name"] == name:
                        correct_pageidx = pageidx
                        correct_settingidx = settingidx
            if operation == "Flip":
                olddata.pagedata[correct_pageidx][correct_settingidx]["value"] = not olddata.pagedata[correct_pageidx][correct_settingidx]["value"]
            self.data = olddata.copy
            #Body Update
        if origstring.startswith("SETTING.") or origstring == "init":
            self.updatebody()

        if origstring.startswith("SETTINGS."):
            command = origstring.split(".")[1]
            if command == "PAGEFWD":
                if self.data.current_page < self.data.maxpages:
                    self.data.current_page = self.data.current_page + 1
                    print(self.data)
                    print("HALLO")
                    self.updatebody()
            if command == "PAGEBWD":
                if self.data.current_page > 0:
                    self.data.current_page = self.data.current_page - 1
                    print(self.data)
                    self.updatebody()
            if command == "SAVE":
                if self.hasSomethingChanged:
                    self.saveDataToFile()
                    self.parentwidget.notify("touched.POPUP.DISCARD", None) 

