from View.errorFrame import ErrorFrame

from Model.error import Error, Solution

class ErrorFrameController():
    def __init__(self, controller):
        self.controller = controller
        self.view = ErrorFrame(self, controller.creationPageController.getView())

        self.errors = []


    def addError(self, message, solutions, problem, callback):
        problem.config(fg="red")
        
        error = Error(message, problem, callback)
        error.label = self.view.addLabel(error.message)
        for solution in solutions:
            traceId = solution.trace("w", lambda i,o,x: self.checkError(error))
            error.solutions.append(Solution(solution, traceId))

        problem.bind("<Unmap>", lambda e: self.removeError(error))
        self.errors.append(error)


    def checkError(self, error):
        func = error.callback

        if func is None:
            self.removeError(error)
            for solution in error.solutions:
                solution.solution.trace_vdelete("w", solution.traceId)
        else:
            res = func()
            if res[0]:
                self.removeError(error)
                return

            if res[1] is not None:
                error.setMessage(res[1])
            
            if error not in self.errors:
                error.problem.config(fg="red")
                error.label = self.view.addLabel(error.message)
                self.errors.append(error)


    def removeError(self, error):
        if error in self.errors:
            error.problem.config(fg="black")
            error.label.destroy()
            self.errors.remove(error)