class uPROPERTYEXCEPTION(Exception):
    def __init__(self, message, widget):
        self.message = "Error causing Node: " + widget + " : " + message
        super().__init__(self.message)
        
class uBUILDTIMEEXCEPTION(Exception):
    def __init__(self, message, widget):
        self.message = "Error causing Node: " + widget + " : " + message
        super().__init__(self.message)

class uHELPEREXCEPTION(Exception):
    def __init__(self, message, widget):
        self.message = "Error causing Node: " + widget + " : " + message
        super().__init__(self.message) 

class uDRAWEXCEPTION(Exception):
    def __init__(self, message, widget):
        self.message = "Error causing Node:" + widget + " : " + message
        super().__init__(self.message)