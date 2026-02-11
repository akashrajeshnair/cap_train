import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.5
size = 1000

data = np.random.binomial(n, p, size)
plt.hist(data, bins=np.arange(-0.5, n+1.5, 1), density=True, edgecolor='black', alpha=0.7, label='Histogram')
x = np.arange(0, n+1)
pmf = binom.pmf(x,n,p)

plt.scatter(x, pmf, color='red', label='Theoretical PMF')
plt.vlines(x, 0, pmf, colors='red', linestyles='dashed')

plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of succesess")
plt.ylabel("Probablity")
plt.legend()
plt.grid(True)
plt.show()