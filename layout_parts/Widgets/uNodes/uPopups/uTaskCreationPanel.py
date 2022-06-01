from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from notifier import NotifyService
from layout_parts.Widgets.uNodes.uPopups.uPopup import uPOPUP
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import *
from layout_parts.Widgets.bodies import BODIES
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *


class uTASKCREATIONPANEL(uPOPUP):
    @tlog
    def __init__(self, parentwidget, tasktitle : str):
        self.parentwidget = parentwidget
        self.taskdata = Task(title = tasktitle)
        self.body = BODIES.AddNewTaskPopupPanel(self, parentwidget = self, taskdata = Task(title = tasktitle))
        self.__node_init__(listening=[], level = 0)
        self.hasSomethingChanged = False
        NotifyService.subscribeIfTouchedOutSide(self)

    def updatebody(self):
        self.body = BODIES.AddNewTaskPopupPanel(parentwidget = self, taskdata=self.taskdata)
        self.body.constrainmod(self.constraint)
        NotifyService.register_event("redraw", self.parentwidget.widgetname)

    def saveDataToFile(self):
        raise NotImplementedError

    @n
    def notify_TextBox(self, name, value):
        print(name)


