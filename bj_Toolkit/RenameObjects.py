import maya.cmds as cmds


class Renamer():
    def __init__(self):
        self.created_window = "bjWindow"

    def RenameObject(self, name_format):
        selection = cmds.ls(selection=True)
        name_format = cmds.textField(self.textInput, q=True, text=True)
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
            else:
                cmds.error("No # symbols located in text input")

    def CreateWindow(self):
        self.DeleteWindow()

        self.window = cmds.window(self.created_window, title="Object Renamer Window", widthHeight=(400, 200))
        self.column = cmds.rowColumnLayout(parent=self.window, numberOfColumns=2)
        cmds.text(parent=self.column, label="Text Input Field: ")
        self.textInput = cmds.textField(parent=self.column)
        cmds.button(parent=self.column, label="Execute", c=self.RenameObject)
        cmds.showWindow(self.window)

    def DeleteWindow(self):
        if cmds.window(self.created_window, exists=True):
            cmds.deleteUI(self.created_window)

