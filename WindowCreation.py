import maya.cmds as cmds


def CreateWindow():
    created_window = "bjWindow"

    if cmds.window(created_window, exists=True):
        cmds.deleteUI(created_window)

    window = cmds.window(created_window, title="Super Cool Window for Exciting Things", widthHeight=(400, 200))
    column = cmds.rowColumnLayout(parent=window, numberOfColumns=2)
    cmds.text(parent=column, label="Text Input Field: ")
    cmds.textField(parent=column)
    cmds.button(parent=column, label="Execute")
    cmds.showWindow(window)


CreateWindow()
