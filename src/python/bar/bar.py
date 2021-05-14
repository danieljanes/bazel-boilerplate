import numpy as np


def greeting() -> str:
    return "Hello from `bar` and NumPy " + str(np.ones(3))
