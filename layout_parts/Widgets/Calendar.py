from layout_parts.Widgets.uNodes.uCard import uCARD
from layout_parts.Widgets.uNodes.uColumn import uCOLUMN
from layout_parts.Widgets.uNodes.uPBox import uPBOX
from layout_parts.Widgets.uNodes.uRow import uROW
from layout_parts.Widgets.uNodes.uLabel import uLABEL

body = uCOLUMN(
    divider_thickness=3,
    children=[
        uROW(
            flex = 1,
            divider_thickness = 0,
            children = [
                uPBOX(
                    modV=60,
                    modH=60,
                    child=uCARD(rounding=10,child=uLABEL("MO", highlight=False))
                ),
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
                            rounding = 5,
                            flex = 5,
                            filled = False,child=uCOLUMN(
                            divider_thickness = 0,
                            children=[
                                uLABEL("FAHR-"),
                                uLABEL("SCHULE")
                                ]
                            )
                        ),
                        
                        uLABEL("17:00"),
                        uLABEL(" ", flex = 2),
                        uLABEL("19:30"),
                        uCARD(
                            flex = 3,
                            thickness = 3,
                            rounding = 5,
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
                                    uLABEL("7:30"),
                                    uCARD(
                                        flex = 1,
                                        filled = False,
                                        thickness=3,
                                        rounding=5,
                                        child=uCOLUMN(
                                            children=[
                                                uLABEL("WANDER-"),
                                                uLABEL("UND"),
                                                uLABEL("MIT"),
                                                uLABEL("FAMILIE")
                                            ]
                                        )
                                    ),
                                    uLABEL("19:45")
                                    ]
                            )
                        )
                    ]
                ),
                uCOLUMN(),
                uCOLUMN(),
                uCOLUMN(),
                uCOLUMN(),
                uCOLUMN(),

            ]
        )
    ]
)
