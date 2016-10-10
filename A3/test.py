import loadTestCases
import A3Part1
import matplotlib.pyplot as plt

p1 = loadTestCases.load(1,1)
x = p1['input']['x']
fs = p1['input']['fs']
f1 = p1['input']['f1']
f2 = p1['input']['f2']
mX = A3Part1.minimizeEnergySpreadDFT(x, fs, f1, f2)
plt.plot(mX)
plt.show()

p1 = loadTestCases.load(1,2)
x = p1['input']['x']
fs = p1['input']['fs']
f1 = p1['input']['f1']
f2 = p1['input']['f2']
mX = A3Part1.minimizeEnergySpreadDFT(x, fs, f1, f2)
plt.plot(mX)
plt.show()