__author__ = 'Dheeraj'

import numpy as np
from scipy.stats import mode


class KNearestNeighbours:
    def __init__(self, k_neighbours, distance_metric: str = 'euclidean'):
        """
        1. k neighbours: No of nearest neighbours tot be considered ,
           while assigning final class-label.
        2. distance_metric: Way to calculate distance between two points
           - Euclidean
           - Manhattan
        """
        self.k = k_neighbours
        self.distance_metric = distance_metric

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

        y_predict = np.zeros(self.m_test)

        # Let's find nearest neighbours for each record/input
        for i in range(x_test):
            x = x_test[i]

            # get K-nearest neighbours for current input
            # neighbours = np.zeros(self.k)
            neighbours = self.___get_neighbours(x)

            # Fetch the most repeated ones (mode) from the resulted ones
            y_predict[i] = mode(neighbours)[0][0]

    def ___get_neighbours(self, x):
        # Finding Distance score between our test sample and all training instances
        distances = np.zeros(self.m)
        for i in range(self.m):
            if self.distance_metric == 'euclidean':
                dist = self.euclidean_distance(x, self.x_train)
            else:
                dist = self.manhattan_distance(x, self.x_train)

            distances[i] = dist

        # Sorting our y-train based distance metric indexes to fetch k-nearest samples
        sorted_indexes = distances.argsort()
        y_train = self.y_train[sorted_indexes]
        k_samples = y_train[:self.k]
        return k_samples

    @staticmethod
    def euclidean_distance(x1, x2):
        return np.sqrt(np.sum(np.square(x1 - x2)))

    @staticmethod
    def manhattan_distance(x1, x2):
        """ This distance metric calculation is in progress"""
        return x1 + x2
