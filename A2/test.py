import sys
import os
sys.path.append('../../software/models/')
import A2Part1
import A2Part2
import A2Part3
import A2Part4
import A2Part5
import numpy as np

print "A2Part1 test..."
A=1.0
f = 10.0
phi = 1.0
fs = 50.0
t = 0.1
x = A2Part1.genSine(A, f, phi, fs, t)
print "sine = " + str(x)
print "-------------------"

print "A2Part2 test..."
N=5
k=1
x = A2Part2.genComplexSine(k, N)
print "complex sine = " + str(x)
print "-------------------"

print "A2Part3 test..."
x = np.array([1,2,3,4])
dftx = A2Part3.DFT(x)
print "X = " + str(dftx)
print "-------------------"

print "A2Part4 test..."
X = np.array([1 ,1 ,1 ,1])
x = A2Part4.IDFT(X)
print "x = " + str(x)
print "-------------------"

print "A2Part5 (optional) test..."
x = np.array([1,2,3,4])
mx = A2Part5.genMagSpec(x)
print "mx = " + str(mx)
print "-------------------"