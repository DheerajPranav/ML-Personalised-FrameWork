__author__ = 'Dheeraj'

import numpy as np


class KNearestNeighbours:
    def __init__(self, k_neighbours):
        """
        1. epochs: no of iterations
        2. learning-rate: To penalize weights step wise
        """
        self.k = k_neighbours

    def train(self):
        return

    # noinspection PyAttributeOutsideInit
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

        self.m, self.n = self.x_train.shape
        return self

    # noinspection PyAttributeOutsideInit
    def predict(self, x_test):
        self.m_test, self.n = x_test.shape

        self.y_predict = np.zeros(self.m_test)

        # Lets find nearest neighbours for each record/input
        for i in range(x_test):
            x = x_test[i]

            # get K-nearest neighbours for current input
            neighbours = np.zeros(self.k)

    def modify_weights(self):
        pass
