from textwrap import fill
from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL
from layout_parts.Widgets.uNodes.uEmpty import uEMPTY

body = uCOLUMN(
    divider_thickness=3,
    children=[
        uROW(
            flex = 1,
            divider_thickness = 0,
            children = [
                #uPBOX(
                #    modV=60,
                #    modH=60,
                #    child=uCARD(rounding=10,child=uLABEL("MO", highlight=False))
                #),
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("DI", highlight=False))
                ),
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("MI", highlight=False))
                ),
                uCARD(rounding=0,child=uLABEL("DO", highlight=False)),
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("FR", highlight=False))
                ),
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("SA", highlight=False))
                ),
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("SO", highlight=False))
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
                        uLABEL("12:30"),
                        uCARD(
                            thickness = 3,
                            rounding = 7,
                            flex = 7,
                            filled = False,child=uCOLUMN(
                            divider_thickness = 0,
                            children=[
                                uLABEL("FAHR-"),
                                uLABEL("SCHULE")
                                ]
                            )
                        ),
                        
                        uLABEL("17:00"),
                        uEMPTY(flex = 2),
                        uLABEL("19:30"),
                        uCARD(
                            flex = 3,
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
                        uCARD(
                            flex = 1,
                            thickness = 3,
                            filled = False,
                            highlight=True,
                            child = uLABEL("GEBURTSTAG...")
                        ),
                        uPBOX(
                            flex = 9,
                            modH = 90,
                            child=uCOLUMN(
                                divider_thickness=0,
                                children = [
                                    uEMPTY(flex = 2),
                                    uLABEL("7:30"),
                                    uCARD(
                                        flex = 3,
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
                                    uEMPTY(flex = 2),

                                    ]
                            )
                        )
                    ]
                ),
                uCOLUMN(
                    flex = 2,
                    children = [
                        uROW(
                            flex = 0.5,
                        divider_thickness=3,
                        children=[
                            uEMPTY(),
                            uEMPTY()]
                    ),
                    uLABEL("9:30"),
                    uPBOX(
                        flex = 3,
                        modH=90,
                        modV=100,
                        child = uCARD(
                        thickness = 3,
                        rounding = 3,
                        filled = False,
                        highlight=True,
                        child = uCOLUMN(
                            children=[
                                uLABEL("MITARBEITER"),
                                uLABEL("FORTBILDUNG"),
                                uEMPTY(flex = 3)
                            ]
                        )
                    )),
                    uLABEL("12:30"),
                    uPBOX(
                        flex = 3,
                        modH=95,
                        child = uROW(
                            seperator = 0,
                            divider_thickness=3,
                            children = [
                                uROW(
                                    
                                    children = [uPBOX(
                                    modH=95,
                                    child = uCOLUMN(
                                    children = [
                                        uLABEL("16:30"),
                                        uCARD(
                                            flex = 3,
                                            filled = False,
                                            highlight=True,
                                            thickness = 3,
                                            rounding=7,
                                            child = uCOLUMN(
                                                children = [
                                                    uLABEL("ZAHN-"),
                                                    uLABEL("ARZT")
                                                ]
                                            )
                                        ),
                                        uLABEL("17:30")
                                        
                                        
                                        ]
                                )),
                                uEMPTY(flex=0.1)
                                ]),
                                uROW(
                                    divider_thickness = 0,
                                    children = [
                                        
                                        uCOLUMN(
                                            flex = 0.1,
                                            children = [
                                                uEMPTY(flex=2),
                                                uCARD(filled = False, thickness=3, rounding=10, level = 1),
                                                uEMPTY(flex = 10)
                                            ]
                                            ),
                                        uCOLUMN(

                                            children = [
                                                uEMPTY(flex=0.8),
                                                uCARD(
                                                flex = 4,
                                                rounding = 7,
                                                filled = True,
                                                highlight=True,
                                                fill_match_border=True,
                                                child=uCOLUMN(
                                                    children=[
                                                        uLABEL("JETZT", highlight=False),
                                                        uEMPTY(),
                                                        uLABEL("BRIEFE", highlight=False),
                                                        uLABEL("ZU", highlight=False),
                                                        uLABEL("DHL", highlight=False),
                                                        uLABEL("BRINGEN", highlight=False)
                                                    ]
                                                )
                                            ),
                                            uLABEL("19:00"),
                                            ]
                                        )
                                    ]
                                )
                                
                            ]
                        )
                    )
                    ]
                ),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    children = [
                        uEMPTY(),
                        uLABEL("7:00"),
                        uCARD(
                            filled = False,
                            thickness = 3,
                            highlight=True,
                            rounding=7,
                            flex=5,
                            child = uCOLUMN(
                                [
                                    uLABEL("MORGEN"),
                                    uLABEL("WORKOUT")
                             ])
                        ),
                        uLABEL("9:30"),
                        uEMPTY(flex = 3),
                        uLABEL("14:30"),
                        uCARD(
                            thickness = 3,
                            filled = False,
                            highlight=True,
                            rounding = 7,
                            flex = 3,
                            child = uCOLUMN(
                                [
                                    uLABEL("MEETING"),
                                    uLABEL("MIT"),
                                    uLABEL("ANDREAS")
                                ]
                            )
                        ),
                        uLABEL("18:30")
                    ]
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                    [
                        uEMPTY(flex=5),
                        uLABEL("20:30"),
                        uCARD(
                            thickness = 3,
                            flex = 6,
                            filled = False,
                            highlight=True,
                            rounding = 7,
                            child=uCOLUMN(
                                [
                                    uLABEL("AB-"),
                                    uLABEL("SCHIEDS-"),
                                    uLABEL("PARTY"),
                                    uLABEL("VON"),
                                    uLABEL("VIVI")
                                ]
                            )
                        ),
                        uLABEL("OPEN END")
                    ]
                )),
                uPBOX(
                    modH = 95,
                    child = uCOLUMN(
                        children = [
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
                            uEMPTY(flex = 4)
                        ]
                    )),
            ]
        )
    ]
)
