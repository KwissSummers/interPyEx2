import numpy as numpy

randomFloats = numpy.random.rand(10)

meanVal = numpy.mean(randomFloats)
medianVal = numpy.median(randomFloats)
standardDeviation = numpy.std(randomFloats)

print("Random Floats", randomFloats)
print("Mean", meanVal)
print("Median", medianVal)
print("Standard Deviation", standardDeviation)
