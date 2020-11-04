import maya.cmds as cmds
import random


def randomDuplication(dupeAmount, minX, maxX, minY, maxY, minZ, maxZ):
    selection = cmds.ls(selection=True)
    objs = []

    for obj in selection:
        for dupeObj in range(0, dupeAmount):
            objs = cmds.duplicate(obj)
            cmds.xform(objs, ws=True, t=(random.uniform(minX, maxX), random.uniform(minY, maxY), random.uniform(minZ, maxZ)))


randomDuplication(1, 0, 12, 0, 12, 0, 12)
