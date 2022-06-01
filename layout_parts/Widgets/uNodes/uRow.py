from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog


class uROW(uNODE):
    @tlog
    def __init__(self, children : list = None, listening : list = [], seperator : int = 0, spacing : str = "center", container : uNODE = None, include_sides : bool = True, divider_thickness : int = 0, flex = 1):
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
    def constrainmod(self, value : uConstrain):
        self.constraint = value.copy
        if self.children == None:
            return 
        new_full_constrain = value.copy
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
        total_flex = 0
        if self.children != None or self.children.empty:
            for child in self.children:
                total_flex = total_flex + child.flex
            if total_flex == 0:
                return
            seperators_placed = 0
            pixels_per_flex = (width_to_fill - pixels_seperator - pixels_for_dividers) / total_flex
            constraints = []
            set_flex = 0
            if self.spacing == "center":
                if self.include_sides:
                    for index in range(len(self.children)):
                        childconst = uConstrain(
                            pointA=uPoint(
                                x = self.constraint.pointA.x + (seperators_placed + 1) * self.divider_thickness + seperators_placed * pixels_per_seperator + set_flex * pixels_per_flex,
                                y = self.constraint.pointA.y
                            ),
                            pointB=uPoint(
                                x = self.constraint.pointA.x + (seperators_placed + 1) * self.divider_thickness + seperators_placed * pixels_per_seperator + pixels_per_flex * (self.children[index].flex + set_flex),
                                y = self.constraint.pointB.y
                            )
                        )
                        set_flex += self.children[index].flex
                        seperators_placed = index
                        constraints.append(childconst)
            elif self.spacing == "start":
                for index in range(len(self.children)):
                        childconst = uConstrain(
                            pointA=uPoint(
                                x = self.constraint.pointA.x + (seperators_placed + 1) * self.divider_thickness + set_flex * pixels_per_flex,
                                y = self.constraint.pointA.y
                            ),
                            pointB=uPoint(
                                x = self.constraint.pointA.x + (seperators_placed + 1) * self.divider_thickness + pixels_per_flex * (self.children[index].flex + set_flex),
                                y = self.constraint.pointB.y
                            )
                        )
                        set_flex += self.children[index].flex
                        seperators_placed = index
                        constraints.append(childconst)

            elif self.spacing == "end":
                for index in range(len(self.children)):
                        childconst = uConstrain(
                            pointA=uPoint(
                                x = self.constraint.pointA.x + pixels_seperator + (seperators_placed + 1) * self.divider_thickness + set_flex * pixels_per_flex,
                                y = self.constraint.pointA.y
                            ),
                            pointB=uPoint(
                                x = self.constraint.pointA.x + pixels_seperator + (seperators_placed + 1) * self.divider_thickness + pixels_per_flex * (self.children[index].flex + set_flex),
                                y = self.constraint.pointB.y
                            )
                        )
                        set_flex += self.children[index].flex
                        seperators_placed = index
                        constraints.append(childconst)

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

                    
    @tlog
    def draw(self):
        children_calls = []
        if len(self.children) > 0:
            for x in self.divider_xss:
                if self.divider_thickness > 0:
                    obj = udraw_Line(pointA=uPoint(x = x, y = self.constraint.pointA.y), pointB=uPoint(x = x, y = self.constraint.pointB.y), thickness=self.divider_thickness)
                    children_calls.append(obj)
            for child in self.children:
                for draw_call in child.draw():
                    children_calls.append(draw_call)
        if NotifyService.get("debug.widget-draw_constraints"):
            children_calls.append(udraw_Rectangle(pointA=self.constraint.pointA, pointB=self.constraint.pointB, is_debug=True))
        return children_calls
