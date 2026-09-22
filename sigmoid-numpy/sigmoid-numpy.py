import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    nx = np.asarray(x)
    nx = 1/(1+ np.exp(-nx))
    return nx.item() if nx.size == 1 else nx