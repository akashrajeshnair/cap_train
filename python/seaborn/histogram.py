import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(1000)
plt.figure(figsize=(8,5))

sns.histplot(data, kde=True, bins=30, color='purple')

mean_value = np.mean(data)
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2)
plt.text(mean_value + 0.1, 50, f'mean: {mean_value:2f}', color='red')
plt.title('distribution with seaborn and matplotlib customization')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()