import sys
import os
sys.path.append('../../software/models/')
import A1Part1
import A1Part2
import A1Part3
import A1Part4
import numpy as np

print "A1Part1 test..."
x = A1Part1.readAudio('../../sounds/piano.wav')
print "x: " + str(x)
print "-------------------"

print "A1Part2 test..."
minx, maxx = A1Part2.minMaxAudio('../../sounds/oboe-A4.wav')
print "min: " + str(minx)
print "max: " + str(maxx)
print "-------------------"

print "A1Part3 test..."
x = np.arange(10)
M = 2
xhp = A1Part3.hopSamples(x,M)
print "x hoped: " + str(xhp)
print "-------------------"