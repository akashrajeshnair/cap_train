import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

x = [1,2,3,4,5]
y = [10,12,15,18,22]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Trend')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('matplotlib with seaborn theme')
plt.legend()
plt.show()