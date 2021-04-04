import os
import sys
import getpass

sys.path.append(os.getcwd)

from util.createMenu import CreateMenu
from util.menus import Menus

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
    except Exception:
        print('Unknown file {}'.format(fileName))

def createDir(dirName):
    if not os.path.isdir(dirName):
        # TODO: add try block
        os.mkdir(dirName)
        print('{} created dir'.format(dirName))
    else:
        print('{} already exists'.format(dirName))


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
    path = joinFileName(path, projectName)
    createDir(path)
    
    #TODO: move to function
    logPath = joinFileName(path, 'log')
    createDir(logPath)
    createFile(logPath, '__init__.py')
    
    utilPath = joinFileName(path, 'util')
    createDir(utilPath)
    createFile(logPath, '__init__.py')
    
    testPath = joinFileName(path, 'test')
    createDir(testPath)
    createFile(logPath, '__init__.py')
    
    includePath = joinFileName(path, 'include')
    createDir(includePath)
    createFile(logPath, '__init__.py')




if __name__ == '__main__':
    main()