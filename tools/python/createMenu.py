class CreateMenu:
    def __init__(self, title, *argv):
        self.width = 50
        self.lineGraphic = '*'
        self.title = title
        self.options = []
        for arg in argv:
            self.options.append(arg)

    def drawLine(self):
        """Draws a line

        Parameters:
        line_graphic (string): The character it uses to draw the line
        width (int): width of the line

        Returns:
        void

        """
        line = str(self.lineGraphic) * self.width
        print(line)

    def addOption(self, statement):
        """Prints info with the correct format

        Parameters:
        statement (string): info that is going to get formatted
        width (int): the width of the area to print

        Returns:
        void

        """
        self.options.append(statement)

    def updateOption(self, arrayIndex, statement):
        self.options[arrayIndex] = statement

    def removeOption(self, index):
        try:
            self.options.pop(index)
        except IndexError:
            print('Unknown Option')

    def printAll(self, showNumbers=True):
        self.drawLine()
        fillerSpaces = ' ' * (self.width - len(self.title) - 3)
        print('| ' + self.title + fillerSpaces + '|')
        self.drawLine()
        if showNumbers:
            for count, option in enumerate(self.options):
                statement = ''
                statement = str(count) + ') ' + option
                fillerSpaces = ' ' * (self.width - len(statement) - 3)
                print('| ' + statement + fillerSpaces + '|')
        else:
            for option in self.options:
                fillerSpaces = ' ' * (self.width - len(option) - 3)
                print('| ' + option + fillerSpaces + '|') 
        self.drawLine()
