from layout_parts.Widgets.uNodes.unode_util.uexceptions import *

from graphics import *

class Cluster():
    def __init__(self, anchor : Point, end : Point, display_number : int, x : int, y : int):
        self.row = y
        self.column = x
        self.anchor = anchor
        self.end = end
        self.display_number = display_number

    def out(self):
        return "(" + str(self.anchor.y) + "|" + str(self.anchor.x) + ")-(" + str(self.end.y) + "|" + str(self.end.x) + ")"

    @property
    def gridcoords(self):
        return str(self.row) + "|" + str(self.column)

    def giveWidget(self, obj):
        self.widget = obj

    @property
    def rect(self):
        output = Rectangle(p1=self.anchor, p2=self.end)
        output.setFill("blue")
        return output

class uPoint():
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        if x == None or y == None:
            raise uHELPEREXCEPTION("Node needs both, x and y, specified.", self.__class__.__name__)

    def to_point(self) -> Point:
        return Point(x = self.x, y = self.y)

    def out(self):
        return "(" + str(self.x) + "|" + str(self.y) + ")"

    @property
    def copy(self):
        return uPoint(x = self.x, y = self.y)

    def isInArea(self, constraint):
        return self.x > constraint.pointA.x and self.x < constraint.pointB.x and self.y > constraint.pointA.y and self.y < constraint.pointB.y
        
class uConstrain():
    def __init__(self, pointA : uPoint, pointB : uPoint):
        self.pointA = uPoint(x = min([pointA.x, pointB.x]), y = min([pointA.y, pointB.y]))
        self.pointB = uPoint(x = max([pointA.x, pointB.x]), y = max([pointA.y, pointB.y]))      

    def out(self) -> str:
        return "(" + str(self.pointA.x) + "|" + str(self.pointA.y) + "),(" + str(self.pointB.x) + "|" + str(self.pointB.y) + ")"

    @property
    def width(self):
        return max(self.pointA.x, self.pointB.x) - min(self.pointA.x, self.pointB.x)
    @property
    def height(self):
        return max(self.pointA.y, self.pointB.y) - min(self.pointA.y, self.pointB.y)

    @property
    def copy(self):
        return uConstrain(pointA=uPoint(x = self.pointA.x, y = self.pointA.y), pointB=uPoint(x = self.pointB.x, y = self.pointB.y))

    @property
    def center(self):
        return uPoint(x = self.pointA.x + ((self.pointB.x - self.pointA.x) / 2), y = self.pointA.y + ((self.pointB.y - self.pointA.y) / 2))
    
    def isSafe(self, other_const, name):
        if self.pointA.x < other_const.pointA.x:
            input()
            raise uBUILDTIMEEXCEPTION("Constrain out of bounds. May fix overlap or put it on another level.", name)
        if self.pointB.x > other_const.pointB.x:
            input()
            raise uBUILDTIMEEXCEPTION("Constrain out of bounds. May fix overlap or put it on another level.", name)
        if self.pointA.y < other_const.pointA.y: 
            input()
            raise uBUILDTIMEEXCEPTION("Constrain out of bounds. May fix overlap or put it on another level.", name)
        if self.pointB.y > other_const.pointB.y:
            input()
            raise uBUILDTIMEEXCEPTION("Constrain out of bounds. May fix overlap or put it on another level.", name)
        else:
            return True

class Task():
    def __init__(self, title : str, creation : str = None, date : str = None, time : str = None, endtime : str = None, tags : list = None, description : str = None, key : str = ""):
        self.date = date
        self.time = time
        self.tags = tags
        self.title = title
        self.description = description
        self.endtime = endtime
        self.key = key
        self.title = title
        self.creation = creation

class uCCSETTINGSdata():
    def __init__(self, current_page, maxpages, max_items_per_page, pagedata):
        self.current_page = current_page
        self.maxpages = maxpages
        self.max_items_per_page = max_items_per_page
        self.pagedata = pagedata

    @property
    def copy(self):
        return uCCSETTINGSdata(
            current_page = self.current_page,
            maxpages = self.maxpages,
            max_items_per_page = self.max_items_per_page,
            pagedata = self.pagedata.copy()
        )