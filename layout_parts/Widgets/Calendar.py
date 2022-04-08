from calendar import Calendar
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uCollectives import *
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *


body = uCOLUMN(
    divider_thickness=3,
    children=[
        uROW(
            flex = 1,
            divider_thickness = 0,
            children = [
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 0 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 0 else 100,
                    child=uCARD(
                        rounding = 10 if NotifyService.get("timing.weekday") != 0 else 0,
                        child=uLABEL("MO", highlight=False))
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 1 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 1 else 100,
                    child=uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 1 else 0,
                        child=uLABEL("DI", highlight=False))
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 2 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 2 else 100,
                    child=uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 2 else 0,
                        child=uLABEL("MI", highlight=False))
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 3 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 3 else 100,
                    child = uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 3 else 0,
                        child=uLABEL("DO", highlight=False)),
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 4 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 4 else 100,
                    child=uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 4 else 0,
                        child=uLABEL("FR", highlight=False))
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 5 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 5 else 100,
                    child=uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 5 else 0,
                        child=uLABEL("SA", highlight=False))
                ),
                uPBOX(
                    modV=60 if NotifyService.get("timing.weekday") != 6 else 100,
                    modH=60 if NotifyService.get("timing.weekday") != 6 else 100,
                    child=uCARD(
                        rounding=10 if NotifyService.get("timing.weekday") != 6 else 0,
                        child=uLABEL("SO", highlight=False))
                )
                
            ]
        ),
        uROW(
            flex = 7,
            include_sides = True,
            divider_thickness = 3,
            children=[
                uPBOX(
                    modH = 90,
                    child = uCOLUMN(
                    children= CalendarEntrys(get_date_based_on_weekday(0))
                )),
                uPBOX(
                    modH=90,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(1))
                )),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(2))

                     )),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(3))

                     )
                ),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(4))
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(5))
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(6))
                    )),
            ]
        )
    ]
)

