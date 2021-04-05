import sys

from pprint import pprint as pp

class File:
    def __init__(self, file):
        self.file = file
        self.fileList = [] 
    
    def openFile(self):
        try:
            with open(self.file, 'r') as f:
                self.fileList.append(f.read())
        except FileNotFoundError:
            print('Unable to locate file')
        except Exception:
            print('Unable to open file')
            print(sys.exc_info())
            sys.exit(0)

    def createFile(self):
        try:
            open(self.file, 'w')
        except FileNotFoundError:
            print('Unable to locate file')
        except Exception:
            print('Unable to open file')
            print(sys.exc_info())
            sys.exit(0)

    def writeFile(self, line):
        self.fileList.append(line)
        try:
            f = open(self.file, 'w')
            for line in self.fileList:
                f.write(line)
        except FileNotFoundError:
            print('Unable to locate file')
        except Exception:
            print('Unable to open file')
            print(sys.exc_info())
            sys.exit(0)
    
    def printAll(self):
        for line in self.fileList:
            print(line)
    
    def ppAll(self):
        for line in self.fileList:
            pp(line)
