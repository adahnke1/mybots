import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
    def Prepare_To_Act(self):
        self.motors = {}
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    def Set_Value(self, robotID, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotID,jointName = self.jointName,controlMode = p.POSITION_CONTROL,targetPosition = self.motorValues,maxForce = 500)
        pass
    def Save_Values():
        #numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues', backLegSensorValues, allow_pickle = True, fix_imports = True)
        #numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues', frontLegSensorValues, allow_pickle = True, fix_imports = True)
        pass