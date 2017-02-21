# Diamond
# By: houseofkraft

import lib.System as System
import lib.Terminal as Terminal
import lib.Filesystem as Filesystem

import sys

path = []

Terminal.clear()
print("Diamond BIOS")
print("Loading...")
print()

# Global Paths
path.append(Filesystem.getPath() + "/bin/")

# Add paths based on specs listed in config.yml
if Terminal.isColor():
    path.append(Filesystem.getPath() + "/bin/color/")

# Import the shell (it actually runs it)
from bin import shell
