#!/usr/bin/env python3
"""
0-line.py
Plots y = x^3 as a solid red line
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots a cubic line graph where:
    - y is plotted as a solid red line
    - x-axis ranges from 0 to 10
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    # Plot y with implicit x (0 to 10)
    plt.plot(y, 'r-')
    # Set x-axis range exactly from 0 to 10
    plt.xlim(0, 10)
    plt.show()
