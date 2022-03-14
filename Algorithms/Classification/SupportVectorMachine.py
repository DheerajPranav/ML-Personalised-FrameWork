__author__ = 'Dheeraj'

import numpy as np


class SVM:
    def __init__(self, learning_rate=0.01, epochs=1000):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.lr = learning_rate
        self.epochs = epochs

        self.m, self.n = 0, 0
        self.weights, self.bias = 0, 0
        self.x, self.y = np.array([]), np.array([])

    def train(self):
        return

    def fit(self, x, y):
        return self

    def modify_weights(self):
        pass
