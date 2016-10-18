import loadTestCases
import A4Part1
import A4Part2

import matplotlib.pyplot as plt
import numpy as np


print "A4Part1 test 1..."
p11 = loadTestCases.load(1,1)
window = p11['input']['window']
M = p11['input']['M']
out = p11['output']
mainlobe = A4Part1.extractMainLobe(window, M)
plt.figure(1)
plt.plot(mainlobe)
plt.show()
print "-------------------"

print "A4Part1 test 2..."
p12 = loadTestCases.load(1,2)
window = p12['input']['window']
M = p12['input']['M']
out = p12['output']
mainlobe = A4Part1.extractMainLobe(window, M)
plt.figure(2)
plt.plot(mainlobe)
plt.show()
print "-------------------"

print "A4Part1 test 3..."
p13 = loadTestCases.load(1,3)
window = p13['input']['window']
M = p13['input']['M']
out = p13['output']
mainlobe = A4Part1.extractMainLobe(window, M)
plt.figure(3)
plt.plot(mainlobe)
plt.show()
print "-------------------"

print "A4Part2 test 1..."
p21 = loadTestCases.load(2,1)
inputFile = p21['input']['inputFile']
window = p21['input']['window']
M = p21['input']['M']
N = p21['input']['N']
H = p21['input']['H']
SNR1, SNR2 = A4Part2.computeSNR(inputFile, window, M, N, H)
print SNR1, SNR2
print "-------------------"

print "A4Part2 test 2..."
p22 = loadTestCases.load(2,2)
inputFile = p22['input']['inputFile']
window = p22['input']['window']
M = p22['input']['M']
N = p22['input']['N']
H = p22['input']['H']
SNR1, SNR2 = A4Part2.computeSNR(inputFile, window, M, N, H)
print SNR1, SNR2
print "-------------------"

print "A4Part2 test 3..."
p23 = loadTestCases.load(2,3)
inputFile = p23['input']['inputFile']
window = p23['input']['window']
M = p23['input']['M']
N = p23['input']['N']
H = p23['input']['H']
SNR1, SNR2 = A4Part2.computeSNR(inputFile, window, M, N, H)
print SNR1, SNR2
print "-------------------"