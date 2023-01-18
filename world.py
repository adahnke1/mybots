import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        