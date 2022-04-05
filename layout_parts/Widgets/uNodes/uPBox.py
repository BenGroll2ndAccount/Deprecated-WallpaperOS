from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle
from layout_parts.Widgets.uNodes.unode_util.uexceptions import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog


from notifier import NotifyService

class uPBOX(uNODE):
    @tlog
    def __init__(self, child : uNODE, listening : list = [], modH : int = 100, modV : int = 100, vAlign : str = "center", hAlign : str = "center", flex = 1):
        allowed_aligns = ["start","center","end"]
        if vAlign not in allowed_aligns:
            raise uPROPERTYEXCEPTION(vAlign + " not a valid align. Valid values include: start, center, end.", self)
        if hAlign not in allowed_aligns:
            raise uPROPERTYEXCEPTION(hAlign + " not a valid align. Valid values include: start, center, end", self)
        self.child : uNODE = child
        self.flex = flex
        self.modH : int = modH
        self.modV : int = modV
        self.vAlign : str = vAlign
        self.hAlign : str = hAlign
        self.__node_init__(listening=listening, level = 0)

    @tlog
    def notify(self, name, value):
        pass

    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        new_const = value.copy
        if self.modH != 100:
            modXfactor = self.modH / 100
            whole_pixels_horizontal = new_const.width
            pixels_to_remove = whole_pixels_horizontal * (1 - modXfactor)    
            if self.hAlign == "center":
                new_const.pointA.x += pixels_to_remove / 2
                new_const.pointB.x -= pixels_to_remove / 2
            if self.hAlign == "start":
                new_const.pointB.x -= pixels_to_remove
            if self.hAlign == "end":
                new_const.pointA.x += pixels_to_remove

        if self.vAlign != 100:
            modYfactor = self.modV / 100
            whole_pixels_vertical = new_const.height
            pixels_to_remove = whole_pixels_vertical * (1 - modYfactor)
            if self.vAlign == "center":
                new_const.pointA.y += pixels_to_remove / 2
                new_const.pointB.y -= pixels_to_remove / 2
            if self.vAlign == "start":
                new_const.pointB.y -= pixels_to_remove
            if self.vAlign == "end":
                new_const.pointA.y += pixels_to_remove
            


        if self.child != None:
            self.child.constrainmod(new_const.copy)
            

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        calls = []
        if NotifyService.get("debug.widget-draw_constraints"):
            calls.append(Rectangle(p1 = self.constraint.pointA.to_point(), p2=self.constraint.pointB.to_point()))
        if self.child != None:
            for call in self.child.draw():
                calls.append(call)
        return calls