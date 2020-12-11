import maya.cmds as cmds


class FreezeTransformations():
    def __init__(self):
        self.selection = cmds.ls(s=True)
        for obj in self.selection:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
