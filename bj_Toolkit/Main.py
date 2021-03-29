import maya.cmds as cmds


class Toolbox():
    def __init__(self):
        self.created_window = "bjToolboxWindow"

    def CreateWindow(self):
        self.DeleteWindow()

        self.window = cmds.window(self.created_window, title="BJ's Toolkit", widthHeight=(400, 250))
        self.column = cmds.rowColumnLayout(parent=self.window, adjustableColumn=True)
        cmds.button(parent=self.column, label="Rename Object Tool", c=lambda *x: self.RenamerWindow())
        cmds.button(parent=self.column, label="Random Placement Tool", c=lambda *x: self.RandomPlacementWindow())
        cmds.button(parent=self.column, label="Freeze Transformations", c=lambda *x: self.FreezeTransformationCall())
        cmds.button(parent=self.column, label="Delete All History", c=lambda *x: self.DeleteAllHistoryCall())
        cmds.button(parent=self.column, label="Create Parent Group", c=lambda *x: self.CreateParentGroup())
        cmds.button(parent=self.column, label="Parent/Scale Constraint", c=lambda *x: self.ConstrainObjsCall())
        cmds.button(parent=self.column, label="Toggle Joint Orientation Axis", c=lambda *x: self.AxisOrientationEnableCall())
        cmds.button(parent=self.column, label="Create Circle Control", c=lambda *x: self.CreateCircleControl())
        cmds.button(parent=self.column, label="Follow Attribute Constraints", c=lambda *x: self.CreateFollowAttributeConstraints())
        cmds.button(parent=self.column, label="Create ID Map Materials", c=lambda *x: self.CreateIDMapMaterials())
        cmds.button(parent=self.column, label="Create IKFK Switch", c=lambda *x: self.CreateIKFKSwitch())
        cmds.showWindow(self.window)

    def DeleteWindow(self):
        if cmds.window(self.created_window, exists=True):
            cmds.deleteUI(self.created_window)

    def RenamerWindow(self):
        import RenameObjects
        reload(RenameObjects)
        Window = RenameObjects.Renamer()
        Window.CreateWindow()

    def RandomPlacementWindow(self):
        import RandomPlacement
        reload(RandomPlacement)
        Window = RandomPlacement.RandomPlacement()
        Window.CreateWindow()

    def FreezeTransformationCall(self):
        import FreezeTransformations
        reload(FreezeTransformations)
        Function = FreezeTransformations.FreezeTransformations()
        Function.__init__()

    def DeleteAllHistoryCall(self):
        import DeleteAllHistory
        reload(DeleteAllHistory)
        Function = DeleteAllHistory.DeleteAllHistory()
        Function.__init__()

    def CreateParentGroup(self):
        import CreateParentGroup
        reload(CreateParentGroup)
        Function = CreateParentGroup.CreateParentGroup()
        Function.CreateGroup()

    def ConstrainObjsCall(self):
        import ParentScaleConstraint
        reload(ParentScaleConstraint)
        Function = ParentScaleConstraint.ParentScaleConstraint()
        Function.ConstrainObjs()

    def AxisOrientationEnableCall(self):
        import EnableJointOrientationAxis
        reload(EnableJointOrientationAxis)
        Function = EnableJointOrientationAxis.JointOrientationAxis()
        Function.Toggle()

    def CreateCircleControl(self):
        import CircleJointControl
        reload(CircleJointControl)
        Function = CircleJointControl.CircleJointControl()
        Function.CreateControl()

    def CreateFollowAttributeConstraints(self):
        import FollowAttributeConstraints
        reload(FollowAttributeConstraints)
        Function = FollowAttributeConstraints.FollowAttributeConstraints()
        Function.Main()

    def CreateIDMapMaterials(self):
        import CreateIDMapMaterials
        reload(CreateIDMapMaterials)
        Function = CreateIDMapMaterials.CreateIDMapMaterials()
        Function.CreateMaterials()

    def CreateIKFKSwitch(self):
        import IKFKSwitch
        reload(IKFKSwitch)
        Function = IKFKSwitch.IKFKSwitch()
        Function.Main()



created_window = Toolbox()
created_window.CreateWindow()