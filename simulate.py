import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION
from robot import ROBOT
from world import WORLD
#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0,0,-9.8)
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
#pyrosim.Prepare_To_Simulate(robotId)
#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)
#for i in range(1000):
#    p.stepSimulation()
#    time.sleep(1/600)
#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b"Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = c.BackLegtargetAngles[i],maxForce = 500)
#    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b"Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = c.FrontLegtargetAngles[i],maxForce = 500)
#print(backLegSensorValues)
#print(frontLegSensorValues)
#numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues', backLegSensorValues, allow_pickle = True, fix_imports = True)
#numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues', frontLegSensorValues, allow_pickle = True, fix_imports = True)
#numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/BackLegtargetAngles', (c.BackLegtargetAngles), allow_pickle = True, fix_imports = True)
#numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/FrontLegtargetAngles', (c.FrontLegtargetAngles), allow_pickle = True, fix_imports = True)
#p.disconnect()
simulation = SIMULATION()
simulation.Run()

