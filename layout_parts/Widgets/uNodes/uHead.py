from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle

class uHEAD(uNODE):
    def __init__(self, anchor : uPoint ,width : int, height : int, body : uNODE, listening : list = None):
        self.anchor : uPoint = anchor
        self.width : int = width  
        self.height : int = height
        self.child : uNODE = body
        self.__node_init__(listening=listening, level = 0)

    def notify(self, name, value):
        pass

    def constrainmod(self):
        self.constraint = uConstrain(pointA=uPoint(x=0, y=0), pointB=uPoint(x=self.width, y=self.height))
        return self.child.constrainmod(uConstrain(pointA=uPoint(x=0, y=0), pointB=uPoint(x=self.width, y=self.height)))

    def miscmod(self):
        return self.child.miscmod()

    def draw(self):
        background_call = udraw_Rectangle(pointA=self.anchor, pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height), filled=True, border_is_highlight=False, fill_match_border=True)
        child_calls : list = self.child.draw()
        child_calls.append(background_call)
        return child_calls