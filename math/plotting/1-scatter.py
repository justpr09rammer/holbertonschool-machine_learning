#!/usr/bin/env python3
"""
1-scatter.py
Plots a scatter plot of men's height vs weight
"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Plots a scatter graph where:
    - x-axis represents Height (in)
    - y-axis represents Weight (lbs)
    - title is Men's Height vs Weight
    - points are magenta
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180

    plt.figure(figsize=(6.4, 4.8))

    # Scatter plot
    plt.scatter(x, y, c='m')

    # Labels and title
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')
    plt.title("Men's Height vs Weight")

    plt.show()

