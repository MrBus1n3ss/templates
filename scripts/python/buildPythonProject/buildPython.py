import os
import sys
import getpass

sys.path.append(os.getcwd)

from util.createMenu import CreateMenu
from util.menus import Menus
import text.mainText as mainText

# TODO: test on each platform
def getPlatform():
    platforms = {
        'linux': 'linux',
        'darwin': 'mac',
        'win32': 'windows'
    }
    os = sys.platform
    if 'linux' in os:
        os = platforms['linux']
    if 'darwin' in os:
        os = platforms['darwin']
    if 'win' in os:
        os = platforms['win32']
    return os
    


# *nix/Windows safe
def joinFileName(*argv):
    if len(argv) >= 2:
        for count, arg in enumerate(argv):
            if(count <= 0):
                temp_arg = arg
            else:
                temp_arg = os.path.join(temp_arg, arg)
        return temp_arg
    else:
        # TODO: add errors
        print('error')


def getProjectFolder(platform):
    user = getpass.getuser()
    if platform == 'linux':
        os.chdir(joinFileName('/', 'home', user))
    elif platform == 'mac':
        os.chdir(joinFileName('/', 'home', user))
    elif platform == 'windows':
        os.chdir('C:\\')
    return os.getcwd()

def createFile(path, fileName):
    try:
        file = open(joinFileName(path, fileName), 'w')
        print('{} created File'.format(fileName))
        return file
    except Exception:
        print('Unknown file {}'.format(fileName))


def writeFile(file, contents):
    try:
        file.write(contents)
    except Exception:
        print('Failed to write lines')


def closeFile(file):
    try:
        file.close()
    except Exception:
        print('Uknown file to close {}'.format(file))


def createDir(dirName):
    if not os.path.isdir(dirName):
        # TODO: add try block
        os.mkdir(dirName)
        print('{} created dir'.format(dirName))
    else:
        print('{} already exists'.format(dirName))


def createInit(path, dirName):
    path = joinFileName(path, dirName)
    createDir(path)
    initFile = createFile(path, '__init__.py')
    closeFile(initFile)


def createFileWithContent(path, fileName, contents):
    createDir(path)
    newFile = createFile(path, fileName)
    writeFile(newFile, contents)
    closeFile(newFile)


def main():
    menus = Menus()
    
    #TODO: will clean this up, will update the arrow better
    projectMenu = CreateMenu('Project Setup')
    projectMenu.addOption('> Project Name')
    projectMenu.addOption('Author')
    projectMenu.addOption('Type of Project')
    menus.addMenu('projectSetup', projectMenu)
    menus.getByName('projectSetup').printAll()
    projectName = input('Project Name >')

    projectMenu.updateOption(0, 'Project Name')
    projectMenu.updateOption(1, '> Author')
    menus.getByName('projectSetup').printAll()
    author = input('Author >')

    projectMenu.updateOption(1, 'Author')
    projectMenu.updateOption(2, '> Type of Project')
    menus.getByName('projectSetup').printAll()
    projectType = input('Type Of Project >')
    # TODO: currently vanilla python, want to add other projects Django/Flask


    platform = getPlatform()
    path = getProjectFolder(platform)    
    path = joinFileName(path, 'projects')
    createDir(path)
    
    #Create Project
    createFileWithContent(path, '{}.py'.format(projectName), mainText.main)
    createInit(path, 'log')
    createInit(path, 'util')
    createInit(path, 'test')
    createInit(path, 'include')




if __name__ == '__main__':
    main()