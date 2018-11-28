# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:25:34 2018
@author: kevzo
"""

import numpy as np
from matplotlib import pyplot


def scatter(i, j):
    x = np.linspace(-np.pi, np.pi, num=i)
    y = np.array([np.sin(j*x) for j in range(j)]).sum(axis=0).clip(-1, 1)
    pyplot.scatter(x, y, s=.2)


def plot():
    i = 20000
    plots = 20
    j = np.arange(1, plots)
    for k in j:
        pyplot.subplot(plots, 1, k)
        scatter(i, k)
    pyplot.show()


plot()
