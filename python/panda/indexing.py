import pandas as pd
import numpy as np

# position based indexing
data = np.array(['a', 'k', 'a', 's', 'h'])
ser = pd.Series(data)
print(ser[:5])

# label based indexing
ser = pd.Series(data, index=[10,11,12,13,14])
print(ser[10])