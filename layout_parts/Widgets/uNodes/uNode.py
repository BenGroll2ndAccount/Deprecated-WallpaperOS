from notifier import NotifyService
from abc import abstractmethod
from layout_parts.Widgets.uNodes.unode_util.helperclasses import *
from layout_parts.Widgets.uNodes.unode_util.uexceptions import *
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *

class uNODE():
    def __node_init__(self, listening : list, level : int = 0):
        self.level = level
        if listening != None:
            NotifyService.addListener(self, names=listening)

    def assign_depth(self, value):
        self.depth = value
        if hasattr(self, "child") and self.child != None:
            self.child.assign_depth(self.depth + 1)
        elif hasattr(self, "children") and self.children != None:
            ready = [child.assign_depth(value + 1) for child in self.children]
            return
        return

    def printChild(self):
        print(self.child)
        if hasattr(self, "child") and self.child != None:
            self.child.printChild()
        if hasattr(self, "children") and self.children != None:
            for child in self.children:
                child.printChild()

    def output(self):
        constraintoutput = self.constraint.out()
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (100 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth) + "-" + str(self.level) + "   " + constraintoutput )
        if not hasattr(self, "child") and not hasattr(self, "children"):
            return
        if hasattr(self, "child") and self.child != None:
            return self.child.output()
        if hasattr(self, "children") and self.children != None:
            for child in self.children:
                wait = child.output()
            return
        

    @abstractmethod
    def notify(self, name, value):
        pass

    @abstractmethod
    def constrainmod(self, value):
        pass

    @abstractmethod
    def passWidgetData(self, data : dict):
        self.widgetData = data.copy()
        if hasattr(self, "child") and self.child != None:
            self.child.passWidgetData(data.copy())
            return
        elif hasattr(self, "children") and self.children != None:
            for child in self.children:
                child.passWidgetData(data.copy())
            return
        else:
            return

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def __init__(self):
        pass

    def constraincheck(self, parent_const, parent_level):
        if self.level <= parent_level:
            if self.constraint.isSafe(parent_const, self.__class__.__name__):
                if hasattr(self, "child") and self.child != None:
                    return self.child.constraincheck(self.constraint, self.level)
                if hasattr(self, "children") and self.children != None:
                    for child in self.children:
                        child.constraincheck(self.constraint, self.level)
                    return
        else:
            if hasattr(self, "child") and self.child != None:
                return self.child.constraincheck(self.constraint)
            if hasattr(self, "children") and self.children != None:
                for child in self.children:
                    child.constraincheck(self.constraint, self.level)
                return


