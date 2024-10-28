import numpy as np
import pandas as pd

t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

data = pd.DataFrame({'t': t, 'sin(t)': sin_t, 'cos(t)': cos_t})
print(data.head())