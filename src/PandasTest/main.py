import pandas as pd
import numpy as np

my_numpy_array = np.random.rand(3)

my_series = pd.Series(my_numpy_array, index=['First', 'Second', 'Third'])

print(my_numpy_array[0])
print(my_series['Second'])