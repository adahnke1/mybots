import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('/Users/adahnke1/Documents/GitHub/mybots/data/backLegvalues.npy')
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()