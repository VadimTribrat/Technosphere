import numpy as np


def equilibrium_sht(A, B):
    ind = np.array(np.argwhere(B.T == np.max(B, axis=1)))
    ind[:, 0], ind[:, 1] = ind[:, 1].copy(), ind[:, 0].copy()
    ind = np.array(ind)
    temp_ind = ind * np.array([B.shape[1], 1]).reshape(-1, 2)
    temp_ind = temp_ind.sum(axis=1)
    C = A.ravel()[temp_ind]
    ind2 = np.argwhere(C == np.max(C))
    res = ind[ind2].ravel().reshape(-1, 2).tolist()
    return (np.max(C), set([(a, b) for a, b in res]))
