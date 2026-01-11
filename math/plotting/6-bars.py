#!/usr/bin/env python3
"""
6-bars.py
Plots a stacked bar graph of fruit quantities per person
"""

import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph where:
    - columns of fruit: Farrah, Fred, Felicia
    - rows of fruit: apples, bananas, oranges, peaches
    - stacked bars represent quantities of each fruit
    - colors: apples=red, bananas=yellow, oranges=#ff8000, peaches=#ffe5b4
    - bar width=0.5
    - y-axis labeled Quantity of Fruit
    - y-axis range 0-80, ticks every 10
    - title: Number of Fruit per Person
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    bottom = np.zeros(3)
    for i in range(fruit.shape[0]):
        plt.bar(people, fruit[i], bottom=bottom, color=colors[i], width=0.5, label=['Apples','Bananas','Oranges','Peaches'][i])
        bottom += fruit[i]
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.show()

