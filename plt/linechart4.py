import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = [3,6,9,12,15]

plt.plot(x,y, marker='o', linestyle='-', label='data points')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line plot")
plt.legend()
plt.show()