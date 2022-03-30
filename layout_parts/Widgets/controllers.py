from layout_parts.Widgets.calendar import body as calendar_body
from layout_parts.Widgets.uNodes.uHead import uHEAD

class WIDGET():
    @property
    def drawcalls(self):
        return self.head.draw()

class Calendar(WIDGET):
    def __init__(self, clusters : list):
        self.clusters = clusters
        self.head : uHEAD = uHEAD(
            anchor = self.clusters[0].anchor,
            width = self.clusters[-1].end.x - self.clusters[0].anchor.x,
            height = self.clusters[-1].end.y - self.clusters[0].anchor.y,
            body = calendar_body
        )
        wait = self.head.assign_depth(0)
        wait = self.head.constrainmod()
        wait = self.head.output()
        return