import numpy
FrontLegamplitude = (numpy.pi)/4
FrontLegfrequency = 3
FrontLegphaseOffset = (numpy.pi)/4
BackLegamplitude = (numpy.pi)/8
BackLegfrequency = 3
BackLegphaseOffset = 0
targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
FrontLegtargetAngles = FrontLegamplitude*numpy.sin(FrontLegfrequency*targetAngles+FrontLegphaseOffset)
BackLegtargetAngles = BackLegamplitude*numpy.sin(BackLegfrequency*targetAngles+BackLegphaseOffset)