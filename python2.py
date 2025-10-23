import pandas as pd
import numpy as np
data = {'Code': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Omega','Omega','Gamma','Beta','Delta']}
d = pd.DataFrame(data)
print("Original Data:\n", d)
#finding uniques values of codes among different codes
codes_list = list(d['Code'].unique())
E = pd.DataFrame()
for i in codes_list:
    E[f'code_{i}'] = [1 if val == i else 0 for val in data['Code']]
#here concat is used for joining the two data
d_encoded = pd.concat([d, E], axis=1)   
print("\nAfter One-Hot Encoding:\n", d_encoded)