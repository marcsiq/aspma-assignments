import loadTestCases
import A5Part1
import A5Part2
import A5Part3
import A5Part4
import A5Part5

import matplotlib.pyplot as plt
import numpy as np

print "A5Part1 test 1..."
p11 = loadTestCases.load(1,1)
inputFile = p11['input']['inputFile']
f = p11['input']['f']
fest, M, N = A5Part1.minFreqEstErr(inputFile, f)
print("best value in freq {0} is M={1}, N={2}".format(fest, M, N))
print "-------------------"

print "A5Part1 test 2..."
p12 = loadTestCases.load(1,2)
inputFile = p12['input']['inputFile']
f = p12['input']['f']
fest, M, N = A5Part1.minFreqEstErr(inputFile, f)
print("best value in freq {0} is M={1}, N={2}".format(fest, M, N))
print "-------------------"

print "A5Part1 test 3..."
p13 = loadTestCases.load(1,3)
inputFile = p13['input']['inputFile']
f = p13['input']['f']
fest, M, N = A5Part1.minFreqEstErr(inputFile, f)
print("best value in freq {0} is M={1}, N={2}".format(fest, M, N))
print "-------------------"

print "A5Part2 test 1..."
fest, M, N = A5Part1.minFreqEstErr(inputFile, f)
M, H, tStamps, fTrackEst, fTrackTrue = A5Part2.chirpTracker()
print "-------------------"

print "A5Part3 test 1..."
window, t, tStamps, fTrackEst, fTrackTrue = A5Part3.mainlobeTracker()
print "-------------------"

print "A5Part4 test 1..."
tStamps, tfreq = A5Part4.sineModelAnalEnhanced()
print "-------------------"
