from debugwindowhandler import DISPLAY
from layout_parts.Widgets.uNodes.unode_util.udrawcalls import *
from notifier import NotifyService
from graphics import Rectangle

def draw(display : DISPLAY):
    drawcalls = []
    for widget in displayController.currently_loaded_widgets:
        for single_call in widget.drawcalls:
            drawcalls.append(single_call)
    isDarkMode = NotifyService.get("user.darkmode")
    highlight_color = "white" if isDarkMode else "black"
    background_color = "black" if isDarkMode else "white"
    print("main.py" + str(drawcalls))
    for draw_call in drawcalls:
        print(draw_call.__class__.__name__)
        if draw_call.__class__.__name__ == "udraw_Pixel":
            pixel_to_draw : udraw_Pixel = draw_call
            display.wallpaper.plotPixel(x = pixel_to_draw.position.x, y = pixel_to_draw.position.y, color = highlight_color if draw_call.highlight else background_color)
        elif draw_call.__class__.__name__ == "udraw_Rectangle":
            rectangle : udraw_Rectangle = draw_call
            obj = Rectangle(p1 = Point(x = rectangle.pointA.x, y = rectangle.pointA.y), p2 = Point(x = rectangle.pointB.x, y = rectangle.pointB.y))
            if rectangle.is_debug:
                obj.setOutline(NotifyService.get("debug.widget-constraint-color"))
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
            obj.draw(display.wallpaper)
            


#Initialize big size Window
displayController = DISPLAY()
input()
displayController.load_layout("Preset Layout 1")
input()
draw(display=displayController)
input()
