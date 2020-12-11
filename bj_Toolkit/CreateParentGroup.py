import maya.cmds as cmds


class CreateParentGroup():
    def __init__(self):
        pass

    def CreateGroup(self):
        self.selection = cmds.ls(selection=True)
        cmds.group(self.selection, n="Group")
