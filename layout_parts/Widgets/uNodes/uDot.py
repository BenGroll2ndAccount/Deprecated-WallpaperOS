from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
class uDOT(uNODE):
    @tlog
    def __init__(self, child : uNODE = None,filled : bool = True, fill_match_border : bool = True, highlight : bool = True, thickness : int = 1, listening : list = None, level : int = 0, flex = 1):
        self.filled = filled
        self.fill_border = fill_match_border
        self.highlight = highlight
        self.child = child
        self.thickness = thickness
        self.flex = flex
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
        print("JHASODHOASHDOJSHDOASHDOAHODAHJSODASODN")
        own_draw_calls = []
        print(self.constraint.out())
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        own_draw_calls.append(udraw_Circle(point = self.constraint.center, radius=self.constraint.width / 2, highlight=self.highlight))
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls