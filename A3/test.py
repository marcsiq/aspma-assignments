import loadTestCases
import A3Part1
import A3Part2
import A3Part3
import A3Part4
import matplotlib.pyplot as plt
import numpy as np
"""
print "A3Part1 test 1..."
p11 = loadTestCases.load(1,1)
x = p11['input']['x']
fs = p11['input']['fs']
f1 = p11['input']['f1']
f2 = p11['input']['f2']
mX = A3Part1.minimizeEnergySpreadDFT(x, fs, f1, f2)
plt.figure(1)
plt.plot(mX)
plt.show()
print "-------------------"

print "A3Part1 test 2..."
p12 = loadTestCases.load(1,2)
x = p12['input']['x']
fs = p12['input']['fs']
f1 = p12['input']['f1']
f2 = p12['input']['f2']
mX = A3Part1.minimizeEnergySpreadDFT(x, fs, f1, f2)
plt.figure(2)
plt.plot(mX)
plt.show()
print "-------------------"

print "A3Part2 test 1..."
p21 = loadTestCases.load(2,1)
x = p21['input']['x']
fs = p21['input']['fs']
f = p21['input']['f']
mX = A3Part2.optimalZeropad(x, fs, f)
plt.figure(3)
plt.plot(mX)
plt.show()
print "-------------------"

print "A3Part2 test 2..."
p22 = loadTestCases.load(2,2)
x = p22['input']['x']
fs = p22['input']['fs']
f = p22['input']['f']
mX = A3Part2.optimalZeropad(x, fs, f)
plt.figure(4)
plt.plot(mX)
plt.show()
print "-------------------"


print "A3Part3 test 1..."
p31 = loadTestCases.load(3,1)
x = p31['input']['x']
re, dftbuffer, X = A3Part3.testRealEven(x)
print "real and even: " + str(re) 
print "dftbuffer: " + str(dftbuffer) 
print "X: " + str(X)
print "-------------------"

print "A3Part3 test 2..."
p32 = loadTestCases.load(3,2)
x = p32['input']['x']
re, dftbuffer, X = A3Part3.testRealEven(x)
print "real and even: " + str(re) 
print "dftbuffer: " + str(dftbuffer) 
print "X: " + str(X)
print "-------------------"
"""
print "A3Part4 test 1..."
p41 = loadTestCases.load(4,1)
x = p41['input']['x']
fs = p41['input']['fs']
N = p41['input']['N']
Y, Yfilt = A3Part4.suppressFreqDFTmodel(x, fs, N)
outY = p41['output'][0]
outYfilt = p41['output'][1]

print np.array_equal(Y, outY)
print np.array_equal(Yfilt, outYfilt)

plt.figure(6)
plt.plot(Y)
plt.show(block = False)

plt.figure(7)
plt.plot(Yfilt)
plt.show(block = False)
print "-------------------"

print "A3Part4 test 2..."
p42 = loadTestCases.load(4,2)
x = p42['input']['x']
fs = p42['input']['fs']
N = p42['input']['N']
Y, Yfilt = A3Part4.suppressFreqDFTmodel(x, fs, N)
outY = p42['output'][0]
outYfilt = p42['output'][1]

print np.array_equal(Y, outY)
print np.array_equal(Yfilt, outYfilt)

plt.figure(8)
plt.plot(Y)
plt.show(block = False)

plt.figure(9)
plt.plot(Yfilt)
plt.show()
print "-------------------"