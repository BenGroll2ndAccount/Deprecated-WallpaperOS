from layout_parts.Widgets.WIDGET import WIDGET
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
        self.get_timing()
        NotifyService.subscribe_to_event(self, "redraw")
        NotifyService.subscribe_to_event(self, "reload_layout")
        get_weeks_earliest_and_latest_time()
        self.displayController.load_layout("Preset Layout 1")
        self.currently_drawn_calls = self.drawAll()
        NotifyService.subscribe_to_keyboard(self)
        NotifyService.startkeyboardlistening(self)
    
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
    def redraw(self, widgetname = None):
        if widgetname == None:
            for widget in self.currently_drawn_calls.keys():
                for call in self.currently_drawn_calls[widget]:
                    call.undraw()
            self.currently_drawn_calls = self.drawAll()
        else:
            for call in self.currently_drawn_calls[widgetname]:
                call.undraw()
            self.currently_drawn_calls[widgetname] = []
            widget_to_redraw : WIDGET
            for widget in self.displayController.currently_loaded_widgets:
                if widget.widgetname == widgetname:
                    widget_to_redraw = widget
            new_draw_objs = self.draw(widget_to_redraw)
            self.currently_drawn_calls[widgetname] = new_draw_objs


    @tlog
    def calls2objs(self, drawcalls):
        isDarkMode = NotifyService.get("user.darkmode")
        light_color = NotifyService.get("debug.display-light_color")
        dark_color = NotifyService.get("debug.display-dark_color")
        highlight_color = light_color if isDarkMode else dark_color
        background_color = dark_color if isDarkMode else light_color
        constraints = []
        touch_areas = []
        drawobjs = []
        display = self.displayController
        for draw_call in drawcalls:
            if draw_call.__class__.__name__ == "udraw_Circle":
                circle_to_draw : udraw_Circle = draw_call
                obj = Circle(circle_to_draw.point, circle_to_draw.radius)
                if circle_to_draw.highlight:
                    obj.setOutline(color = highlight_color)
                    if circle_to_draw.filled:
                        obj.setFill(highlight_color if circle_to_draw.fill_border else background_color)
                else:
                    obj.setOutline(color = background_color)
                    if circle_to_draw.filled:
                        obj.setFill(background_color if circle_to_draw.fill_border else highlight_color)
                obj.setWidth(circle_to_draw.thickness)
                drawobjs.append(obj)
            if draw_call.__class__.__name__ == "udraw_Pixel":
                pixel_to_draw : udraw_Pixel = draw_call
                display.wallpaper.plotPixel(x = pixel_to_draw.position.x, y = pixel_to_draw.position.y, color = highlight_color if draw_call.highlight else background_color)
            elif draw_call.__class__.__name__ == "udraw_Rectangle":
                rectangle : udraw_Rectangle = draw_call
                if rectangle.rounding > 0:
                    obj = RoundedRectangle(p1 = rectangle.pointA.to_point(), p2 = rectangle.pointB.to_point(), radius=rectangle.rounding)
                else:
                    obj = Rectangle(p1 = Point(x = rectangle.pointA.x, y = rectangle.pointA.y), p2 = Point(x = rectangle.pointB.x, y = rectangle.pointB.y))
                if rectangle.filled:
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
                if rectangle.is_debug:
                    obj.setOutline(color=NotifyService.get("debug.widget-constraint_color"))
                    constraints.append(obj)
                elif rectangle.is_touch_debug:
                    obj.setOutline(color=NotifyService.get("debug.widget-toucharea_color"))
                    touch_areas.append(obj)
                else:
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
                drawobjs.append(obj)
            elif draw_call.__class__.__name__ == "udraw_Text":
                txt : udraw_Text = draw_call
                obj = Text(txt.anchorpoint.to_point(), txt.textString)
                obj.setSize(txt.size)
                obj.setFace("courier")
                obj.setTextColor(highlight_color if txt.highlight else background_color)
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
                drawobjs.append(obj)
        return {"constraints" : constraints, "objs" : drawobjs, "touch" : touch_areas}

    @tlog
    def notify_Event_redraw(self, *args):
        self.redraw(args[0] if len(args) > 0 else None)

    @tlog
    def notify_Event_reload_layout(self):
        self.displayController.load_layout(NotifyService.get("ram.currently_loaded_layout"))

    @tlog
    def notify_Keyboard(self, key):
        if key == "q":
            exit()
        elif key == "l":
            self.displayController.load_layout("Preset Layout 1")
        elif key == "c":
            NotifyService.reloadcache()
        elif key == "t":
            for widget in self.displayController.currently_loaded_widgets:
                widget.output()    
        elif key == "d":
            self.notify_Event_redraw()
    
    
    @tlog
    def draw(self, widget):
        display = self.displayController
        drawobjs = self.calls2objs(widget.drawcalls)
        drawobjlist = []
        for obj in drawobjs["objs"]:
            obj.draw(display.wallpaper)
            drawobjlist.append(obj)
        for obj in drawobjs["constraints"]:
            obj.draw(display.wallpaper)
            drawobjlist.append(obj)
        for obj in drawobjs["touch"]:
            obj.draw(display.wallpaper)
            drawobjlist.append(obj)
        widget.constraincheck()
        return drawobjlist

    @tlog
    def drawAll(self):
        drawcalls = {}
        for widget in self.displayController.currently_loaded_widgets:
            drawcalls[widget.widgetname] = self.draw(widget)
        return drawcalls

setattr(NotifyService, "os", OS())
