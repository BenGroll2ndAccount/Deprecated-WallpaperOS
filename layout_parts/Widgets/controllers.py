from layout_parts.Widgets.calendar import body as calendar_body
from layout_parts.Widgets.uNodes.uHead import uHEAD
import time
from elapsed import *

class WIDGET():
    @property
    def drawcalls(self):
        return self.head.draw()
    
    def finish(self):
        wait = self.head.assign_depth(0)
        wait = self.head.constrainmod()
        print("Calendar")
        print("-------------------")
        print("Type" + " " * (50 - len("Type")) + "Depth" + " " + "Constraints")
        wait = self.head.output()
        print("-------------------", end="")

class Calendar(WIDGET):
    def __init__(self, clusters : list, header : str):
        t = time.time()
        self.clusters = clusters
        self.head : uHEAD = uHEAD(
            header = header,
            anchor = self.clusters[0].anchor,
            width = self.clusters[-1].end.x - self.clusters[0].anchor.x,
            height = self.clusters[-1].end.y - self.clusters[0].anchor.y,
            body = calendar_body
        )
        self.finish()
        elapsedtime(t)
        return