from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.helperclasses import uConstrain, uPoint
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle
from notifier import NotifyService

class ControlCenter():
    def __init__(self, constraint, settings, widgetname:str, status):
            self.constraint = constraint
            self.status = status
            self.settings = settings
            builder = getattr(ControlCenterBodyMap, widgetname.split("_")[0] + "ControlCenter"+ "BOTTOM")
            self.body : uNODE = builder(settings = settings)
            self.body.passWidgetData(settings)
            wait = self.body.assign_depth(1)
            wait = self.body.constrainmod(constraint.copy)


    def draw(self):
        return self.body.draw()


class ControlCenterBodyMap():
    def CalendarControlCenterBOTTOM(settings):
        return uCARD(
            
        )










   