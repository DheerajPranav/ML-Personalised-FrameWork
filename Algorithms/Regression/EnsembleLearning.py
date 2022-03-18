__author__ = 'Dheeraj`, Venkat'

import numpy as np


class RandomForest:
    def __init__(self, learning_rate=0.01, epochs=1000):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.lr = learning_rate
        self.epochs = epochs

    def train(self):
        return

    def fit(self, x, y):
        return self

    def modify_weights(self):
        pass


class DecisionTreeRegressor:
    def __init__(self, learning_rate=0.01, epochs=1000):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.lr = learning_rate
        self.epochs = epochs

    def train(self):
        return

    def fit(self, x, y):
        return self

    def modify_weights(self):
        pass


class XGBoostRegressor:
    def __init__(self, learning_rate=0.01, epochs=1000):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.lr = learning_rate
        self.epochs = epochs

    def train(self):
        return

    def fit(self, x, y):
        return self

    def modify_weights(self):
        pass
