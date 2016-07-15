#preamble.py

"""

"""

import sys, os, pkp, shutil, commands
import numpy as np

def clone(repo):
    print "cloning ", repo,
    os.system('cd /tmp && git clone ' + repo)
    print "[done] "

# if os.path.exists('/tmp'):
#     shutil.rmtree('/tmp')
#     os.makedirs('/tmp')
# else:
#     os.makedirs('/tmp')

print "Revision:", commands.getstatusoutput("git reflog | head -n 1")[1]

clone("https://github.com/greole/CoalExp.git")
clone("https://github.com/greole/IPythonTricks.git")
sys.path.append("/tmp")

from IPythonTricks.ToggleCodeButton import (
    ToggleCodeButton, EnableEquationNumbers, 
    DictTable, DictValueTable, below, side)

from copy import deepcopy
