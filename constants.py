import numpy
amplitude = (numpy.pi)/4
frequency = 3
phaseOffset = (numpy.pi)/4
BackLegamplitude = (numpy.pi)/8
BackLegfrequency = 3
BackLegphaseOffset = 0
targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
targetAngles = amplitude*numpy.sin(frequency*targetAngles+phaseOffset)
BackLegtargetAngles = BackLegamplitude*numpy.sin(BackLegfrequency*targetAngles+BackLegphaseOffset)