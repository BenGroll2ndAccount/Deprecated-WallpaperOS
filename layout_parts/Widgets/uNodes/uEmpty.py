from layout_parts.Widgets.uNodes.uNode import uNODE
from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog

class uEMPTY(uNODE):
    @tlog
    def __init__(self, flex = 1, level = 0):
        self.flex = flex
        self.__node_init__(listening=[], level = level)


    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy

    @tlog
    def miscmod(self):
        return

    @tlog
    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        return own_draw_calls