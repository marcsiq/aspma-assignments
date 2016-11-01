import loadTestCases
import A6Part1
import A6Part2
import A6Part3
import A6Part4

import matplotlib.pyplot as plt
import numpy as np

print "A6Part1 test 1..."
#f0 = A6Part1.estimateF0()
print "-------------------"

print "A6Part2 test 1..."
p21 = loadTestCases.load(2,1)
inputFile = p21['input']['inputFile']
stdThsld = p21['input']['stdThsld']
minNoteDur = p21['input']['minNoteDur']
winStable = p21['input']['winStable']
window = p21['input']['window']
M = p21['input']['M']
N = p21['input']['N']
H = p21['input']['H']
f0et = p21['input']['f0et']
t = p21['input']['t']
minf0 = p21['input']['minf0']
maxf0 = p21['input']['maxf0']
#segments = A6Part2.segmentStableNotesRegions(inputFile, stdThsld, minNoteDur, 
#                              winStable, window, M, N, H, f0et, t, 
#                              minf0, maxf0)
print "-------------------"

print "A6Part2 test 2..."
p22 = loadTestCases.load(2,2)
inputFile = p22['input']['inputFile']
stdThsld = p22['input']['stdThsld']
minNoteDur = p22['input']['minNoteDur']
winStable = p22['input']['winStable']
window = p22['input']['window']
M = p22['input']['M']
N = p22['input']['N']
H = p22['input']['H']
f0et = p22['input']['f0et']
t = p22['input']['t']
minf0 = p22['input']['minf0']
maxf0 = p22['input']['maxf0']
#segments = A6Part2.segmentStableNotesRegions(inputFile, stdThsld, minNoteDur, 
#                              winStable, window, M, N, H, f0et, t, 
#                              minf0, maxf0)
print "-------------------"

print "A6Part2 test 3..."
p23 = loadTestCases.load(2,3)
inputFile = p23['input']['inputFile']
stdThsld = p23['input']['stdThsld']
minNoteDur = p23['input']['minNoteDur']
winStable = p23['input']['winStable']
window = p23['input']['window']
M = p23['input']['M']
N = p23['input']['N']
H = p23['input']['H']
f0et = p23['input']['f0et']
t = p23['input']['t']
minf0 = p23['input']['minf0']
maxf0 = p23['input']['maxf0']
#segments = A6Part2.segmentStableNotesRegions(inputFile, stdThsld, minNoteDur, 
#                              winStable, window, M, N, H, f0et, t, 
#                              minf0, maxf0)
print "-------------------"

print "A6Part3 test 1..."
p31 = loadTestCases.load(3,1)
inputFile = p31['input']['inputFile']
t1 = p31['input']['t1']
t2 = p31['input']['t2']
window = p31['input']['window']
M = p31['input']['M']
N = p31['input']['N']
H = p31['input']['H']
f0et = p31['input']['f0et']
t = p31['input']['t']
minf0 = p31['input']['minf0']
maxf0 = p31['input']['maxf0']
nH = p31['input']['nH']
print inputFile, t1, t2, window, M, N, H, f0et, t, minf0, maxf0, nH
inharmonicity = A6Part3.estimateInharmonicity(inputFile, t1, t2, window, 
                            M, N, H, f0et, t, minf0, maxf0, nH)
print "inharmonicity --> ", inharmonicity
print "-------------------"

print "A6Part3 test 2..."
p32 = loadTestCases.load(3,2)
inputFile = p31['input']['inputFile']
t1 = p32['input']['t1']
t2 = p32['input']['t2']
window = p32['input']['window']
M = p32['input']['M']
N = p32['input']['N']
H = p32['input']['H']
f0et = p32['input']['f0et']
t = p32['input']['t']
minf0 = p32['input']['minf0']
maxf0 = p32['input']['maxf0']
nH = p32['input']['nH']
print inputFile, t1, t2, window, M, N, H, f0et, t, minf0, maxf0, nH
inharmonicity = A6Part3.estimateInharmonicity(inputFile, t1, t2, window, 
                            M, N, H, f0et, t, minf0, maxf0, nH)
print "inharmonicity --> ", inharmonicity
print "-------------------"

print "A6Part3 test 3..."
p33 = loadTestCases.load(3,3)
inputFile = p33['input']['inputFile']
t1 = p33['input']['t1']
t2 = p33['input']['t2']
window = p33['input']['window']
M = p33['input']['M']
N = p33['input']['N']
H = p33['input']['H']
f0et = p33['input']['f0et']
t = p33['input']['t']
minf0 = p33['input']['minf0']
maxf0 = p33['input']['maxf0']
nH = p33['input']['nH']
print inputFile, t1, t2, window, M, N, H, f0et, t, minf0, maxf0, nH
inharmonicity = A6Part3.estimateInharmonicity(inputFile, t1, t2, window, 
                            M, N, H, f0et, t, minf0, maxf0, nH)
print "inharmonicity --> ", inharmonicity
print "-------------------"