import numpy as np
from Backpropagation import Backpropagation

X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([[-1], [1], [1], [-1]])

model = Backpropagation(alpha=0.3, epoch=1000, target_error=0.001)
model.fit(X, t)