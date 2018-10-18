from View.sheetPage import SheetPage

class SheetPageController:
    def __init__(self, controller):
        self.controller = controller
        self.char       = controller.char

        self.view = SheetPage(self, controller.nb)


    def getView(self):
        return self.view.sheetPage