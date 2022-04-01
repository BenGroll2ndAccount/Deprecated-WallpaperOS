from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import log


class uROW(uNODE):
    @log
    def __init__(self, children : list, listening : list = [], seperator : int = 0, spacing : str = "center", container : uNODE = None, include_sides : bool = True):
        allowed_spacings = {"start", "center", "end"}
        if spacing not in allowed_spacings:
            self.spacing = "center"
        else:
            self.spacing = spacing
        self.seperator = seperator
        self.spacing = spacing
        self.container = container
        self.include_sides = include_sides
        if container != None:
            children_cont = []
            for child in children:
                placeholder = child
                new_child = container
                container.child = placeholder
                children_cont.append(new_child)
            self.children = children_cont
        else:
            self.children = children
        self.__node_init__(listening=listening, level = 0)
    @log
    def notify(name, value):
        raise NotImplementedError#
    @log
    def constrainmod(self, value : uConstrain):
        self.constraint = uConstrain(pointA=uPoint(x = value.pointA.x, y = value.pointA.y), pointB=uPoint(x = value.pointB.x, y = value.pointB.y))
        if self.children == None:
            return
        constwidth = value.width
        pixels_for_seperation = (self.seperator / 100) * constwidth
        pixels_for_constraints = constwidth - pixels_for_seperation
        pixels_for_each_seperator = pixels_for_seperation / (len(self.children) + 1) if self.include_sides else pixels_for_seperation / (len(self.children) - 1)
        pixels_for_each_widget = pixels_for_constraints / len(self.children)
        for index in range(len(self.children)):
            if self.include_sides and self.spacing == "center":
                self.children[index].constrainmod(value = uConstrain(pointA=uPoint(
                    x =  self.constraint.pointA.x + pixels_for_each_widget * index + pixels_for_each_seperator * (index + 1),
                    y =  self.constraint.pointA.y),
                    pointB=uPoint(
                    x = self.constraint.pointA.x + pixels_for_each_widget * (index + 1) + pixels_for_each_seperator * (index + 1),
                    y =  self.constraint.pointB.y
                    )
                ))
                print(self.children[index].constraint.out())
            elif not self.include_sides and self.spacing == "center":
                self.children[index].constrainmod(value = uConstrain(
                    pointA=uPoint(
                    x =  self.constraint.pointA.x + pixels_for_each_widget * index + pixels_for_each_seperator * index,
                    y = self.constraint.pointA.y),
                    pointB=uPoint(
                    x = self.constraint.pointA.x + pixels_for_each_widget * (index + 1) + pixels_for_each_seperator * index,
                    y = self.constraint.pointB.y
                    )
                )) 
                print(self.children[index].constraint.out())
            else:
                raise NotImplementedError()
    @log
    def draw(self):
        children_calls = []
        for child in self.children:
            for draw_call in child.draw():
                children_calls.append(draw_call)
        if NotifyService.get("debug.widget-draw_constraints"):
            children_calls.append(udraw_Rectangle(pointA=self.constraints.pointA, pointB=self.constraints.pointB, is_debug=True))
        return children_calls
