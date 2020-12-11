import maya.cmds as cmds

class DeleteAllHistory():
    def __init__(self):
        print "I'm being called twice :)"
        self.selection = cmds.ls(selection=True)
        for obj in self.selection:
            cmds.delete(all=True, constructionHistory=True)
