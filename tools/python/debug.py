#!/opt/local/bin/python3
"""
Debug tools for scripts

Date: 1/1/2017
Revised: 5/16/2019
Created By: John Richardson


"""
import sys


def sysExe():
    """sysExe
    Prints the error code

    Parameters: None

    Return
    void
    """
    print(sys.exc_info())


def typeOf(obj):
    """typeOf
    Tells the type of an object

    Parameters: obj

    Return
    void
    """
    print(type(obj))


def printAll(*args):
    """printAll
    will print anything

    Parameters: *args

    Return
    void
    """
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))
