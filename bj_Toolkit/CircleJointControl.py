import maya.cmds as cmds


class CircleJointControl:
    def __init__(self):
        pass

    def CreateControl(self):
        # Grab your selection X
        # For loop through the list X
        # Grab name of Joint X
        # Copy name of Joint and replace Jnt and other suffixes with correct suffixes X
        # Create Group and change name to correct name X
        # Create Nurbs Circle and change name to correct name X
        # Parent Nurbs Circle to Group X
        # TODO select between FK, IK, RK, Bind, Ect. suffixes
        # Match transformations with joint X
        sels = cmds.ls(selection=True)  # Should be a list of Joints
        if len(sels) > 0:
            for obj in sels:
                obj_Name = cmds.joint(obj, q=True, n=True)
                name_Partition = obj_Name.partition("_Jnt")
                print name_Partition
                ctrl_Suffix = "_Ctrl"
                grp_Suffix = "_Ctrl_Grp"
                control = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0))
                cmds.select(control)
                cmds.rename(name_Partition[0] + ctrl_Suffix)
                group = cmds.group(n=name_Partition[0] + grp_Suffix)
                cmds.matchTransform(group, obj)
        else:
            ctrl_Suffix = "_Ctrl"
            grp_Suffix = "_Ctrl_Grp"
            control = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0))
            cmds.select(control)
            cmds.rename(ctrl_Suffix)
            group = cmds.group(n=grp_Suffix)
