import maya.cmds as cmds

class FollowAttributeConstraints:
    def __init__(self):
        pass

    def Main(self):
        sels = cmds.ls(selection=True)
        parents = sels
        child = sels[len(sels) - 1]
        parents.remove(child)
        parentNames = ""

        pConstraint = cmds.parentConstraint(parents, child, mo=True)
        sConstraint = cmds.scaleConstraint(parents, child, mo=True)

        pConstraintName = cmds.rename(pConstraint, pConstraint)
        sConstraintName = cmds.rename(sConstraint, sConstraint)

        parentNames = "World:"
        for obj in range(1, len(parents)):
            parentNames += cmds.rename(parents[obj], parents[obj])
            parentNames += ":"

        cmds.addAttr(child, longName="Follow", at="enum", enumName=parentNames)
        cmds.setAttr(child + ".Follow", k=True)

        for i, t in enumerate(parents):
            cmds.setAttr(child + ".Follow", i)

            for b, c in enumerate(parents):
                # Set every weight to 0 and then set driven key
                cmds.setAttr("%s.w%i" % (pConstraintName, b), 0)
                cmds.setAttr("%s.w%i" % (sConstraintName, b), 0)
                cmds.setDrivenKeyframe("%s.w%i" % (pConstraintName, b), cd=child + ".Follow", itt="linear", ott="linear")
                cmds.setDrivenKeyframe("%s.w%i" % (sConstraintName, b), cd=child + ".Follow", itt="linear", ott="linear")

            # Set the correct weight to 1 and then set driven key
            cmds.setAttr("%s.w%i" % (pConstraintName, i), 1)
            cmds.setAttr("%s.w%i" % (sConstraintName, i), 1)
            cmds.setDrivenKeyframe("%s.w%i" % (pConstraintName, i), cd=child + ".Follow", itt="linear", ott="linear")
            cmds.setDrivenKeyframe("%s.w%i" % (sConstraintName, i), cd=child + ".Follow", itt="linear", ott="linear")

        cmds.setAttr(child + ".Follow", 0)

