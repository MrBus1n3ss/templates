class Menus:
    def __init__(self):
        self.menuDictionary = {}

    def addMenu(self, name, menu):
        self.menuDictionary[name] = menu
    
    def getByName(self, name):
        menu = ''
        try:
            menu = self.menuDictionary[name]
        except KeyError:
            print('Unknown Menu')
        return menu

    def removeMenu(self, name):
        try:
            self.menuList.pop(name, None)
        except KeyError:
            print('Unknown Option')
