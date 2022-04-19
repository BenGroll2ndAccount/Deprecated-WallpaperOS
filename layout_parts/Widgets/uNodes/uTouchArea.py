from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog

class uTOUCHAREA(uNODE):
    @tlog
    def __init__(self, child : uNODE = None, level : int = 0, flex = 1, identifier : str = ""):
        self.flex = flex
        self.child = child
        self.identifier = identifier
        self.__node_init__(listening=["ram.touching"], level = level)

    @tlog
    def notify(self, name, value):
        print(self.constraint.out())
        if name == "ram.touching":
            fakepoint = uPoint(value[0], value[1])
            if fakepoint.isInArea(self.constraint.copy):
                print("lol")

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