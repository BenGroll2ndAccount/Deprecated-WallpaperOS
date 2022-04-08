from layout_parts.Widgets.Calendar import body as calendar_body
from layout_parts.Widgets.uNodes.uHead import uHEAD
import time
from layout_parts.Widgets.uNodes.unode_util.helperclasses import uConstrain, uPoint
from notifier import NotifyService


class WIDGET():
    @property
    def drawcalls(self):
        return self.head.draw()
    
    def finish(self, settings):
        self.head.passWidgetData(settings)
        wait = self.head.assign_depth(0)
        wait = self.head.constrainmod()
        
        print("Calendar", end = "")
        if NotifyService.get("debug.widget-output_widget_tree"):
            print("\n-------------------")
            print("Type" + " " * (100 - len("Type")) + "Depth" + " " + "Constraints")
            self.head.output()
            print("-------------------", end="")
        else:
            print("*collapsed*")


class Calendar(WIDGET):
    def __init__(self, clusters : list, header : str, headercontent : str = None, headershape : str = "rect", settings : dict = None):
        t = time.time()
        self.settings  = settings
        self.clusters = clusters
        self.head : uHEAD = uHEAD(
            headershape=headershape,
            header = header,
            headercontent = headercontent if headercontent != None else self.__class__.__name__,
            anchor = self.clusters[0].anchor,
            width = self.clusters[-1].end.x - self.clusters[0].anchor.x,
            height = self.clusters[-1].end.y - self.clusters[0].anchor.y,
            body = calendar_body(self.settings.copy())
        )
        
        self.finish(self.settings)
        return
    
    def constraincheck(self):
        return self.head.constraincheck(self.head.constraint, 0)