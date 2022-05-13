from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.bodies import BODIES

class uControlCenter(uNODE):
    @tlog
    def __init__(self, parentwidget):
        self.parentwidget = parentwidget
        self.status = "Closed"
        self.body = getattr(BODIES, "ControlCenter" + self.parentwidget.widgetname.split("_")[0] + self.status)(parentwidget)
        self.__node_init__(listening=[], level = 0)
        

    @tlog
    def notify(self, name, value):
        pass

    @tlog
    def update_status(self):
        self.body = getattr(BODIES, "ControlCenter" + self.parentwidget.widgetname.split("_")[0] + self.status)(self.parentwidget)
        self.constrainmod(self.constraint.copy)

        NotifyService.register_event("redraw", self.parentwidget.widgetname)

    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.body != None:
            self.body.constrainmod(self.constraint.copy)
        else:
            return 0

    @tlog
    def miscmod(self):
        return self.body.miscmod()

    @tlog
    def draw(self):
        own_draw_calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        if self.body != None:
            child_calls : list = self.body.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls

    @tlog
    def output(self):
        self.assign_depth(1)
        constraintoutput = self.constraint.out()
        print((" " * 5 * self.depth) + self.__class__.__name__ + "-" * (100 - len(self.__class__.__name__) - 5 * self.depth) + " | " + str(self.depth) + "   " + constraintoutput )
        self.body.output()

    @tlog
    def assign_depth(self, value):
        self.depth = value
        self.body.assign_depth(value + 1)
