from windowhandler import DISPLAY
from layout_parts.Widgets.uNodes.unode_util.decorators import tlog
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from graphics import Rectangle
from rounded_rectangle import RoundedRectangle
import datetime
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *

class OS():
    def __init__(self):
        #Initialize big size Window
        self.displayController = DISPLAY()
        get_weeks_earliest_and_latest_time()
        self.displayController.load_layout("Preset Layout 1")
        self.get_timing()
        currently_drawn_calls = self.draw()
        while True:
            print("quit; layout; empty -> reload Widgets on Display; cache;")
            command = input()
            if command == "quit":
                exit()
            elif command == "layout":
                self.displayController.load_layout("Preset Layout 1")
            elif command == "cache":
                NotifyService.reloadcache()
            else:
                for call in currently_drawn_calls:
                    call.undraw()
                self.draw()
    @tlog
    def get_timing(self):
        date = datetime.date.today()
        year = date.year
        month = date.month
        day = date.day
        daytime = datetime.datetime.now()
        hour = daytime.hour
        minute = daytime.minute
        
        NotifyService.dumpchange(filename = "timing", changes = {
            "date_day" : day,
            "date_month" : month,
            "date_year" : year,
            "time_hour" : hour,
            "time_minute" : minute,
            "weekday" : date.weekday()
        })
        



    @tlog
    def draw(self):
        display = self.displayController
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
                if rectangle.rounding > 0:
                    obj = RoundedRectangle(p1 = rectangle.pointA.to_point(), p2 = rectangle.pointB.to_point(), radius=rectangle.rounding)
                else:
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
            elif draw_call.__class__.__name__ == "udraw_Line":
                line : udraw_Line = draw_call
                if line.pointA.x == line.pointB.x:
                    obj = Rectangle(p1=Point(x = line.pointA.x - line.thickness / 2, y = line.pointA.y), p2=Point(x = line.pointA.x + line.thickness / 2, y = line.pointB.y))
                elif line.pointA.y == line.pointB.y:
                    obj = Rectangle(p1=Point(x = line.pointA.x, y = line.pointA.y - line.thickness / 2), p2=Point(x = line.pointB.x, y = line.pointA.y + line.thickness / 2))
                if line.highlight:
                    obj.setOutline(color = highlight_color)
                    obj.setFill(color= highlight_color)
                else:
                    obj.setOutline(color = background_color)
                    obj.setFill(color = background_color)
                obj.draw(display.wallpaper)
                drawobjs.append(obj)
            elif draw_call.__class__.__name__ == "udraw_Text":
                txt : udraw_Text = draw_call
                obj = Text(txt.anchorpoint.to_point(), txt.textString)
                obj.setSize(txt.size)
                obj.setFace("courier")
                obj.setTextColor(highlight_color if txt.highlight else background_color)
                obj.draw(display.wallpaper)
                drawobjs.append(obj)
            elif draw_call.__class__.__name__ == "udraw_Polygon":
                call : udraw_Polygon = draw_call
                obj = Polygon([call.pointA.to_point(), call.pointB.to_point(), call.pointC.to_point(), call.pointD.to_point()])
                if call.border_is_highlight:
                    obj.setOutline(highlight_color)
                if call.filled:
                    if call.fill_border and call.border_is_highlight:
                        obj.setFill(highlight_color)
                    elif call.fill_border and not call.border_is_highlight:
                        obj.setFill(background_color)
                    elif not call.fill_border and call.border_is_highlight:
                        obj.setFill(background_color)
                    else:
                        obj.setFill(highlight_color)
                obj.draw(display.wallpaper)

            
        if NotifyService.get("debug.widget-draw_constraints"):
            for call in constraints:
                call.setOutline(color=NotifyService.get("debug.widget-constraint_color"))
                call.draw(display.wallpaper)
                drawobjs.append(call)
        print(">>>(Re)Drawn Display", end="")
        for widget in display.currently_loaded_widgets:
            widget.constraincheck()
        return drawobjs

setattr(NotifyService, "os", OS())

