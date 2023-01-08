import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
for i in range(10):
    for j in range(5):
        for k in range(5):
            pyrosim.Send_Cube(pos=[x+j,y+k,z+i] , size=[length,width,height])
    length = 0.9 * length
    width = 0.9 * width
    height = 0.9 * height
pyrosim.End()