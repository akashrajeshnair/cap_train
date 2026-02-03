import seaborn as sns
import matplotlib.pyplot as plt

plt.plot([0,1],[10,11], label='line 1')
plt.plot([0,1], [11,10], label='line 2')
plt.scatter([0,1],[10.5, 10.5], color='blue', marker='o', label='Dots')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('simple line and dot plot')
plt.legend()
plt.show()