from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import log
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import tlog

class uHEAD(uNODE):
    @tlog
    def __init__(self, anchor : uPoint ,width : int, height : int, body : uNODE, listening : list = None, header : str = None, headercontent : str = None):
        self.anchor : uPoint = anchor
        self.width : int = width  
        self.height : int = height
        self.child : uNODE = body
        self.header : str = header
        self.headercontent : str = headercontent
        self.__node_init__(listening=listening, level = 0)

    @tlog
    def notify(self, name, value):
        pass

    @tlog
    def constrainmod(self):
        self.constraint = uConstrain(pointA=uPoint(x=0, y=0), pointB=uPoint(x=self.width, y=self.height))
        self.child.constrainmod(self.constraint.copy)

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        header_calls = []
        if self.header != None:
            childplaceholder = self.child
            ############s
            ############
            ############ -> LEFT OFF
            ############
            ############
        background_call = udraw_Rectangle(pointA=self.anchor, pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height), filled=True, border_is_highlight=False, fill_match_border=True)
        list = []
        list.append(background_call)
        child_calls : list = self.child.draw()
        for call in child_calls:
            list.append(call)
        return list