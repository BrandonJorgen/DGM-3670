import maya.cmds as cmds


class CreateIDMapMaterials():
    def __init__(self):
        self.numOfMats = 0
        self.nameOfMat = ""

    def CreateMaterials(self):
        #we need materials for each of the base colors that Maya gives us
        #8 materials are needed

        self.numOfMats = 0

        while self.numOfMats < 8:
            #create the material and assign its color

            #create the initial shader node
            material = cmds.shadingNode("lambert", n=self.DefineMaterialName(self.numOfMats), asShader=True)

            #create the SG node, I don't even know what this does or what SG stands for
            materialSG = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=(material + "SG"))

            #set up the connections between the two nodes
            cmds.connectAttr(material + ".outColor", materialSG + ".surfaceShader")

            #change the color of the shader
            cmds.select(material)
            cmds.setAttr(material + ".color", self.DefineMaterialColor(self.nameOfMat)[0], self.DefineMaterialColor(self.nameOfMat)[1], self.DefineMaterialColor(self.nameOfMat)[2], type="float3")

            #increment the number of materials made
            self.numOfMats += 1

    def DefineMaterialName(self, num):
        #Need a way to define what the name of the next material should be

        switcher = {
            0: "Red",
            1: "Blue",
            2: "Yellow",
            3: "Green",
            4: "Teal",
            5: "Purple",
            6: "White",
            7: "Black"
        }

        return switcher.get(num, "Number out of range")

    def DefineMaterialColor(self, name):
        name = self.DefineMaterialName(self.numOfMats)

        switcher = {
            "Red": [1, 0, 0],
            "Blue": [0, 0, 1],
            "Yellow": [1, 1, 0],
            "Green": [0, 1, 0],
            "Teal": [0, 1, 1],
            "Purple": [1, 0, 1],
            "White": [1, 1, 1],
            "Black": [0, 0, 0]
        }

        return switcher.get(name, "Incorrect name")
