import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues.npy')
frontLegSensorValues = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/frontLegvalues.npy')
targetAngles = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/targetAngles.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg',linewidth=2)
#matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg',linewidth=1)
matplotlib.pyplot.plot(targetAngles, label='Target Angles',linewidth=1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()