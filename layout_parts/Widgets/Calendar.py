from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW

body = uCOLUMN(
    divider_thickness=1,
    seperator = 10,
    children=[
    uROW(
        seperator=20,
        divider_thickness = 2,
        children=[
            uCARD(filled=True),
            uCARD(filled=True)
        ]),
    uROW(
        seperator=20,
        divider_thickness = 2,
        children=[
            uCARD(filled=True),
            uCARD(filled=True)
        ]),
    ]
)
