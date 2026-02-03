import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('basic histogram')
plt.show()