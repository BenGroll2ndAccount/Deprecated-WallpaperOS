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


class uTASKCREATIONPANEL(uPOPUP):
    @tlog
    def __init__(self, parentwidget, tasktitle : str):
        self.parentwidget = parentwidget
        self.body = BODIES.AddNewTaskPopupPanel(self, parentwidget = self, taskdata = Task(title = tasktitle))
        self.__node_init__(listening=[], level = 0)
        self.hasSomethingChanged = False
        NotifyService.subscribeIfTouchedOutSide(self)

    def updatebody(self):
        self.body = BODIES.AddNewTaskPopupPanel(parentwidget = self)
        self.body.constrainmod(self.constraint)
        NotifyService.register_event("redraw", self.parentwidget.widgetname)

    def saveDataToFile(self):
        raise NotImplementedError


    def notify(self, string:str):
        raise NotImplementedError
