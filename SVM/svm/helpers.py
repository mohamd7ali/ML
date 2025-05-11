import numpy as np
from sklearn import datasets


# helper for SVM exercise

''' Gives a simple toy dataset.'''
def get_simple_dataset():
    # create a toy dataset
    np.random.seed(1)
    X, Y = datasets.make_blobs(n_samples=100, centers=2, n_features=2, center_box=(0, 10))
    return X,Y

'''Gives two circluar dataset'''
def get_circle_dataset():
    np.random.seed(0)
    X,Y = datasets.make_circles(n_samples=100, factor=.5,
                                      noise=.05)
    return X,Y