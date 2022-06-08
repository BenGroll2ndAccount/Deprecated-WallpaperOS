from re import U
from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.helperclasses import Task
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *


class uTOUCHAREA(uNODE):
    def __init__(self, child : uNODE = None, level : int = 0, flex = 1, parentwidget = None, funcname : str = "", args = None, kwargs = None):
        self.flex = flex
        self.child = child
        self.parentwidget = parentwidget
        self.onlyOnPress = (funcname, args, kwargs)
        NotifyService.subscribe_to_event(self, "touching")
        self.__node_init__(listening=[], level = level)

    @tlog
    def notify_Touched(self):
        if self.onlyOnPress[0] == "Task":
            self.parentwidget.notify_OpenTask(self.onlyOnPress[1][0])
        if self.onlyOnPress[0] == "CCenter":
            if self.parentwidget.controlcenter == None:
                self.parentwidget.notify_OpenCCenter()
            else:
                self.parentwidget.notify_CloseCCenter()
        if self.onlyOnPress[0] == "Header":
            self.parentwidget.notify_Touched()
        if self.onlyOnPress[0] == "CCenterOpenSettings":
            self.parentwidget.notify_CCenterOpenSettings()
        if self.onlyOnPress[0] == "SETTINGS.DISCARD":
            self.parentwidget.parentwidget.notify_DiscardPopup()
        if self.onlyOnPress[0].startswith("SETTINGS."):
            getattr(self.parentwidget, "notify_" + self.onlyOnPress[0].split(".")[1])()
        if self.onlyOnPress[0].startswith("SETTING."):
            self.parentwidget.notify_Setting('%s' % self.onlyOnPress[0].split(".")[1], self.onlyOnPress[0].split(".")[2])
        if self.onlyOnPress[0].startswith("CCenterNewTask"):
            self.parentwidget.notify_CCenterNewTask()
        if self.onlyOnPress[0] == "TextBoxClicked":
            self.parentwidget.notify_TextBox()
        if self.onlyOnPress[0] == "NameSubmitted.Flip":
            self.parentwidget.notify_NameSubmitted()

    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.child != None:
            self.child.constrainmod(self.constraint.copy)
        else:
            return 0

    @tlog
    def affected_by_touch(self, point : uPoint):
        return point.isInArea(self.constraint.copy)

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw-touch-areas"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_touch_debug = True))
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls
