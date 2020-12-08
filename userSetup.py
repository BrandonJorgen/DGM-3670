import maya.cmds as cmds
import sys

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

if 'F:/Fall 2020/DGM-3670/bj_Toolkit' not in sys.path:
    sys.path.append('F:/Fall 2020/DGM-3670/bj_Toolkit')

for s in sys.path:
    print s