import maya.cmds as cmds


class JointOrientationAxis():
    def __init__(self):
        pass

    def Toggle(self):
        # List of selected joints
        selection = cmds.ls(selection=True)

        # Check if every object selected is a joint
        for obj in selection:
            if cmds.objectType(obj) != "joint":
                cmds.error("Please only select joints for this operation")
            # current object is a joint
            else:
                if cmds.getAttr(obj + ".displayLocalAxis", k=True):
                    cmds.setAttr(obj + ".displayLocalAxis", keyable=False)
                    cmds.setAttr(obj + ".displayLocalAxis", False)
                    cmds.setAttr(obj + ".jointOrientX", keyable=False)
                    cmds.setAttr(obj + ".jointOrientY", keyable=False)
                    cmds.setAttr(obj + ".jointOrientZ", keyable=False)
                else:
                    cmds.setAttr(obj + ".displayLocalAxis", keyable=True)
                    cmds.setAttr(obj + ".displayLocalAxis", True)
                    cmds.setAttr(obj + ".jointOrientX", keyable=True)
                    cmds.setAttr(obj + ".jointOrientY", keyable=True)
                    cmds.setAttr(obj + ".jointOrientZ", keyable=True)
