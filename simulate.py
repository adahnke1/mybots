import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/600)
    print(i)
p.disconnect()
