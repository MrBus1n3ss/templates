import os
import sys


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

def main():
    platform = getPlatform()    
    print(joinFileName('Test', 'John'))


if __name__ == '__main__':
    main()