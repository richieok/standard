#handy module
import re, os.path
from configparser import ConfigParser

class QuitException(Exception):
    pass

def testQuit(response):
    '''Raises QuitException when input == "quit"'''
    temp = input(response)
    qmo = re.search(r'^quit$', temp, re.I)
    if qmo:
        raise QuitException("Quit")
    else:
        return temp

def mapFolder(location):
    m = []
    for folder, subs, files in os.walk(location):
        for sub in subs:
            m.append({os.path.join(folder,sub):False})
        for f in files:
            m.append({os.path.join(folder,f):False})
    return m
