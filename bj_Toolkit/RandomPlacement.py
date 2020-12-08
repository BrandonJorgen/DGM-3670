import maya.cmds as cmds
import random


class RandomPlacement():
    def __init__(self):
        self.created_window = "bjWindow"

    def randomDuplication(self, dupeamount, minx, maxx, miny, maxy, minz, maxz):
        dupeamount = cmds.intField(self.dupeAmountInput, q=True, value=True)
        minx = cmds.intField(self.minXInput, q=True, value=True)
        maxx = cmds.intField(self.maxXInput, q=True, value=True)
        miny = cmds.intField(self.minYInput, q=True, value=True)
        maxy = cmds.intField(self.maxYInput, q=True, value=True)
        minz = cmds.intField(self.minZInput, q=True, value=True)
        maxz = cmds.intField(self.maxZInput, q=True, value=True)
        selection = cmds.ls(selection=True)
        objs = []

        for obj in selection:
            for dupeObj in range(0, dupeamount):
                objs = cmds.duplicate(obj)
                cmds.xform(objs, ws=True, t=(random.uniform(minx, maxx),
                                             random.uniform(miny, maxy),
                                             random.uniform(minz, maxz)))

    def CreateWindow(self):
        self.DeleteWindow()

        self.window = cmds.window(self.created_window, title="Random Placement Window", widthHeight=(400, 200))
        self.column = cmds.rowColumnLayout(parent=self.window, numberOfColumns=2)
        cmds.text(parent=self.column, label="Duplication amount: ")
        self.dupeAmountInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=1)
        cmds.text(parent=self.column, label="Min X: ")
        self.minXInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.text(parent=self.column, label="Max X: ")
        self.maxXInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.text(parent=self.column, label="Min Y: ")
        self.minYInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.text(parent=self.column, label="Max Y: ")
        self.maxYInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.text(parent=self.column, label="Min Z: ")
        self.minZInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.text(parent=self.column, label="Max Z: ")
        self.maxZInput = cmds.intField(parent=self.column, minValue=-100, maxValue=100, value=0)
        cmds.button(parent=self.column, label="Execute", c=lambda *x: self.randomDuplication(dupeamount=self.dupeAmountInput,
                                                                                             minx=self.minXInput,
                                                                                             maxx=self.maxXInput,
                                                                                             miny=self.minYInput,
                                                                                             maxy=self.maxYInput,
                                                                                             minz=self.minZInput,
                                                                                             maxz=self.maxXInput))
        cmds.showWindow(self.window)

    def DeleteWindow(self):
        if cmds.window(self.created_window, exists=True):
            cmds.deleteUI(self.created_window)
