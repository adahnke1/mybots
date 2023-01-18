from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import constants as c



class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)
     #  print(self.robot.values)
    def Run(self):
        for i in range(1000):
            print(i)
            p.stepSimulation()
            time.sleep(1/60)
        p.disconnect()
