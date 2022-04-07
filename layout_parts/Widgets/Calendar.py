from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY
from layout_parts.Widgets.uNodes.uCollectives import *

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
                    divider_thickness = 0,
                    seperator=10,
                    children=[
                        uEMPTY(flex = 4),
                        uLABEL("12:30"),
                        uCARD(
                            thickness = 3,
                            rounding = 7,
                            flex = 4.5,
                            filled = False,child=uCOLUMN(
                            divider_thickness = 0,
                            children=[
                                uLABEL("FAHR-"),
                                uLABEL("SCHULE")
                                ]
                            )
                        ),
                        
                        uLABEL("17:00"),
                        uEMPTY(flex = 1.5),
                        uLABEL("19:30"),
                        uCARD(
                            flex = 1.5,
                            thickness = 3,
                            rounding = 7,
                            filled = False, highlight=True,
                            child=uCOLUMN(
                                children = [
                                uLABEL("GESPRÄCH"),
                                uLABEL("MIT"),
                                uLABEL("THOMAS")
                                ]
                            )
                        ),
                        uLABEL("21:00")
                        
                    ]
                )),
                uCOLUMN(
                    children = [
                        uPBOX(
                            flex = 14,
                            modH = 90,
                            child=uCOLUMN(
                                divider_thickness=0,
                                children = [
                                    uEMPTY(flex = 0.5),
                                    uLABEL("7:30", flex = 0.5),
                                    uCARD(
                                        flex = 12,
                                        filled = False,
                                        thickness=3,
                                        rounding=7,
                                        child=uCOLUMN(
                                            children=[
                                                uLABEL("WANDER-"),
                                                uLABEL("UND"),
                                                uLABEL("MIT"),
                                                uLABEL("FAMILIE")
                                            ]
                                        )
                                    ),
                                    uLABEL("19:47"),
                                    uEMPTY(flex = 0.5),

                                    ]
                            )
                        )
                    ]
                ),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = CalendarEntrys("07.04.2022")

                     )),
                uPBOX(
                    modH=95,
                    child = uCOLUMN(
                        children = [
                            uEMPTY(1.5),
                            uLABEL("9:30"),
                            uCARD(
                                thickness = 3,
                                rounding = 7,
                                filled = False,
                                flex = 3,
                                child = uPBOX(
                                    modH=90,
                                    modV=90,
                                    child = uCOLUMN(
                                        children = [
                                            uLABEL("MITARBEITER-"),
                                            uLABEL("FORTBILDUNG")
                                        ]
                                    )
                                )
                            ),
                            uLABEL("12:30"),
                            uEMPTY(flex = 2),
                            uLABEL("16:30"),
                            uCARD(
                                thickness = 3,
                                rounding = 7,
                                flex = 1,
                                filled = False,
                                child = uCOLUMN(
                                    children=[
                                        uLABEL("BRIEFE"),
                                        uLABEL("DHL"),
                                    ]
                                )
                            ),
                            uLABEL("17:30"),
                            uEMPTY(flex = 2.5)

                        ]

                     )
                ),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = [
                        uLABEL("7:00"),
                        uCARD(
                            filled = False,
                            thickness = 3,
                            highlight=True,
                            rounding=7,
                            flex=2.5,
                            child = uCOLUMN(
                                [
                                    uLABEL("MORGEN"),
                                    uLABEL("WORKOUT")
                             ])
                        ),
                        uLABEL("9:30"),
                        uEMPTY(flex = 2),
                        uLABEL("14:30"),
                        uCARD(
                            thickness = 3,
                            filled = False,
                            highlight=True,
                            rounding = 7,
                            flex = 4,
                            child = uCOLUMN(
                                [
                                    uLABEL("MEETING"),
                                    uLABEL("MIT"),
                                    uLABEL("ANDREAS")
                                ]
                            )
                        ),
                        uLABEL("18:30"),
                        uEMPTY(flex = 1.5)
                    ]
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    [
                        uEMPTY(flex=15),
                        uLABEL("20:30"),
                        uCARD(
                            thickness = 3,
                            flex = 2,
                            filled = False,
                            highlight=True,
                            rounding = 7,
                            child=uCOLUMN(
                                [
                                    uLABEL("PARTY"),
                                    uLABEL("VIVI")
                                ]
                            )
                        ),
                    ]
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                        children = [
                            uEMPTY(flex = 2),
                            uLABEL("10:30"),
                            uCARD(
                                thickness = 3,
                                rounding = 7,
                                flex = 4,
                                filled = False,
                                highlight=True,
                                child = uCOLUMN(
                                    children = [
                                        uLABEL("BRUNCH"),
                                        uEMPTY(flex=4)
                                        ],
                                        
                                )
                            ),
                            uLABEL("14:30"),
                            uEMPTY(flex = 5)
                        ]
                    )),
            ]
        )
    ]
)
