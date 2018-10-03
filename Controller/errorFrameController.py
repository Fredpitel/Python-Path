from View.errorFrame import ErrorFrame

from Model.error import Error

class ErrorFrameController():
    def __init__(self, controller):
        self.controller = controller
        self.view = ErrorFrame(self, controller.creationPageController.getView())


    def addError(self, message, problems):
        error = Error(message, problems)

        for problem in error.problems:
            problem.config(fg="red")
        
        if error.message.get() != "":
            error.label = self.view.addLabel(error.message)

        return error


    def removeError(self, error):
        if error.label != None:
            error.label.pack_forget()