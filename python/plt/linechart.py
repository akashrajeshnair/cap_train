import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temp = [22,24,23,26,25]

plt.plot(days, temp, marker='o')
plt.title("Weekly temperature")
plt.xlabel('Days')
plt.ylabel('Temperature(C)')
plt.show()