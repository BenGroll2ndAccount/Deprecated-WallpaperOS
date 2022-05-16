from layout_parts.Widgets.uNodes.uDot import uDOT
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uRect import uRECT
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from layout_parts.Widgets.uNodes.uTouchArea import uTOUCHAREA

def uCHECKBOX(widget_to_notify, initial_status : bool, name : str, level : int):
    return uRECT(uTOUCHAREA(
        level = level,
        parentwidget=widget_to_notify,
        funcname = name +".Flip",
        child = uCARD(
            rounding = 4,
            thickness = 4,
            filled = False,
            highlight = True,
            child = uDOT(filled = True, highlight = True) if initial_status else uEMPTY()
        )
    )
    )