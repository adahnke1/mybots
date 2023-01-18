import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues.npy')
frontLegSensorValues = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues.npy')
FrontLegtargetAngles = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/FrontLegtargetAngles.npy')
BackLegtargetAngles = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/BackLegtargetAngles.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg',linewidth=2)
#matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg',linewidth=1)
matplotlib.pyplot.plot(FrontLegtargetAngles, label='Target Angles',linewidth=1)
matplotlib.pyplot.plot(BackLegtargetAngles, label='Target Angles',linewidth=1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()