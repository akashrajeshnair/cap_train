import json
import pandas as pd
from pandas import json_normalize

with open('s') as f:
    d = json.load(f)

nycphil = json_normalize(d['programs'])
nycphil.head(3)