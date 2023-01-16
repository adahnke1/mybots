import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)
for i in range(500):
    p.stepSimulation()
    time.sleep(1/600)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
print(backLegSensorValues)
print(frontLegSensorValues)
numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues', backLegSensorValues, allow_pickle = True, fix_imports = True)
numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues', frontLegSensorValues, allow_pickle = True, fix_imports = True)
p.disconnect()
