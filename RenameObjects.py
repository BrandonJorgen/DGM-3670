import maya.cmds as cmds


def RenameObject(name_format):
    selection = cmds.ls(selection=True)
    current_sel_count = 1
    for obj in selection:
        num_of_hash = name_format.count("#")
        if num_of_hash > 0:
            obj_partition = name_format.partition("#" * num_of_hash)
            sequence_string = str(current_sel_count)
            cmds.select(obj)
            sequence_string = sequence_string.zfill(num_of_hash)
            cmds.rename(obj_partition[0] + sequence_string + obj_partition[2])
            cmds.rename(obj_partition[0] + sequence_string + obj_partition[2])
            current_sel_count += 1


RenameObject("Leg_##_Jnt")