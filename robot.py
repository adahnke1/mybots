import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
p.setAdditionalSearchPath(pybullet_data.getDataPath())

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        pyrosim.Prepare_To_Simulate(self.robotId)