# Diamond
# By: houseofkraft

import os
from lib import System

backgroundColor = "40m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def isColor():
    return False

def printColored(sText, sColor):
    tColors = {
          "black": "\033[1;30; " + backgroundColor + " ",
          "red": "\033[1;31; " + backgroundColor + " ",
          "green": "\033[1;32; " + backgroundColor + " ",
          "yellow": "\033[1;33; " + backgroundColor + " ",
          "blue": "\033[1;34; " + backgroundColor + " ",
          "purple": "\033[1;35; " + backgroundColor + " ",
          "cyan": "\033[1;36; " + backgroundColor + " "
    }
    if tColors.get(sColor):
        print(tColors.get(sColor) + sText)
    else:
        return System.Error("Invaild Color")
