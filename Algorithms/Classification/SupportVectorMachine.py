__author__ = 'Dheeraj'

import numpy as np


class SVM:
    def __init__(self, kernel=0.01, points=1000):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.lr = kernel
        self.epochs = points

        self.m, self.n = 0, 0
        self.weights, self.bias = 0, 0
        self.x, self.y = np.array([]), np.array([])

    def train(self):
        return

    def fit(self, x, y):
        self.x, self.y = x, y

        # no_of_training_examples -> m, no_of_features -> n
        self.m, self.n = x.shape

        # parameter initialization
        self.weights = np.zeros(self.n)
        self.bias = np.zeros(self.n)

        # Iterate through no of iterations/epochs mentioned to update weights using gradient descent way.
        for iteration in range(self.epochs):
            self.modify_weights()

        return self

    def modify_weights(self):
        pass
