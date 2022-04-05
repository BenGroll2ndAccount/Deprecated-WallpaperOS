from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog


class uROW(uNODE):
    @tlog
    def __init__(self, children : list, listening : list = [], seperator : int = 0, spacing : str = "center", container : uNODE = None, include_sides : bool = True, divider_thickness : int = 1, flex = 1):
        allowed_spacings = {"start", "center", "end"}
        if spacing not in allowed_spacings:
            self.spacing = "center"
        else:
            self.spacing = spacing
        self.seperator = seperator
        self.flex = flex
        self.spacing = spacing
        self.container = container
        self.divider_thickness : int = divider_thickness
        self.include_sides = include_sides
        if container != None:
            children_cont = []
            for child in children:
                placeholder = child
                new_child : uNODE = container
                container.child = placeholder
                children_cont.append(new_child)
            self.children = children_cont
        else:
            self.children = children
        self.__node_init__(listening=listening, level = 0)
    @tlog
    def notify(name, value):
        raise NotImplementedError#

    @tlog
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        new_full_constrain = value.copy
        y_begin = new_full_constrain.pointA.y
        y_end = new_full_constrain.pointB.y
        width_to_fill = new_full_constrain.width
        pixels_seperator = width_to_fill * (self.seperator / 100)
        seperator_count = len(self.children) - 1 
        seperator_count = seperator_count + 2 if self.include_sides else seperator_count
        if self.divider_thickness > 0:
            divdier_count = len(self.children) - 1
            pixels_for_dividers = divdier_count * self.divider_thickness
        else:
            divdier_count = 1
            pixels_for_dividers = 0
        pixels_per_seperator = pixels_seperator / seperator_count
        pixels_per_widget = (width_to_fill - pixels_seperator - pixels_for_dividers) / len(self.children)
        constraints = []
        if self.spacing == "center":
            if self.include_sides:
                for index in range(len(self.children)):
                    childs_constrain = uConstrain(
                        pointA=uPoint(
                            x = new_full_constrain.pointA.x + pixels_per_seperator + (pixels_per_seperator * index) + pixels_per_widget * index + (pixels_for_dividers / divdier_count) * index,
                            y = y_begin
                        ),
                        pointB=uPoint(
                            x = new_full_constrain.pointA.x + pixels_per_seperator + (pixels_per_seperator * index) + pixels_per_widget * (index + 1) + (pixels_for_dividers / divdier_count) * index,
                            y = y_end
                        )
                    )
                    constraints.append ( childs_constrain.copy )
                    del childs_constrain
        for childex in range(len(self.children)):
            self.children[childex].constrainmod(constraints[childex].copy)
        divider_x_coords = []
        for idx in range(len(self.children)):
            if not len(self.children) <= idx + 1:
                x_begin : int= self.children[idx].constraint.pointB.x
                x_end : int = self.children[idx + 1].constraint.pointA.x
                x = x_begin + ((x_end - x_begin) / 2)
                divider_x_coords.append(x)
        self.divider_xss = divider_x_coords
        print(self.divider_xss)
                    
    @tlog
    def draw(self):
        children_calls = []
        for x in self.divider_xss:
            obj = udraw_Line(pointA=uPoint(x = x, y = self.constraint.pointA.y), pointB=uPoint(x = x, y = self.constraint.pointB.y), thickness=self.divider_thickness)
            children_calls.append(obj)
        for child in self.children:
            for draw_call in child.draw():
                children_calls.append(draw_call)
        if NotifyService.get("debug.widget-draw_constraints"):
            children_calls.append(udraw_Rectangle(pointA=self.constraint.pointA, pointB=self.constraint.pointB, is_debug=True))
        return children_calls
