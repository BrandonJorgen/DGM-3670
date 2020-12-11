import maya.cmds as cmds


class ParentScaleConstraint():
    def __init__(self):
        pass

    def ConstrainObjs(self):
        selection = cmds.ls(os=True)

        if len(selection) % 2 != 0:
            cmds.error("Current selection is an odd number, please select an even amount of objects")
        else:
            for obj in range(0, len(selection), 2):
                cmds.parentConstraint(selection[obj], selection[obj + 1], mo=True)
                cmds.scaleConstraint(selection[obj], selection[obj + 1], mo=True)
