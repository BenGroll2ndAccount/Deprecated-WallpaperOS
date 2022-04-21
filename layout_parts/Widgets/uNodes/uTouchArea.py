from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.helperclasses import Task

class uTOUCHAREA(uNODE):
    @tlog
    def __init__(self, child : uNODE = None, level : int = 0, flex = 1, parentwidget = None, funcname : str = "", args = None, kwargs = None):
        self.flex = flex
        self.child = child
        self.parentwidget = parentwidget
        self.onPress = (funcname, args, kwargs)
        NotifyService.subscribe_to_event(self, "touching")
        self.__node_init__(listening=[], level = level)

    @tlog
    def notify(self, name, *args, **kwargs):
        if name == "event.touching":
            if self.onPress[0] == "Task":
                self.parentwidget.notify("touched.Task", self.onPress[1][0])
            if self.onPress[0] == "CCenter":
                self.parentwidget.notify("touched.CCenter", None)
    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.child != None:
            self.child.constrainmod(self.constraint.copy)
        else:
            return 0

    @tlog
    def affected_by_touch(self, point):
        return point.isInArea(self.constraint.copy)

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw-touch-areas"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_touch_debug = True))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls
