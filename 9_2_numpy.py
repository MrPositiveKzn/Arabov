# import numpy as np
#
# X = np.ones((5,5))
# print(X)
# X = np.pad(X, pad_width=1, mode = 'constant', constant_values=0)
# print(X)

import numpy as np

X = np.ones((5,5))
print(X)
X[:,[0, -1]] = 0
X[[0, -1], :] = 0
print(X)