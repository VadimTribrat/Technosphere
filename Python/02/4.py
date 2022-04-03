import numpy as np


def encode_rle(arr):
    arr = np.asarray(arr)
    dif = arr[1:] != arr[:-1]
    ind = np.append(np.where(dif), len(arr)-1)
    res = np.diff(np.append(-1, ind))
    return (arr[ind], res)
