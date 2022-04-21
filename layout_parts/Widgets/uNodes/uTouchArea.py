from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.helperclasses import Task

class uTOUCHAREA(uNODE):
    @tlog
    def __init__(self, child : uNODE = None, level : int = 0, flex = 1, funcname : str = "", args = None, kwargs = None):
        self.flex = flex
        self.child = child
        self.onPress = (funcname, args, kwargs)
        NotifyService.subscribe_to_event(self, "touching")
        self.__node_init__(listening=[], level = level)

    @tlog
    def notify(self, name, values):
        print(self.constraint.out())
        if name == "event.touching":
            fakepoint = uPoint(values[0], values[1])
            if fakepoint.isInArea(self.constraint.copy):
                self.getPressFunction(self.onPress[0], self.onPress[1], self.onPress[2])
    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.child != None:
            self.child.constrainmod(self.constraint.copy)
        else:
            return 0

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_touch_debug = True))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls

    @tlog
    def getPressFunction(self, funcname, *args, **kwargs):
        getattr(uTouchAreaFunctions, "onPress_" + funcname)(*args, *kwargs)
    
class uTouchAreaFunctions():
    def onPress_Task(self, *args, **kwargs):
        print("Touched")