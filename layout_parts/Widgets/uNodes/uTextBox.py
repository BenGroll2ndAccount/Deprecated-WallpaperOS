from re import U
from layout_parts.Widgets.uNodes.uTouchArea import uTOUCHAREA
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uLabel import uLABEL


from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.helperclasses import Task

class uTEXTBOX(uNODE):
    @tlog
    def __init__(self, funcname : str = None, rounding : int = 5, thickness : int = 4, level : int = 0, flex : int = 1, parentwidget = None):
        self.funcname = funcname
        self.rounding = rounding
        self.thickness = thickness
        self.parentwidget = parentwidget
        self.text = "..."
        self.level = level
        self.flex = flex
        self.open = False
        self.buildChild(textcontent=self.text)

    def notify(self, string):
        if string == "TextBoxClicked":
            if not self.open:
                self.open = True
                NotifyService.subscribeIfTouchedOutSide(self)
                NotifyService.subscribe_to_keyboard(self)
                self.child.child.thickness += 1
                NotifyService.register_event("redraw")
                self.text = " "
        elif string == "event.touchedOutside":
            if self.open:
                self.open = False
                NotifyService.unsubscribeIfTouchedOutSide(self)
                NotifyService.resumeMainKeyLoop()
                self.child.child.thickness -= 1
                NotifyService.register_event("redraw")

        elif string.split("_")[0] == "keyboard":
            if string.split("_")[1] == "Return":
                self.open = False
                NotifyService.unsubscribeIfTouchedOutSide(self)
                NotifyService.resumeMainKeyLoop()
                self.child.child.thickness -= 1
                self.buildChild(self.text)
                self.constrainmod(self.constraint.copy)
                NotifyService.register_event("redraw")
            else:
                self.text = self.text + string.split("_")[1]
                self.parentwidget.notify("Textbox_" + self.funcname + "_" + self.text)
                self.buildChild(self.text)
                self.constrainmod(self.constraint.copy)
                NotifyService.register_event("redraw")

    def buildChild(self, textcontent):
        self.child = uTOUCHAREA(
            parentwidget=self,
            funcname="TextBoxClicked",
            level = self.level,
            child = uCARD(
                thickness = self.thickness,
                rounding = self.rounding,
                highlight = True,
                filled = True,
                fill_match_border = False,
                child=uLABEL(
                    varname = textcontent
                )           
            )
        )
        
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
        if self.child != None:
            child_calls : list = self.child.draw()
        else:
            child_calls = []
        for call in child_calls:
            own_draw_calls.append(call)
        return own_draw_calls
