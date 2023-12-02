import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #used by loadURDF
p.setGravity(0,0,-9.81)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
time.sleep(5)
p.loadURDF("/robot.urdf",cubeStartPos, cubeStartOrientation, globalScaling = 0.1)
p.stepSimulation()
time.sleep(5000)
#p.disconnect()