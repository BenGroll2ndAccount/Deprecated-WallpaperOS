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



class uConstrain():
    def __init__(self, pointA : uPoint, pointB : uPoint):
        self.pointA = pointA
        self.pointB = pointB

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

