#!/usr/bin/env python3
"""
0-line.py
Plot y = x^3 as a solid red line from x = 0 to 10
"""


def line():
    """
    Plots a line graph of y = x^3 for x values from 0 to 10.

    - y is plotted as a solid red line
    - x-axis ranges from 0 to 10
    - Includes labels and title for clarity
    """

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, 'r-')
    plt.xlim((0, 10))
    plt.show()
