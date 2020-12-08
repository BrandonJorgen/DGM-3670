import maya.cmds as cmds


class Toolbox():
    def __init__(self):
        self.created_window = "bjToolboxWindow"

    def CreateWindow(self):
        self.DeleteWindow()

        self.window = cmds.window(self.created_window, title="BJ's Toolkit", widthHeight=(400, 200))
        self.column = cmds.rowColumnLayout(parent=self.window, adjustableColumn=True)
        cmds.button(parent=self.column, label="Rename Object Tool", c=lambda *x: self.RenamerWindow())
        cmds.button(parent=self.column, label="Random Placement Tool", c=lambda *x: self.RandomPlacementWindow())
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

created_window = Toolbox()
created_window.CreateWindow()