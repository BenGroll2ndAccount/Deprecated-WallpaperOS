from layout_parts.Widgets.Calendar import body as calendar_body
from layout_parts.Widgets.uNodes.uHead import uHEAD
import time
from elapsed import *
from layout_parts.Widgets.uNodes.unode_util.helperclasses import uConstrain, uPoint

class WIDGET():
    @property
    def drawcalls(self):
        return self.head.draw()
    
    def finish(self):
        wait = self.head.assign_depth(0)
        wait = self.head.constrainmod()
        wait = self.head.constraincheck(uConstrain(pointA=uPoint(0,0), pointB=uPoint(self.head.width+1, self.head.height + 1)), 0)
        print("Calendar")
        print("-------------------")
        print("Type" + " " * (100 - len("Type")) + "Depth" + " " + "Constraints")
        wait = self.head.output()
        print("-------------------", end="")

class Calendar(WIDGET):
    def __init__(self, clusters : list, header : str, headercontent : str = None, headershape : str = "rect"):
        t = time.time()
        self.clusters = clusters
        self.head : uHEAD = uHEAD(
            headershape=headershape,
            header = header,
            headercontent = headercontent if headercontent != None else self.__class__.__name__,
            anchor = self.clusters[0].anchor,
            width = self.clusters[-1].end.x - self.clusters[0].anchor.x,
            height = self.clusters[-1].end.y - self.clusters[0].anchor.y,
            body = calendar_body
        )
        self.finish()
        elapsedtime(t)
        return