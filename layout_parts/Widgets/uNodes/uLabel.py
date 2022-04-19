from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle, udraw_Text
from layout_parts.Widgets.uNodes.unode_util.uexceptions import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
import pretty as pretty
from notifier import NotifyService

class uLABEL(uNODE):
    @tlog
    def __init__(self, varname = None, nice : bool = False, size : int = 36, highlight : bool = True, flex = 1):
        self.text = ""
        self.varname = ""
        self.nice = nice
        self.flex = flex
        self.child = None
        self.size = size
        self.highlight = highlight
        
        if varname != None and str.startswith(varname, "_"):
            varvalue = NotifyService.get(varname.split("_")[1])
            self.text = self.formatt(varname.split("_")[1], varvalue)
            self.__node_init__([varname.split("_")[1]], level = 0)
        else:
            self.text = varname
            self.__node_init__(listening = [])
       
        
    @tlog
    def notify(self, name, value):
        if name == self.varname:
            self.text = self.formatt(name, value)
            NotifyService.change("ram.widget_request_redraw", True)

    def formatt(self, varname, value):
        if varname == "timing.weekday":
            return pretty.weekday(value)



    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        maxwidth = self.constraint.width / len(self.text) / 0.6
        if self.size > maxwidth:
            self.size = int(maxwidth)
        if self.size > self.constraint.height:
            self.size = int(self.constraint.height)
        return    

    @tlog
    def miscmod(self):
        return

    @tlog
    def draw(self):
        calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug=True))
        calls.append(udraw_Text(anchorpoint=self.constraint.center, textString=self.text, size=self.size, highlight = self.highlight))
        return calls