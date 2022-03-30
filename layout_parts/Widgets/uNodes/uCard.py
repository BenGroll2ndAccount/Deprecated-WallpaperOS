from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
class uCARD(uNODE):
    def __init__(self, rounded : bool = False, rounding : int = False, filled : bool = True, fill_match_border : bool = False, highlight : bool = False, thickness : int = 1, child : uNODE = None, listening : list = None, level : int = 0):
        self.rounded = rounded
        self.rounding = rounding
        self.filled = filled
        self.fill_border = fill_match_border
        self.highlight = highlight
        self.child = child
        self.thickness = thickness
        self.__node_init__(listening=listening, level = level)

    def notify(self, name, value):
        pass

    def constrainmod(self, value : uConstrain):
        self.constraint = value
        if self.child != None:
            return self.child.constrainmod(uConstrain())
        else:
            return 0

    def miscmod(self):
        return self.child.miscmod()

    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, border_is_highlight = self.highlight, thickness = self.thickness, rounding = self.rounding, round_oct = NotifyService.get("debug.ll-draw-rect-rounding-oct"), filled = self.filled, fill_match_border=self.fill_border, is_debug=False))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in own_draw_calls:
            child_calls.append(call)
        return child_calls