import pandas as pd
import numpy as np
data = {
    'Age': [25, np.nan, 30, 22, np.nan],
    'City': ['Delhi', 'Mumbai', np.nan, 'Chennai', 'Delhi']
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
age_values = [x for x in df['Age'] if not pd.isnull(x)]
mean_age = sum(age_values) / len(age_values)
df['Age_Imputed'] = [x if not pd.isnull(x) else mean_age for x in df['Age']]
city_values = [x for x in df['City'] if not pd.isnull(x)]
mode_city = max(set(city_values), key=city_values.count)
df['City_Imputed'] = [x if not pd.isnull(x) else mode_city for x in df['City']]

print("\nAfter Manual Imputation:\n", df)
