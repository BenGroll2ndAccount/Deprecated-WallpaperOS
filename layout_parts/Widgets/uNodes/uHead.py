from layout_parts.Widgets.uNodes.uPopups.uCCenterSettingsPanel import uCCSETTINGS
from layout_parts.Widgets.uNodes.uPopups.uTaskCreationHeaderQuestion import uTASKCREATIONPANELHEADERQUESTION
from layout_parts.Widgets.uNodes.uPopups.uTaskCreationPanel import uTASKCREATIONPANEL
from layout_parts.Widgets.uNodes.uTouchArea import uTOUCHAREA
from layout_parts.Widgets.bodies import BODIES
from layout_parts.Widgets.uNodes.uNode import uNODE
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import udraw_Rectangle, udraw_Text, udraw_Polygon
from layout_parts.Widgets.uNodes.unode_util.decorators import log
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uControlCenter import uControlCenter
from layout_parts.Widgets.uNodes.uPopups.uPopup import uPOPUP
from notifier import NotifyService

class uHEAD(uNODE):
    @tlog
    def __init__(self, anchor : uPoint ,width : int, height : int, body : uNODE, header : str = None, headercontent : str = None, flex = 1, headershape : str = "rect", parentwidget = None, settings = None):
        self.anchor : uPoint = anchor
        self.width : int = width  
        self.height : int = height
        self.headershape = headershape
        self.flex = flex
        self.child : uNODE = body
        self.parentwidget = parentwidget
        self.widgetname = parentwidget.widgetname
        self.settings = settings
        self.controlcenter = None
        self.controlcenterOpenButton = BODIES.ControlCenterOpenButton(self)
        self.popup : uPOPUP = None
        self.header : str = header
        self.headercontent : str = headercontent
        self.__node_init__(listening=[], level = 0)

    @tlog
    def notify(self, name : str, value):
        
        if name.startswith("touched"):
            if name.split(".")[1] == "Task":
                print("Task Opened")
            elif name.split(".")[1] == "CCenterNewTask":
                if self.popup == None:
                    self.popup = uTASKCREATIONPANELHEADERQUESTION(self)
                    self.popup.assign_depth(0)
                    self.constrainmod()
                    NotifyService.register_event("redraw")
            elif name.split(".")[1] == "CCenter":
                if self.controlcenter == None:
                    self.controlcenterOpenButton.level = 2
                    self.controlcenter = uControlCenter(self)
                    self.controlcenter.assign_depth(0)
                    self.controlcenter.status = "Base"
                    self.constrainmod()
                    self.controlcenter.update_status()
                else:
                    if self.popup == None:
                        self.controlcenterOpenButton.level = 1
                        self.controlcenter = None
                        self.constrainmod()
                        NotifyService.register_event("redraw", self.widgetname)
            elif name.split(".")[1] == "CCenterOpenSettings":
                self.controlcenterOpenButton.level = 1
                self.popup = uCCSETTINGS(self)
                self.popup.assign_depth(0)
                self.constrainmod()
            
            elif name.split(".")[1] == "POPUP":
                if name.split(".")[2] == "DISCARD":
                    print("Closed Popup!")
                    self.controlcenterOpenButton.level = 1
                    self.popup = None
                    self.constrainmod()
                    NotifyService.trigger_layout_reload()
                    NotifyService.register_event("redraw", self.widgetname)
                
                    



    @tlog
    def constrainmod(self):
        self.constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        __HEADERSIZE__ : float = NotifyService.get("debug.widget-header_thickness_in_clusters")
        __CLUSTERRESOLUTION__ : int = NotifyService.get("debug.display-cluster_resolution")
        __CCENTERSIZE__ : float = NotifyService.get("debug.widget-controlcenter-thickness-in-clusters")
        new_constraint = None
        if self.controlcenter == None:
            if self.header == "t":
                new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x, y = __HEADERSIZE__ * __CLUSTERRESOLUTION__), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.6, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.6),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.2, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.2)))
            elif self.header == "l":
                new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x + __HEADERSIZE__ * __CLUSTERRESOLUTION__, y = self.anchor.y), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.6, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.6),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.2, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.2)))

            elif self.header == "r":
                new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width - (__HEADERSIZE__ * __CLUSTERRESOLUTION__), y = self.anchor.y + self.height))
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.6, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.6 - __CLUSTERRESOLUTION__ * __HEADERSIZE__),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.2 - __CLUSTERRESOLUTION__ * __HEADERSIZE__, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.2)))

            elif self.header == "b":
                new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - (__HEADERSIZE__ * __CLUSTERRESOLUTION__)))
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.6 + __CLUSTERRESOLUTION__ * 0.5, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.6 - __CLUSTERRESOLUTION__ * __HEADERSIZE__ + __CLUSTERRESOLUTION__ * 0.5),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * 0.2 - __CLUSTERRESOLUTION__ * __HEADERSIZE__+ __CLUSTERRESOLUTION__ * 0.5, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * 0.2+ __CLUSTERRESOLUTION__ * 0.5)))
            else:
                return self.child.constrainmod(self.constraint.copy)
        else:
            if self.header == "t":
                #Set Widget Constraint
                new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x, y = __HEADERSIZE__ * __CLUSTERRESOLUTION__), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - __CLUSTERRESOLUTION__ * __CCENTERSIZE__))
                #Set CCenter Constraint
                button_shrinking_factor = 0.3
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor) + __CLUSTERRESOLUTION__ * __CCENTERSIZE__), pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__  + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor) + __CLUSTERRESOLUTION__ * __CCENTERSIZE__)))
                self.controlcenter.constrainmod(uConstrain(pointA=uPoint(x = new_constraint.pointA.x, y = new_constraint.pointB.y + __CCENTERSIZE__ * __CLUSTERRESOLUTION__), pointB=uPoint(x = new_constraint.pointB.x, y = new_constraint.pointB.y)))
            elif self.header == "l":
                #Set Widget Constraint
                new_constraint = uConstrain(pointA=uPoint(x=self.anchor.x + __HEADERSIZE__ * __CLUSTERRESOLUTION__, y = self.anchor.y), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - __CCENTERSIZE__ * __CLUSTERRESOLUTION__))
                #Set CCenter Constraint
                button_shrinking_factor = 0.3
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor) + __CCENTERSIZE__ * __CLUSTERRESOLUTION__),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__  + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor) + __CLUSTERRESOLUTION__ * __CCENTERSIZE__)))
                self.controlcenter.constrainmod(uConstrain(pointA=uPoint(x = new_constraint.pointA.x + __HEADERSIZE__ * __CLUSTERRESOLUTION__ - __CLUSTERRESOLUTION__, y = new_constraint.pointB.y), pointB=uPoint(x = new_constraint.pointB.x, y = new_constraint.pointB.y + __CCENTERSIZE__ * __CLUSTERRESOLUTION__)))
            elif self.header == "r":
                #Set Widget Constraint
                new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width - (__HEADERSIZE__ * __CLUSTERRESOLUTION__), y = self.anchor.y + self.height - __CLUSTERRESOLUTION__ * __CCENTERSIZE__))
                #Set CCenter Constraint
                button_shrinking_factor = 0.3
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor)),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__  + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor) - __HEADERSIZE__ * __CLUSTERRESOLUTION__, new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor))))
                self.controlcenter.constrainmod(uConstrain(pointA=uPoint(x = new_constraint.pointA.x, y = new_constraint.pointB.y - __CCENTERSIZE__ * __CLUSTERRESOLUTION__), pointB=uPoint(x = new_constraint.pointB.x, y = new_constraint.pointB.y)))
            elif self.header == "b":
                #Set Widget Constraint
                new_constraint = uConstrain(pointA = self.anchor, pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - (__HEADERSIZE__ * __CLUSTERRESOLUTION__) - __CLUSTERRESOLUTION__ * __CCENTERSIZE__))
                #Set CCenter Constraint
                button_shrinking_factor = 0.3
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor) + __CCENTERSIZE__ * __CLUSTERRESOLUTION__ * 1.5),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__  + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor) - __HEADERSIZE__ * __CLUSTERRESOLUTION__+ __CCENTERSIZE__ * __CLUSTERRESOLUTION__ * 1.5)))
                self.controlcenter.constrainmod(uConstrain(pointA=uPoint(x = new_constraint.pointA.x, y = new_constraint.pointB.y), pointB=uPoint(x = new_constraint.pointB.x, y = new_constraint.pointB.y + __CCENTERSIZE__ * __CLUSTERRESOLUTION__)))
            else:
                #Set CCenter Constraint
                button_shrinking_factor = 0.3
                self.controlcenterOpenButton.constrainmod(uConstrain(pointA = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ - 1) / (2) - (__CLUSTERRESOLUTION__ * button_shrinking_factor)),pointB = uPoint(new_constraint.pointB.x - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__  + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor), new_constraint.pointB.y - __CLUSTERRESOLUTION__ * (__CCENTERSIZE__ + 1) / (2) + (__CLUSTERRESOLUTION__ * button_shrinking_factor))))
                self.controlcenter.constrainmod(uConstrain(pointA=uPoint(x = new_constraint.pointA.x, y = new_constraint.pointB.y - __CCENTERSIZE__ * __CLUSTERRESOLUTION__), pointB=uPoint(x = new_constraint.pointB.x, y = new_constraint.pointB.y)))
                #Set Widget Constraint
                return self.child.constrainmod(uConstrain(pointA = self.anchor, pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height - __CLUSTERRESOLUTION__ * __CCENTERSIZE__)))
        self.childs_constraint = new_constraint.copy
        self.child.constrainmod(new_constraint.copy)
        if self.popup != None:
            settings_constraint = new_constraint.copy
            settings_constraint.pointA.x += __CLUSTERRESOLUTION__
            settings_constraint.pointA.y += __CLUSTERRESOLUTION__
            settings_constraint.pointB.x -= __CLUSTERRESOLUTION__
            self.popup.constrainmod(settings_constraint.copy)
            

    @tlog
    def miscmod(self):
        return self.child.miscmod()

    @tlog
    def draw(self):
        outlist = []            
        background_call = udraw_Rectangle(pointA=self.anchor, pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height), filled=True, border_is_highlight=False, fill_match_border=True)
        #list.append(background_call)
        child_calls : list = self.child.draw()
        for call in child_calls:
            outlist.append(call)    
        __HEADERSIZE__ : int = NotifyService.get("debug.widget-header_thickness_in_clusters")
        __CLUSTERRESOLUTION__ : int = NotifyService.get("debug.display-cluster_resolution")
        if self.header == "t":
            headerconsts = uConstrain(pointA=uPoint(x=self.anchor.x, y = self.anchor.y), pointB=uPoint(x = self.anchor.x + self.width, y = self.anchor.y + __CLUSTERRESOLUTION__ * __HEADERSIZE__))
        elif self.header == "l":
            headerconsts = uConstrain(pointA=uPoint(x=self.anchor.x ,y = self.anchor.y), pointB=uPoint(x = self.anchor.x + __CLUSTERRESOLUTION__ * __HEADERSIZE__, y = self.anchor.y + self.height))
        elif self.header == "r":
            headerconsts = uConstrain(pointA = uPoint(x = self.anchor.x + self.width - __CLUSTERRESOLUTION__ * __HEADERSIZE__, y = self.anchor.y), pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        elif self.header == "b":
            headerconsts = uConstrain(pointA = uPoint(x = self.anchor.x, y = self.anchor.y + self.height - __CLUSTERRESOLUTION__ * __HEADERSIZE__), pointB = uPoint(x = self.anchor.x + self.width, y = self.anchor.y + self.height))
        if self.header != None:
            self.headerText = uTOUCHAREA(
                level=1,
                parentwidget=self.parentwidget,
                funcname="Header",
                child = uLABEL(varname = self.headercontent, nice = True, highlight=False))
            self.headerText.constrainmod(headerconsts.copy)
            headertextcalls = self.headerText.draw()
            if self.headershape == "poly":
                outlist.append(udraw_Polygon(pointA=headerconsts.pointA, pointB = uPoint(x = headerconsts.pointA.x + __CLUSTERRESOLUTION__ * __HEADERSIZE__, y = headerconsts.pointA.y + headerconsts.height), pointC = uPoint(headerconsts.pointB.x - __CLUSTERRESOLUTION__ * __HEADERSIZE__, y = headerconsts.pointA.y + headerconsts.height), pointD = uPoint(x = headerconsts.pointA.x + headerconsts.width, y = headerconsts.pointA.y), border_is_highlight=True, filled = True, fill_match_border=True,thickness = 1)) 
            else:
                outlist.append(udraw_Rectangle(pointA=headerconsts.pointA, pointB=headerconsts.pointB, border_is_highlight=True, filled = True, fill_match_border=True))
            for htcall in headertextcalls:
                outlist.append(htcall)
        controlcenterbuttoncalls = self.controlcenterOpenButton.draw()
        controlcentercalls = self.controlcenter.draw() if self.controlcenter != None else []
        popupcalls = self.popup.draw() if self.popup != None else []
        for call in controlcentercalls:
            outlist.append(call)
        for call in controlcenterbuttoncalls:
            outlist.append(call)
        for call in popupcalls:
            outlist.append(call)
        
        return outlist