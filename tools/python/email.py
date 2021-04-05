#!/opt/local/bin/python3
"""
Email module

Date: 12/1/2018
Revised: 5/16/2019
Created By: John Richardson


"""
import os


def email(subject, body, emailAddress):
    """email
    Email Template

    Parameters: string subject, string body, string emailAddress

    Return
    void
    """
    if '@' in emailAddress:
        string = ('echo ' + body +
                  ' | mutt -s "' + subject + '" ' + emailAddress)
        os.system(string)
    else:
        print('email is not valid')
