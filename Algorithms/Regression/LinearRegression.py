__author__ = 'Dheeraj'

import numpy as np


class LinearRegression:
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
        """
        Model-Fitting with certain parameters , after penalizing them properly
        """
        self.x, self.y = x, y

        # no_of_training_examples -> m, no_of_features -> n
        self.m, self.n = x.shape

        # initialize parameter/weights
        self.weights = np.zeros(self.n)
        self.bias = 0

        # Iterate through no of iterations/epochs mentioned to update weights
        # using gradient descent way.
        for iteration in range(self.epochs):
            self.modify_weights()

        return self

    def modify_weights(self):
        y_pred = self.predict(self.x)

        # Calculating derivatives w.r.t Parameters
        weightsD = (-2/self.n) * sum(self.x * (self.y - y_pred))
        biasD = (-1/self.n) * sum(self.y-y_pred)

        # update weights
        self.weights = self.weights - self.lr * weightsD
        self.bias = self.bias - self.lr * biasD

    def predict(self, x):
        """
        Predict the result based in input feature provided: x , along with parameters
        Here we use equation: y = (m * x) + c
        y : output
        x : input
        m : slope
        c : bias
        """
        y_pred = x * self.weights + self.bias
        return y_pred
