from layout_parts.Widgets.uNodes.unode_util.uexceptions import *
from graphics import *

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
        return uConstrain(pointA=uPoint(x = self.pointA.x, y = self.pointA.y), pointB=uPoint(x = self.pointB.x, y = self.pointB.y ))

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
    def __init__(self, title : str, date : str = None, time : str = None, endtime : str = None, category : str = None, description : str = None, key : str = ""):
        self.date = date
        self.time = time
        self.category = category
        self.title = title
        self.description = description
        self.endtime = endtime
        self.key = key
