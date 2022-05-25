from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uControllerNodes import uCHECKBOX
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uTextBox import uTEXTBOX

from notifier import NotifyService
from layout_parts.Widgets.uNodes.uPopups.uPopup import uPOPUP
from layout_parts.Widgets.uNodes.uPopups.uTaskCreationPanel import uTASKCREATIONPANEL

from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.bodies import BODIES
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *


class uTASKCREATIONPANELHEADERQUESTION(uPOPUP):
    @tlog
    def __init__(self, parentwidget):
        NotifyService.subscribeIfTouchedOutSide(self)
        self.parentwidget = parentwidget
        self.body = uCARD(
                filled = True,
                highlight = True, 
                fill_match_border = False,
                thickness= 4,
                child = uCOLUMN(
                    divider_thickness=4,
                    seperator=10,
                    children=[
                        uLABEL("Enter title:"),
                        uPBOX(
                            uROW(
                                children=[
                                    uTEXTBOX(funcname = "EnteredTitle", rounding = 10, thickness = 3, level = 2, parentwidget = self),
                                    uPBOX(
                                        uCHECKBOX(
                                        widget_to_notify=self,
                                        initial_status=False,
                                        name = "NameSubmitted",
                                        level = 4,
                                        ),
                                        modH = 80,
                                        modV = 80,
                                        flex = 0.3
                                    )
                                ],
                            ),
                            modH = 95,
                            modV = 50,
                            flex = 3,
                        )
                    ]
                )
            )
        
        self.__node_init__(listening=[], level = 0)
        self.hasSomethingChanged = False

    def notify(self, info):
        self.textboxreference = self.body.child.children[1].child.children[0]
        if info == "NameSubmitted":
            headertitle = self.textboxreference.text
            self.parentwidget.notify("OpenTaskCreationPanel_" + headertitle, None)
        if info == "event.touchedOutside":
            print("Still HERE!")
            self.parentwidget.notify("touched.POPUP.DISCARD", None)
