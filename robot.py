import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy


class ROBOT:
    def __init__(self):
        self.motor = MOTOR()
        self.sensor = SENSOR()
        self.robotID = p.loadURDF("body.urdf")
        self.motors = {}
        self.sensors = {}
        pyrosim.Prepare_To_Simulate(self.robotID)
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, i):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)
    def Prepare_to_Act(self):
        pass
    def Act(self):
        self.motor.Set_Value()
