import maya.cmds as cmds


sels = cmds.ls(sl=True)
bbox = cmds.exactWorldBoundingBox(sels)

xLoc = (bbox[0] + bbox[3]) / 2
yLoc = (bbox[1] + bbox[4]) / 2
zLoc = (bbox[2] + bbox[5]) / 2
locator = cmds.spaceLocator(p=[0, 0, 0])
cmds.xform(locator, ws=True, t=[xLoc, yLoc, zLoc])

