#Emma Patton, 2018-10-07
#2D Plot Practice - Scatter Plots 

import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, "r.")
plt.plot(x, y, "b-")

plt.show()
