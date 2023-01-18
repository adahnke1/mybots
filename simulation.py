from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim




class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)
    def Run(self):
        for i in range(1000):
            print(i)
#       p.stepSimulation()
#       time.sleep(1/600)
#       backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#       frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#       pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b"Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = c.BackLegtargetAngles[i],maxForce = 500)
#       pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b"Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = c.FrontLegtargetAngles[i],maxForce = 500)
