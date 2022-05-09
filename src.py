import numpy as np
import matplotlib.pyplot as plt

n = 0
xarr = []
yarr = []
while (n < 10) :
    xarr.append(n)
    yarr.append(n+1)
    n += 1

plt.plot(xarr, yarr)
plt.show()
