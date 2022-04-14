from email import header
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle, udraw_Text, udraw_Polygon
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from notifier import NotifyService

class uHEAD(uNODE):
    @tlog
    def __init__(self, anchor : uPoint ,width : int, height : int, body : uNODE, listening : list = None, header : str = None, headercontent : str = None, flex = 1, headershape : str = "rect"):
        self.anchor : uPoint = anchor
        self.width : int = width  
        self.height : int = height
        self.headershape = headershape
        self.flex = flex
        self.child : uNODE = body
        self.header : str = header
        self.headercontent : str = headercontent
        self.__node_init__(listening=listening, level = 0)

    @tlog
    def notify(self, name, value):
        pass

    @tlog
    def constrainmod(self):
        self.constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        __HEADERSIZE__ : int = NotifyService.get("debug.widget-header_thickness_in_clusters")
        __HEADERRESOLUTION__ : int = NotifyService.get("debug.display-cluster_resolution")
        new_constraint = None
        if self.header == "t":
            new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x, y = __HEADERSIZE__ * __HEADERRESOLUTION__), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        elif self.header == "l":
            new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x + __HEADERSIZE__ * __HEADERRESOLUTION__, y = self.anchor.y), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        elif self.header == "r":
            new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width - (__HEADERSIZE__ * __HEADERRESOLUTION__), y = self.anchor.y + self.height))
        elif self.header == "b":
            new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - (__HEADERSIZE__ * __HEADERRESOLUTION__)))
        else:
            return self.child.constrainmod(self.constraint.copy)
        self.child.constrainmod(new_constraint.copy)

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        outlist = []
        background_call = udraw_Rectangle(pointA=self.anchor, pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height), filled=True, border_is_highlight=False, fill_match_border=True)
        #list.append(background_call)
        child_calls : list = self.child.draw()
        for call in child_calls:
            outlist.append(call)    
        __HEADERSIZE__ : int = NotifyService.get("debug.widget-header_thickness_in_clusters")
        __HEADERRESOLUTION__ : int = NotifyService.get("debug.display-cluster_resolution")
        if self.header == "t":
            headerconsts = uConstrain(pointA=uPoint(x=self.anchor.x, y = self.anchor.y), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + __HEADERRESOLUTION__ * __HEADERSIZE__))
        elif self.header == "l":
            headerconsts = uConstrain(pointA=uPoint(x=self.anchor.x ,y = self.anchor.y), pointB=uPoint(x = self.anchor.x + __HEADERRESOLUTION__ * __HEADERSIZE__, y = self.anchor.y + self.height))
        elif self.header == "r":
            headerconsts = uConstrain(pointA = uPoint(x = self.anchor.x + self.width - __HEADERRESOLUTION__ * __HEADERSIZE__, y = self.anchor.y), pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        elif self.header == "b":
            headerconsts = uConstrain(pointA = uPoint(x = self.anchor.x, y = self.anchor.y + self.height - __HEADERRESOLUTION__ * __HEADERSIZE__), pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        if self.header != None:
            self.headerText = uLABEL(varname = self.headercontent, nice = True, highlight=False)
            self.headerText.constrainmod(headerconsts.copy)
            headertextcalls = self.headerText.draw()
            if self.headershape == "poly":
                outlist.append(udraw_Polygon(pointA=headerconsts.pointA, pointB = uPoint(x = headerconsts.pointA.x + __HEADERRESOLUTION__ * __HEADERSIZE__, y = headerconsts.pointA.y + headerconsts.height), pointC = uPoint(headerconsts.pointB.x - __HEADERRESOLUTION__ * __HEADERSIZE__, y = headerconsts.pointA.y + headerconsts.height), pointD = uPoint(x = headerconsts.pointA.x + headerconsts.width, y = headerconsts.pointA.y), border_is_highlight=True, filled = True, fill_match_border=True,thickness = 1)) 
            else:
                outlist.append(udraw_Rectangle(pointA=headerconsts.pointA, pointB=headerconsts.pointB, border_is_highlight=True, filled = True, fill_match_border=True))

            for htcall in headertextcalls:
                outlist.append(htcall)
        return outlist