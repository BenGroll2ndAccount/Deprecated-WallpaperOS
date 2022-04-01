from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW

body = uROW(
    container=uPBOX(child=None, modV=40),
    children=[
        uCARD(filled=True),
        uCARD(filled=False),
        uCARD(filled=True)
    ]
)
