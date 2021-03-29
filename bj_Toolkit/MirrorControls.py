import maya.cmds as cmds


sels = cmds.ls(selection=True)  # First selection is OBJ, second selection is TARGET transform
obj = sels[0]
target = sels[1]

obj = cmds.parent(obj, target, absolute=True)[0]
cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0, pn=1)
cmds.delete(obj, ch=True)

obj_shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)
target_shapes = cmds.listRelatives(target, shapes=True, fullPath=True)

for shape in obj_shapes:
    cmds.parent(shape, target, shape=True, relative=True)


cmds.delete(target_shapes)
cmds.delete(obj)

target_shapes = target_shapes = cmds.listRelatives(target, shapes=True, fullPath=True)
for shape in target_shapes:
    cmds.rename(shape, "%sShape" % target)
