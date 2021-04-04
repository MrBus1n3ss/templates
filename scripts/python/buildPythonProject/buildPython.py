import os

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
    print(joinFileName('Test'))


if __name__ == '__main__':
    main()