from re import T
from debugwindowhandler import DISPLAY
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from graphics import Rectangle
import time
from elapsed import *



class OS():
    def __init__(self):
        #Initialize big size Window
        self.displayController = DISPLAY()
        self.displayController.load_layout("Preset Layout 1")
        currently_drawn_calls = self.draw()
        while True:
            print("q -> quit; l -> reload Layout; empty -> reload Widgets on Display")
            lol = input()
            if lol == "q":
                exit()
            elif lol == "l":
                self.displayController.load_layout("Preset Layout 1")
            else:
                for call in currently_drawn_calls:
                    call.undraw()
                self.draw()
    
    def draw(self):
        display = self.displayController
        t = time.time()
        drawcalls = []
        drawobjs = []
        for widget in display.currently_loaded_widgets:
            for single_call in widget.drawcalls:
                drawcalls.append(single_call)
        isDarkMode = NotifyService.get("user.darkmode")
        light_color = NotifyService.get("debug.display-light_color")
        dark_color = NotifyService.get("debug.display-dark_color")
        highlight_color = light_color if isDarkMode else dark_color
        background_color = dark_color if isDarkMode else light_color
        constraints = []
        for draw_call in drawcalls:
            if draw_call.__class__.__name__ == "udraw_Pixel":
                pixel_to_draw : udraw_Pixel = draw_call
                display.wallpaper.plotPixel(x = pixel_to_draw.position.x, y = pixel_to_draw.position.y, color = highlight_color if draw_call.highlight else background_color)
            elif draw_call.__class__.__name__ == "udraw_Rectangle":
                rectangle : udraw_Rectangle = draw_call
                obj = Rectangle(p1 = Point(x = rectangle.pointA.x, y = rectangle.pointA.y), p2 = Point(x = rectangle.pointB.x, y = rectangle.pointB.y))
                if rectangle.is_debug:
                    constraints.append(obj)
                elif rectangle.filled:
                    if rectangle.border_is_highlight and rectangle.fill_border:
                        obj.setOutline(color=highlight_color)
                        obj.setFill(color=highlight_color)
                    elif rectangle.border_is_highlight and not rectangle.fill_border:
                        obj.setOutline(color=highlight_color)
                        obj.setFill(color=background_color)
                    elif not rectangle.border_is_highlight and not rectangle.fill_border:
                        obj.setOutline(color=background_color)
                        obj.setFill(color=highlight_color)
                    else:
                        obj.setFill(background_color)
                        obj.setOutline(background_color)
                obj.setWidth(rectangle.thickness)
                if not rectangle.is_debug:
                    obj.draw(display.wallpaper)
                drawobjs.append(obj)
        if NotifyService.get("debug.widget-draw_constraints"):
            for call in constraints:
                call.setOutline(color=NotifyService.get("debug.widget-constraint_color"))
                call.draw(display.wallpaper)
                drawobjs.append(call)
        print(">>>(Re)Drawn Display", end="")
        elapsedtime(t)
        return drawobjs

setattr(NotifyService, "os", OS())

