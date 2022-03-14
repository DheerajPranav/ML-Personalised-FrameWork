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
        y_pred = (self.weights * self.x) + self.bias

        # Calculating derivatives w.r.t Parameters
        weightsD = (-2/self.n)*sum(self.x * (self.y - y_pred))
        biasD = (-1/self.n)*sum(self.y-y_pred)

        pass
