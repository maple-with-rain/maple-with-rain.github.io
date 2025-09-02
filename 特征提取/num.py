import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def input_data():
    data = np.ones(6)
    return data
def read_data():
    digit_1 = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0]
    ])
    digit_2 = np.array([
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
    ])