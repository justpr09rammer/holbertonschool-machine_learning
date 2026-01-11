#!/usr/bin/env python3
"""
2-change_scale.py
Plots the exponential decay of Carbon-14
"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plots x ↦ y as a line graph where:
    - x-axis is Time (years)
    - y-axis is Fraction Remaining
    - y-axis is logarithmically scaled
    - x-axis ranges from 0 to 28650
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y)
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of C-14')
    plt.yscale('log')
    plt.xlim(0, 28650)
    plt.show()
