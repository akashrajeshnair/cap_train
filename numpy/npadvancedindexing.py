import numpy as np

a = np.array([10,20,30,40,50,60])
idx = np.array([1,3,5])
print(a[idx])

cond = a > 30
print(a[cond])