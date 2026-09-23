import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # a = np.ndarray([np.asarray(x) for x in A])
    a = np.asarray(A)
    return a.T
