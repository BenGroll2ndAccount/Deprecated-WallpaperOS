from notifier import NotifyService
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
class uRECT(uNODE):
    @tlog
    def __init__(self, child : uNODE = None, flex = 1):
        self.child = child
        self.flex = flex

    @tlog
    def notify(self, name, value):
        pass

    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.child != None:
            new_constraint = value.copy
            smaller_value = min([new_constraint.width, new_constraint.height])
            new_value = smaller_value
            if new_constraint.width != new_value:
                width_to_reduce_by = new_constraint.width - smaller_value
                new_constraint.pointA.x += width_to_reduce_by / 2
                new_constraint.pointB.x -= width_to_reduce_by / 2
            if new_constraint.height != new_value:
                height_to_reduce_by = new_constraint.height - smaller_value
                new_constraint.pointA.y += height_to_reduce_by / 2
                new_constraint.pointB.y -= height_to_reduce_by / 2
            #self.child.constraint = new_constraint
            if self.child != None:
                self.child.constrainmod(uConstrain(pointA=uPoint(new_constraint.pointA.x, new_constraint.pointA.y), pointB = uPoint(new_constraint.pointB.x, new_constraint.pointB.y)))
            


        if self.child != None:
            self.child.constrainmod(self.constraint.copy)
        else:
            return 0

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        if self.child != None:
            return self.child.draw()
        else:
            return []