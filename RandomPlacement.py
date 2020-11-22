import maya.cmds as cmds
import random


class RandomPlacement():
    def __init__(self):
        self.created_window = "bjWindow"

    def randomDuplication(self, dupeAmount, minX, maxX, minY, maxY, minZ, maxZ):
        selection = cmds.ls(selection=True)
        objs = []
        dupeAmount = cmds.intSlider(self.dupeAmountSlider, q=True, value=True)
        minX = cmds.intSlider(self.minXSlider, q=True, value=True)
        maxX = cmds.intSlider(self.maxXSlider, q=True, value=True)
        minY = cmds.intSlider(self.minYSlider, q=True, value=True)
        maxY = cmds.intSlider(self.maxYSlider, q=True, value=True)
        minZ = cmds.intSlider(self.minZSlider, q=True, value=True)
        maxZ = cmds.intSlider(self.maxZSlider, q=True, value=True)

        for obj in selection:
            for dupeObj in range(0, dupeAmount):
                objs = cmds.duplicate(obj)
                cmds.xform(objs, ws=True, t=(random.uniform(minX, maxX), random.uniform(minY, maxY), random.uniform(minZ, maxZ)))


    def CreateWindow(self):
        self.DeleteWindow()

        self.window = cmds.window(self.created_window, title="Random Placement Window", widthHeight=(400, 200))
        self.column = cmds.rowColumnLayout(parent=self.window, numberOfColumns=3)
        cmds.text(parent=self.column, label="Duplication amount: ")
        self.dupeAmountSlider = cmds.intSlider(min=1, max=100, value=1, step=1)
        cmds.text(parent=self.column, label="Min X: ")
        self.minXSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.minXValue = cmds.text(parent=self.column, label="value")
        cmds.text(parent=self.column, label="Max X: ")
        self.maxXSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.maxXValue = cmds.text(parent=self.column, label="value")
        cmds.text(parent=self.column, label="Min Y: ")
        self.minYSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.minYValue = cmds.text(parent=self.column, label="value")
        cmds.text(parent=self.column, label="Max Y: ")
        self.maxYSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.maxYValue = cmds.text(parent=self.column, label="value")
        cmds.text(parent=self.column, label="Min Z: ")
        self.minZSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.minZValue = cmds.text(parent=self.column, label="value")
        cmds.text(parent=self.column, label="Max Z: ")
        self.maxZSlider = cmds.intSlider(min=0, max=12, value=0, step=1)
        self.maxZValue = cmds.text(parent=self.column, label="value")
        cmds.button(parent=self.column, label="Execute", c=self.randomDuplication)
        cmds.showWindow(self.window)

    def DeleteWindow(self):
        if cmds.window(self.created_window, exists=True):
            cmds.deleteUI(self.created_window)
