import graphics


class RoundedRectangle(graphics._BBox):
    """
    Draws a rectangle with rounded corners.
    Based on https://wiki.tcl.tk/1416

    Using the given corners and radius,
    calculates the vertices of a polygon equivalent to a rounded rectangle,
    and then uses a Tk/Tcl (?) function to draw the polygon smoothly.

    Parameters:
        p1: upper left corner of the rectangle
        p2: lower right corner of the rectangle
        radius: size of the corners (max: 3/8 the size of the smallest side)
    """
    def __init__(self, p1: graphics.Point, p2: graphics.Point, radius: int):
        super().__init__(p1, p2)
        self.radius = radius

    def __repr__(self):
        return "RoundedRectangle({}, {}, r={})".format(self.p1, self.p2, self.radius)

    def _draw(self, canvas: graphics.GraphWin, options: dict):
        #print(type(canvas), type(options))
        # Converts the corner coordinates to (real) screen pixel values
        x1, y1 = canvas.toScreen(self.p1.x, self.p1.y)
        x2, y2 = canvas.toScreen(self.p2.x, self.p2.y)

        # Arguments passed to tkinter.Canvas.
        # Starting with the canvas that's being used.
        args = [canvas]

        diameter = 2 * self.radius

        # The radius can have at most 3/8 the size of the smallest side of the
        # rectangle, due to a limitation ok Tk/Tcl.
        # 2 * (3/8) = 6/8 = 3/4 = 0.75
        # (I haven't understood this part very well)
        maxr = 0.75
        if diameter > (maxr * (x2 - x1)):
            diameter = maxr * (x2 - x1)
        if diameter > (maxr * (y2 - y1)):
            diameter = maxr * (y2 - y1)

        # Calculates 12 points that outline the rectangle,
        # off of the two given corners.
        #
        # A---c--------c---B \
        # |                |  } diameter
        # c                c /
        # |                |
        # |                |
        # |                |
        # c                c \
        # |                |  } diameter
        # B---c--------c---A /
        # Caption:
        # A - the two given corners
        # B - the other two corners
        # c - guide points for the Tk/Tcl smoothing process
        #
        # An example of how a corner will be drawn:
        #
        #               |                         |
        #               |                         |
        #               c                         c
        #               |                        _`
        #               |     =>                /
        #               |                   __``
        # ----c---------A           ----c```      A
        #
        a1 = x1 + diameter
        a2 = x2 - diameter
        b1 = y1 + diameter
        b2 = y2 - diameter
        args.extend([
            x1, y1,  # A1
            a1, y1,  # c1
            a2, y1,  # c2
            x2, y1,  # B1
            x2, b1,  # c3
            x2, b2,  # c4
            x2, y2,  # A2
            a2, y2,  # c5
            a1, y2,  # c6
            x1, y2,  # B2
            x1, b2,  # c7
            x1, b1,  # c8
            '-smooth', '1'
        ])
        # The '-smooth 1' command activates the smoothing mode,
        # which is critical for the rounded corners to appear.

        # Other options inherited from graphics or from tkinter.Canvas
        args.append(options)

        return graphics.GraphWin.create_polygon(*args)

    def clone(self):
        other = RoundedRectangle(self.p1, self.p2, self.radius)
        other.config = self.config.copy()
        return other
