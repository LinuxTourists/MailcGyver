# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:11:35 2016

@author: markus

MailcGyver Filter Module
return value must be True or False.

"""

from email.utils import parseaddr

# example, check if the "Mail From" Address is a valid mail address
def ValidMailAddress (email):
    if parseaddr (email) == ('', ''):
        return False
    return "@" in parseaddr(email)[1]


# Main
def MGFilter (Incomming):
    return ValidMailAddress(Incomming["mlfr"])
