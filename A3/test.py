import loadTestCases
import A3Part1
import A3Part2
import A3Part3
import matplotlib.pyplot as plt


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
dftbuffer, X = A3Part3.testRealEven(x)
print "x: " + str(x) 
print "dftbuffer: " + str(dftbuffer) 
print "X: " + str(X)
print "-------------------"

print "A3Part3 test 2..."
p32 = loadTestCases.load(3,2)
x = p32['input']['x']
dftbuffer, X = A3Part3.testRealEven(x)
print "x: " + str(x) 
print "dftbuffer: " + str(dftbuffer) 
print "X: " + str(X)
print "-------------------"