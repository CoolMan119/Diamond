# Diamond
# By: houseofkraft

from pathlib import Path

import sys
import os

def exists(sName):
    file = Path(sName)
    return file.is_file()

def getPath():
    file = sys.argv[0]
    pathname = os.path.dirname(file)
    return os.path.abspath(pathname)
