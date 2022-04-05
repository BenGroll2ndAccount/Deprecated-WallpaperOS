from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL

body = uCOLUMN(
    seperator = 20,
    children = [
        uCARD(filled = True),
        uCARD(filled = True, flex = 2)
    ]
)
