import numpy as np
from scipy.optimize import minimize

def function(x):
    return x[0]**2 + x[1]**2 + 1

init_point = np.array([3.0, 1.0])
Optimum = minimize(function, init_point, method='CG', options={'xtol':1e-8, 'disp':True})
print(Optimum)
