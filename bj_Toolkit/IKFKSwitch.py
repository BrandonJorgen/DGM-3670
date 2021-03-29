import maya.cmds as cmds


class IKFKSwitch:
    def Main(self):
        self.LoadSelection()
        self.CreateRKJoints()
        self.CreateGroups()
        self.ConstrainJoints()
        self.CreateAttributes()
        self.ConnectAttributes()

    def LoadSelection(self):
        sels = cmds.ls(selection=True)
        for i in sels:
            objName = cmds.rename(i, i)
            if "FK" in objName:
                self.fkJoint = i
            elif "IK" in objName:
                self.ikJoint = i
            elif "Transform" in objName:
                self.transformCtrl = i
            else:
                cmds.error("Object name doesn't fit any options (Check for capitalization)")

    def CreateRKJoints(self):
        #Duplicate FK Joints
        self.newJointChain = cmds.duplicate(self.fkJoint, name="tempname", renameChildren=True)
        self.jointName = cmds.rename(self.fkJoint, self.fkJoint)
        self.jointNamePartion = self.jointName.replace("FK", "RK")
        #Rename Joints to RK
        cmds.select(self.newJointChain, hierarchy=True)
        self.RenameObject(self.jointNamePartion)
        self.rkJointSel = cmds.select(self.jointNamePartion)
        self.rkJoint = cmds.ls(selection=True, an=True)
        self.rkJointName = cmds.rename(self.rkJoint, self.rkJoint)
        #Change override color of Parent RK Joint
        #14 is index number for GREEN
        cmds.setAttr(self.rkJointName + ".overrideColor", 14)
        #Change the radius of the joints
        #first, find the radius of the FK chain
        #TODO MAYBE?
        #self.fkJointRadius = cmds.joint(self.fkJoint, q=True, radius=True)


    def RenameObject(self, name_format):
        selection = cmds.ls(selection=True)
        current_sel_count = 1
        for obj in selection:
            num_of_hash = name_format.count("01")
            if num_of_hash > 0:
                obj_partition = name_format.partition("01" * num_of_hash)
                sequence_string = str(current_sel_count)
                cmds.select(obj)
                sequence_string = sequence_string.zfill(num_of_hash + 1)
                cmds.rename(obj_partition[0] + sequence_string + obj_partition[2])
                cmds.rename(obj_partition[0] + sequence_string + obj_partition[2])
                current_sel_count += 1
            else:
                cmds.error("No # symbols located in text input")

    def CreateGroups(self):
        cmds.select(self.fkJoint)
        self.masterGrp = cmds.pickWalk(direction="up")
        self.fkJntGrp = cmds.group(empty=True, n=self.jointName.replace("01_FK_Jnt", "FK_Grp"), parent=cmds.rename(self.masterGrp, self.masterGrp))
        cmds.parent(self.fkJoint, self.fkJntGrp)
        self.ikJntGrp = cmds.group(empty=True, n=self.jointName.replace("01_FK_Jnt", "IK_Grp"), parent=cmds.rename(self.masterGrp, self.masterGrp))
        cmds.parent(self.ikJoint, self.ikJntGrp)
        self.rkJntGrp = cmds.group(empty=True, n=self.jointName.replace("01_FK_Jnt", "RK_Grp"), parent=cmds.rename(self.masterGrp, self.masterGrp))
        cmds.parent(self.jointNamePartion, self.rkJntGrp)

        self.fkCtrlGrp = cmds.group(empty=True, n=self.jointName.replace("01_FK_Jnt", "FK_Ctrl_Grp"), parent=cmds.rename(self.masterGrp, self.masterGrp))
        cmds.parent(self.fkCtrlGrp, w=True)
        self.ikCtrlGrp = cmds.group(empty=True, n=self.jointName.replace("01_FK_Jnt", "IK_Ctrl_Grp"), parent=cmds.rename(self.masterGrp, self.masterGrp))
        cmds.parent(self.ikCtrlGrp, w=True)

    def ConstrainJoints(self):
        cmds.select(self.fkJoint)
        cmds.select(self.ikJoint, add=True)
        cmds.select(self.rkJoint, add=True)
        self.constraintList = []
        for i in range(3):
            self.constraintList.append(cmds.parentConstraint(cmds.ls(selection=True), mo=True))
            self.constraintList.append(cmds.scaleConstraint(cmds.ls(selection=True), mo=True))
            cmds.pickWalk(direction="down")

    def CreateAttributes(self):
        enumNames = "IK:FK"
        self.partition = self.fkJoint.partition("01_FK")
        cmds.addAttr(self.transformCtrl, longName=self.partition[0] + "_IKFK_Switch", at="enum", enumName=enumNames)
        cmds.setAttr(self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", k=True)

    def ConnectAttributes(self):
        temp = 1

        for k in range(2):
            cmds.setAttr(self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", k)
            cmds.setAttr(self.fkCtrlGrp + ".visibility", k)
            cmds.setDrivenKeyframe(self.fkCtrlGrp + ".visibility", cd=self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", itt="linear", ott="linear")
            cmds.setAttr(self.ikCtrlGrp + ".visibility", temp)
            cmds.setDrivenKeyframe(self.ikCtrlGrp + ".visibility", cd=self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", itt="linear", ott="linear")
            for i, t in enumerate(self.constraintList):
                cmds.setAttr("%s.w%i" % (cmds.rename(t, t), 0), k)
                cmds.setDrivenKeyframe("%s.w%i" % (cmds.rename(t, t), 0), cd=self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", itt="linear", ott="linear")
                cmds.setAttr("%s.w%i" % (cmds.rename(t, t), 1), temp)
                cmds.setDrivenKeyframe("%s.w%i" % (cmds.rename(t, t), 1), cd=self.transformCtrl + "." + self.partition[0] + "_IKFK_Switch", itt="linear", ott="linear")

            temp = 0


