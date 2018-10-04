class Requirement:
    def __init__(self, controller, targets, condition, message, problems):
        self.controller = controller
        
        self.targets    = targets
        self.condition  = condition
        self.message    = message
        self.problems   = problems
        self.error      = None

        for target in self.targets:
            target.traceID = target.trace("w", lambda i,o,x: self.checkFulfilled())

        for problem in self.problems:
            problem.config(fg="red")
            problem.bind("<Unmap>", lambda e, p=problem: self.removeProblem(p))
        
        self.checkFulfilled()


    def remove(self):
        if self.error is not None:
            self.controller.removeError(self.error)
            self.error = None

        for problem in self.problems:
            problem.config(fg="black")


    def removeProblem(self, problem):
        if len(self.problems) > 0:
            self.checkFulfilled()
        else:
            self.remove()


    def addProblem(self, problem):
        problem.config(fg="red")
        self.problems.append(problem)
        problem.bind("<Unmap>", lambda e, p=problem: self.removeProblem(p))
        self.checkFulfilled()


    def addTarget(self, target):
        self.targets.append(target)
        target.traceID = target.trace("w", lambda i,o,x: self.checkFulfilled())


    def checkFulfilled(self):
        res = self.condition()

        if not res[0]:
            if res[1] is not None:
                self.message = res[1]
            
            if self.error is None:
                self.error = self.controller.addError(self.message)
            else:
                self.error.setMessage(self.message)
        else:
            self.remove()