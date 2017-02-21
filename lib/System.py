# Diamond
# By: houseofkraft

from lib import Terminal

PATH = []

def error(sText):
    if sText:
        Terminal.printColored(sText, "red")
    else:
        Terminal.printColored("Usage: System.error(string text)", "red")

def setPath(newPath):
    PATH = newPath

def getPath():
    return PATH
