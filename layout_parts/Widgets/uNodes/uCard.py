from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
class uCARD(uNODE):
    @tlog
    def __init__(self, child : uNODE = None,rounding : int = 0, filled : bool = True, fill_match_border : bool = True, highlight : bool = False, thickness : int = 1,  listening : list = None, level : int = 0, flex = 1):
        self.rounding = rounding
        self.filled = filled
        self.fill_border = fill_match_border
        self.highlight = highlight
        self.child = child
        self.thickness = thickness
        self.flex = 1
        self.__node_init__(listening=listening, level = level)

    @tlog
    def notify(self, name, value):
        pass

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
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, border_is_highlight = self.highlight, thickness = self.thickness, rounding = self.rounding, round_oct = NotifyService.get("debug.ll-draw_rect_rounding_oct"), filled = self.filled, fill_match_border=self.fill_border, is_debug=False))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in own_draw_calls:
            child_calls.append(call)
        return child_calls