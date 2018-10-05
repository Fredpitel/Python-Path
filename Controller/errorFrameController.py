from View.errorFrame import ErrorFrame

from Model.error import Error

class ErrorFrameController():
    def __init__(self, controller, view):
        self.controller = controller
        self.view = ErrorFrame(self, view)


    def addError(self, message):
        error = Error(message)
        
        if error.message.get() != "":
            error.label = self.view.addLabel(error.message)

        return error


    def removeError(self, error):
        if error.label != None:
            error.label.pack_forget()