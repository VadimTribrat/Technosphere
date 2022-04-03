import numpy as np


def collect_votes(votes):
    led = np.bincount(np.ravel(votes[votes > 0]))
    res = (votes.T + range(0, 6*votes.shape[0], 6)).T
    res = np.bincount(np.ravel(res), minlength=6*votes.shape[0])
    res = np.delete(res.reshape(-1, 6), 0, 1)
    return (np.argmax(led), np.argmax(res, axis=1) + 1)
