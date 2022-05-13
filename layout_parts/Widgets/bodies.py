from tkinter import Label

from matplotlib.pyplot import fill
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uDot import uDOT
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uRect import uRECT
from layout_parts.Widgets.uNodes.uBuilders import *
from layout_parts.Widgets.uNodes.unode_util.helperfunctions import *

class BODIES():
    def ControlCenterOpenButton(parentwidget):
        return uTOUCHAREA( 
            level = 1,
            parentwidget=parentwidget,
            funcname="CCenter",
            child = uDOT(
            filled=True,
            thickness=1,
            highlight=True,
            fill_match_border=False,
            
        ))
    def ControlCenterCalendarClosed(parentwidget):
        return uEMPTY()

    def ControlCenterCalendarBase(parentwidget):
        return uCARD(
            thickness=4,
            filled = True,
            fill_match_border=False,
            highlight=True,
            child=uPBOX(
                modV = 80,
                modH = 70,
                hAlign="start",
                child = uROW(
                    children=[uEMPTY(),BODIES.ControlCenterOpenSettingsButton(parentwidget)],

                )
            )
        )

    def ControlCenterOpenSettingsButton(parentwidget):
        return uRECT(
            child = uTOUCHAREA(
            level=1,
            parentwidget=parentwidget,
            funcname="CCenterOpenSettings",
            child = uCARD(
                filled = False,
                thickness = 4,
                rounding = 5,
                highlight = True,
                child=uPBOX(
                    modH=99,
                    modV=99,
                    child=uLABEL("Settings")
                    )
                )
            )
        )

    def ControlCenterSettingsPanel(parentwidget, dummy):
        print(parentwidget)
        return uCARD(
            filled=True,
            thickness=4,
            rounding = 5,
            fill_match_border=False,
            highlight=True,
            child=uCOLUMN(
                divider_thickness=4,
                include_sides=True,
                children=[
                    uPBOX(
                        modH = 95,
                        modV = 95,
                        child = uROW(
                        divider_thickness=4,
                        children=[
                            uPBOX(
                                modH = 90,
                                modV = 92,
                                child = uTOUCHAREA(
                                level = 3,
                                flex = 3,
                                parentwidget=parentwidget,
                                funcname="SETTINGS.Saved",
                                child=uCARD(
                                    filled = True,
                                    fill_match_border=True,
                                    highlight=True,
                                    rounding = 5,
                                    child = uLABEL("SAVE", highlight = False)
                                ))
                            ),
                            uEMPTY(flex = 2),
                            uROW(
                                flex = 3,
                                children = [
                                    uPBOX(
                                        modH = 60,
                                        modV = 60,
                                        flex = 0.3,
                                        child = uTOUCHAREA(
                                            level = 3,                               
                                            parentwidget=parentwidget,
                                            funcname="SETTINGS.PAGEBWD",
                                            child = uDOT(filled = False, fill_match_border=False, highlight = True, thickness=2)
                                            )
                                        ),
                                    uLABEL(varname = "Page 0 / 0" if dummy else "PAGE " + str(parentwidget.ccenterSettingsPanel.current_page) + " / " + str(parentwidget.ccenterSettingsPanel.total_pages)),
                                    uPBOX(
                                        modH = 60,
                                        modV = 60,
                                        flex = 0.3,
                                        child = uTOUCHAREA(
                                            level = 3,                               
                                            parentwidget=parentwidget,
                                            funcname="SETTINGS.PAGEFWD",
                                            child = uDOT(filled = False, fill_match_border=False, highlight = True, thickness=2)
                                            )
                                        ),
                            ]),
                            uEMPTY(flex = 2),
                            uTOUCHAREA(
                                flex = 0.5,
                                parentwidget = parentwidget,
                                funcname = "SETTINGS.DISCARD",
                                child = uCARD(
                                thickness = 4,
                                rounding = 0,
                                filled = True,
                                fill_match_border=True,
                                highlight=True
                            ))
                        ]
                    )
                    ),
                    
                    uEMPTY(flex = 8)
                ]
            )
        )
    
    

    def Calendar(parentwidget):
        return uCOLUMN(
        divider_thickness=3,
        children=[
            uCOLUMN(
                children = [
                    uROW(
                flex = 1,
                divider_thickness = 0,
                children = [
                        uCOLUMN(
                        children = [uPBOX(
                        modV=80 if NotifyService.get("timing.weekday") != 0 else 100,
                        modH=80 if NotifyService.get("timing.weekday") != 0 else 100,
                        flex = 2,
                        child=uCARD(
                            rounding = 10 if NotifyService.get("timing.weekday") != 0 else 0,
                            child=uLABEL("MO", highlight=False))
                    ),
                    uLABEL(get_date_based_on_weekday(0).split("-")[2] + "." + get_date_based_on_weekday(0).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]),
                    uCOLUMN(
                        children = [uPBOX(
                            flex = 2,
                        modV=80 if NotifyService.get("timing.weekday") != 1 else 100,
                        modH=80 if NotifyService.get("timing.weekday") != 1 else 100,
                        child=uCARD(
                            rounding=10 if NotifyService.get("timing.weekday") != 1 else 0,
                            child=uLABEL("DI", highlight=False))
                    ),
                    uLABEL(get_date_based_on_weekday(1).split("-")[2] + "." + get_date_based_on_weekday(1).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]),
                    uCOLUMN(
                        children = [uPBOX(
                            flex = 2,
                            modV=80 if NotifyService.get("timing.weekday") != 2 else 100,
                            modH=80 if NotifyService.get("timing.weekday") != 2 else 100,
                            child=uCARD(
                                rounding=10 if NotifyService.get("timing.weekday") != 2 else 0,
                                child=uLABEL("MI", highlight=False)
                                )
                            ),
                    uLABEL(get_date_based_on_weekday(2).split("-")[2] + "." + get_date_based_on_weekday(2).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]),
                    uCOLUMN(
                        children = [uPBOX(
                            flex = 2,
                        modV=80 if NotifyService.get("timing.weekday") != 3 else 100,
                        modH=80 if NotifyService.get("timing.weekday") != 3 else 100,
                        child = uCARD(
                            rounding=10 if NotifyService.get("timing.weekday") != 3 else 0,
                            child=uLABEL("DO", highlight=False)),
                    ),
                    uLABEL(get_date_based_on_weekday(3).split("-")[2] + "." + get_date_based_on_weekday(3).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]),
                    uCOLUMN(
                        children = [uPBOX(
                            flex = 2,
                            modV=80 if NotifyService.get("timing.weekday") != 4 else 100,
                            modH=80 if NotifyService.get("timing.weekday") != 4 else 100,
                            child=uCARD(
                                    rounding=10 if NotifyService.get("timing.weekday") != 4 else 0,
                            child=uLABEL("FR", highlight=False))
                        ),
                        uLABEL(get_date_based_on_weekday(4).split("-")[2] + "." + get_date_based_on_weekday(4).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                        ]),
                        uCOLUMN(
                            children = [uPBOX(
                                flex = 2,
                                modV=80 if NotifyService.get("timing.weekday") != 5 else 100,
                                modH=80 if NotifyService.get("timing.weekday") != 5 else 100,
                                child=uCARD(
                                rounding=10 if NotifyService.get("timing.weekday") != 5 else 0,
                                child=uLABEL("SA", highlight=False))
                    ),
                    uLABEL(get_date_based_on_weekday(5).split("-")[2] + "." + get_date_based_on_weekday(5).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]),
                    uCOLUMN(
                        children = [uPBOX(
                            flex = 2,
                        modV=80 if NotifyService.get("timing.weekday") != 6 else 100,
                        modH=80 if NotifyService.get("timing.weekday") != 6 else 100,
                        child=uCARD(
                            rounding=10 if NotifyService.get("timing.weekday") != 6 else 0,
                            child=uLABEL("SO", highlight=False))
                    ),
                    uLABEL(get_date_based_on_weekday(6).split("-")[2] + "." + get_date_based_on_weekday(6).split("-")[1]) if parentwidget.settings["show-dates"] else uEMPTY(flex = 0)
                    ]
        ),
        ]),
        ]),
        uROW(
            flex = 7,
            include_sides = True,
            divider_thickness = 3,
            children=[
                uPBOX(
                    modH = 90,
                    child = uCOLUMN(
                    children= CalendarEntrys(get_date_based_on_weekday(0), parentwidget)
                )),
                uPBOX(
                    modH=90,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(1), parentwidget)
                )),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(2), parentwidget)

                     )),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(3), parentwidget)

                     )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(4), parentwidget)
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = CalendarEntrys(get_date_based_on_weekday(5), parentwidget)
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                        children = CalendarEntrys(get_date_based_on_weekday(6), parentwidget)
                    )),
                        ]
                    )
                ]
            )
    def TODOs(settings):
        return uLABEL("jzgfjzgc")

    
