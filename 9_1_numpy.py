import numpy as np

print(np.allclose([2,5], [6,31]))
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([22,25], [23,26]))
print(np.allclose([1.0, np.nan], [1.0, np.nan]))
print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))