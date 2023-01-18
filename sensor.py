import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

class SENSOR:
    def __init__(self, linkname):
        self.linkname = linkname
        self.values = numpy.zeros(1000)
        self.sensors = {}
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Get_Value(self, i): 
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        if i == 1000: 
            print(self.values)
    def Save_Values():
        #numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues', backLegSensorValues, allow_pickle = True, fix_imports = True)
        #numpy.save('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues', frontLegSensorValues, allow_pickle = True, fix_imports = True)
        pass

