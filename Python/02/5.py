import numpy as np


def get_best_indices(ranks: np.ndarray, top: int, axis: int = 1) -> np.ndarray:
    """
    Returns indices of top largest values in rows of array.

    Parameters
    ----------
    ranks : np.ndarray, required
        Input array.
    top : int, required
        Number of largest values.
    """
    res = np.argpartition(ranks, -np.array(range(top + 1)), axis=axis)
    return np.flip(res.take(indices=range(-top, 0), axis=axis), axis=axis)


if __name__ == '__main__':
    with open('input.bin', 'rb') as f_data:
        ranks = np.load(f_data)
    res = get_best_indices(ranks, top=5)
    with open('output.bin', 'wb') as output:
        np.save(output, res)
