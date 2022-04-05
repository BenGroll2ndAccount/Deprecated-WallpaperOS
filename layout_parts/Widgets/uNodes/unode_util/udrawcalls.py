from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.uexceptions import *

class udraw_Pixel():
    def __init__(
                self, 
                position : uPoint,
                highlight : bool = True
                ):
        if position != None: # Requirance check
            self.position = position #Point Class
            self.highlight = highlight
        else:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "")

class udraw_Line():
    def __init__(
            self,
            pointA : uPoint = None,
            pointB: uPoint = None,
            highlight: bool = True,
            thickness : int = 1
            ):
        if pointA == None or pointB == None:
            raise uDRAWEXCEPTION(widget=self.__class__.__name__, message = "Draw needs both start and endpoint")
        self.pointA = pointA
        self.pointB = pointB
        self.highlight = highlight
        self.thickness = thickness

    def out(self):
        return f"udraw_Line @" + self.pointA.out() + self.pointB.out() + "_highlight: " + str(self.highlight) + ", thickness: " + str(self.thickness)

class udraw_Rectangle():
    def __init__(
            self, 
            pointA : uPoint = None,
            pointB : uPoint = None,
            border_is_highlight : bool = True,
            thickness : int = 1,
            rounding : int = 0,
            round_oct : bool = True,
            filled : bool = False,
            fill_match_border : bool = False,
            is_debug : bool = False
            ):
        if pointA == None or pointB == None:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "Draw needs both start and endpoint")
        self.pointA = pointA
        self.pointB = pointB
        self.border_is_highlight = border_is_highlight
        self.thickness = thickness
        rounding_length = 0
        smaller_side = "h" if (pointB.x - pointA.x) > (pointB.y - pointA.y) else "v"
        if smaller_side == "h":
            rounding_length  = pointB.x - pointA.x
        else:
            rounding_length = pointB.y - pointA.y
        total_rounding = rounding_length * (rounding / 100)
        self.rounding = total_rounding
        self.round_oct = round_oct
        self.filled = filled
        self.fill_border = fill_match_border
        self.is_debug = is_debug

    def out(self):
        return "udraw_Rectangle @" + self.pointA.out() + self.pointB.out() + "border_is_highlight: " + str(self.border_is_highlight) + ", thickness: " + str(self.thickness) + ", rounding: " + str(self.rounding) + ", round_oct: " + str(self.round_oct) + ", filled: " + str(self.filled) + ", fill_match_border: " + str(self.fill_border) + ", is_debug: " + str(self.is_debug)

class udraw_Circle():
    def __init__(
            self,
            point : uPoint = None,
            radius : int = 1,
            highlight : bool = True
            ):
        if point == None:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "Draw needs a centerpoint.")
        self.point = point,
        self.radius = radius
        self.highlight = highlight

class udraw_Text():
    def __init__(self, anchorpoint : uPoint = None, textString : str = "Lorem", size : int = 8, highlight : bool = True):
        self.anchorpoint = anchorpoint
        self.textString : str = textString
        self.size : int = size
        self.highlight = highlight

    def out(self):
        return "udraw_Text @" + str(self.anchorpoint.out()) + "highlight: " + str(self.highlight) + ", size: "# + str(self.size) + ", textString: " + self.textString  