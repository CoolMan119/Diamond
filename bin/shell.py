# Diamond Shell
# By: houseofkraft

# TODO: Add recent commands with the up and down key

from msvcrt import getch
from lib import System
from lib import Filesystem
from lib import Terminal

import os

Terminal.clear()

print("Diamond Shell")

bRunning = True
while bRunning:
    print("> ", end="")
    sCommand = input() # May be insecure
    # Attempt to search the file
    # newCommand = "py " + Filesystem.getPath() + "/bin/" + sCommand + ".py"
    # if Filesystem.exists(newCommand):
    #  print(newCommand)
    #  #exec(newCommand)
    # elif sCommand == "exit":
    #     bRunning = False # End the shell process
    # else:
    print("Invaild Command!")


# The shell has ended, shutdown the process.
os.system("exit")
