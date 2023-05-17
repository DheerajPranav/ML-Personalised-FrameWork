__author__ = 'Dheeraj'

import numpy as np


class LogisticRegression:
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
        # z = (x * w) + b
        z = (self.x.dot(self.weights) + self.bias)

        # Sigmoid is applied to get values in range (0, 1) and equation ==> 1 / (1 + (np.exp(-z)))
        y_pred = self.apply_sigmoid(z)

        # Calculating derivatives w.r.t Parameters
        weights_D = (-2 / self.n) * sum(self.x * (self.y - y_pred))
        bias_D = (-1 / self.n) * sum(self.y - y_pred)

    @staticmethod
    def apply_sigmoid(z):
        return 1 / (1 + (np.exp(-z)))
