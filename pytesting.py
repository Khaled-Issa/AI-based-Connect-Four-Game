import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y = np.exp(x)

z = np.sin(x)

fig1, ax1 = plt.subplots()
ax1.plot(x, y)


fig2, ax = plt.subplots(nrows=2, ncols=1) # two axes on figure
for i in ax:
	i.plot(x,z)

plt.show()
