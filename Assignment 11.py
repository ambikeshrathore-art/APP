import pandas as pd
import numpy as np

numbers = np.random.randint(1, 100, 10)

series = pd.Series(numbers)

print(series)
