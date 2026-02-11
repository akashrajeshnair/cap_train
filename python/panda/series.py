import pandas as pd
import numpy as np

s = pd.Series()
print('pandas series: ', s)
data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print("pandas series: \n", s)