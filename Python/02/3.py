import numpy as np


def find_equal_lines(A, B):
    B = B[:, np.newaxis, :]
    C = A == B
    C_temp = C.reshape(C.shape[0]*C.shape[1], -1).copy()
    C_temp = np.all(C_temp, axis=1).reshape(-1, A.shape[0])
    res = set(np.argwhere(C_temp.ravel()).ravel() % A.shape[0])
    return np.array(list(res))
