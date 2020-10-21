import maya.cmds as cmds

#Body Geo creation
cmds.polySphere(r=2, sx=20, sy=20, ax=[0, 2, 0], cuv=2, ch=1, n="Body_Bottom")
cmds.polySphere(r=1.5, sx=20, sy=20, ax=[0, 2, 0], cuv=2, ch=1, n="Body_Middle")
cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 2, 0], cuv=2, ch=1, n="Body_Top")

#Body Geo Movement
cmds.select("Body_Bottom")
cmds.xform(r=True, t=[0, 2, 0])
cmds.select("Body_Middle")
cmds.xform(r=True, t=[0, 4.5, 0])
cmds.select("Body_Top")
cmds.xform(r=True, t=[0, 6.5, 0])

#Face Geo creation
cmds.polySphere(r=0.1, sx=6, sy=6, ax=[0, 2, 0], cuv=2, ch=1, n="Eye_Right")
cmds.polySphere(r=0.1, sx=6, sy=6, ax=[0, 2, 0], cuv=2, ch=1, n="Eye_Left")
cmds.polyCone(r=0.1, h=2, sx=20, sy=1, sz=0, ax=[0, 1, 0], cuv=3, ch=1, n="Nose")

#Face Geo Movement
cmds.select("Eye_Right")
cmds.xform(r=True, t=[-0.2, 6.75, 0.95], ro=[90, 0, 0])
cmds.select("Eye_Left")
cmds.xform(r=True, t=[0.2, 6.75, 0.95], ro=[90, 0, 0])
cmds.select("Nose")
cmds.xform(r=True, t=[0, 6.5, 1.4], ro=[90, 0, 0], s=[1, 0.475, 1])

#Face Geo Smoothing
cmds.polySoftEdge("Eye_Right", a=180, ch=1)
cmds.polySoftEdge("Eye_Left", a=180, ch=1)

#Chest Geo creation
cmds.polySphere(r=0.15, sx=10, sy=10, ax=[0, 1, 0], cuv=2, ch=1, n="Dot01")
cmds.polySphere(r=0.15, sx=10, sy=10, ax=[0, 1, 0], cuv=2, ch=1, n="Dot02")
cmds.polySphere(r=0.15, sx=10, sy=10, ax=[0, 1, 0], cuv=2, ch=1, n="Dot03")
cmds.polySphere(r=0.15, sx=10, sy=10, ax=[0, 1, 0], cuv=2, ch=1, n="Dot04")
cmds.polySphere(r=0.15, sx=10, sy=10, ax=[0, 1, 0], cuv=2, ch=1, n="Dot05")
cmds.polyCylinder(r=0.1, h=2.5, sx=8, sy=1, sz=1, ax=[0, 1, 0], rcp=True, cuv=3, ch=1, n="Arm_Right")
cmds.polyCylinder(r=0.1, h=2.5, sx=8, sy=1, sz=1, ax=[0, 1, 0], rcp=True, cuv=3, ch=1, n="Arm_Left")

#Chest Geo Movement
cmds.select("Dot01")
cmds.xform(r=True, t=[0, 5.3, 1.2], ro=[60, 0, 0])
cmds.select("Dot02")
cmds.xform(r=True, t=[0, 4.7, 1.4], ro=[90, 0, 0])
cmds.select("Dot03")
cmds.xform(r=True, t=[0, 4, 1.35], ro=[113, 0, 0])
cmds.select("Dot04")
cmds.xform(r=True, t=[0, 3.323, 1.418], ro=[51, 0, 0])
cmds.select("Dot05")
cmds.xform(r=True, t=[0, 2.7, 1.8], ro=[70, 0, 0])
cmds.select("Arm_Right")
cmds.xform(r=True, t=[2.4, 5.5, 0], ro=[0, 0, -53])
cmds.select("Arm_Left")
cmds.xform(r=True, t=[-2.4, 5.5, 0], ro=[0, 0, 53])

#Chest Geo Smoothing
cmds.polySoftEdge("Dot01", a=180, ch=1)
cmds.polySoftEdge("Dot02", a=180, ch=1)
cmds.polySoftEdge("Dot03", a=180, ch=1)
cmds.polySoftEdge("Dot04", a=180, ch=1)
cmds.polySoftEdge("Dot05", a=180, ch=1)

#Hat Geo creation
cmds.polyCylinder(r=0.85, h=1.2, sx=20, sy=2, sz=1, ax=[0, 1, 0], cuv=3, ch=1, n="Hat")

#Hat Geo Movement
cmds.select("Hat")
cmds.xform(r=True, t=[0, 7.78, 0])
cmds.move( 0, -0.497605, 0, "Hat.e[20:39]", r=True)
cmds.polyExtrudeFacet("Hat.f[0:19]", ch=1, kft=1, pvx=-8.940696716e-08, pvy=7.231118525, pvz=-1.490116119e-07,
                      d=1, twt=0, tp=1, off=0, tk=0, sma=30,)
cmds.setAttr("polyExtrudeFace1.localTranslate", 0, 0, 0.25276, type="double3")
cmds.select(clear=True)