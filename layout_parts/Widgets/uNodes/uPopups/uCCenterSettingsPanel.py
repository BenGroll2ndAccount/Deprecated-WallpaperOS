from notifier import NotifyService
from layout_parts.Widgets.uNodes.uPopups.uPopup import uPOPUP
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.bodies import BODIES

class uCCSETTINGS(uPOPUP):
    @tlog
    def __init__(self, parentwidget):
        self.parentwidget = parentwidget
        # LOAD CORRESPONDING WIDGET SETTING DATA HERE
        # DUMMY
        self.current_page = 0
        self.total_pages = 2
        # \DUMMY
        self.body = BODIES.ControlCenterSettingsPanel(self.parentwidget, dummy = True)
        self.__node_init__(listening=[], level = 0)
        
    