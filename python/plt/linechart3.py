import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = x*2

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line plot")
plt.show()