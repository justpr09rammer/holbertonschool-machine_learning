#!/usr/bin/env python3
"""
6-bars.py
Plots a stacked bar graph of fruit quantities per person
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph representing the amount and types of fruit
    each person possesses.

    - Columns of fruit: Farrah, Fred, Felicia
    - Rows of fruit: apples, bananas, oranges, peaches
    - Bars are stacked in the same order as the fruit rows
    - Colors: apples=red, bananas=yellow, oranges=#ff8000, peaches=#ffe5b4
    - Bar width: 0.5
    - Y-axis labeled 'Quantity of Fruit'
    - Y-axis ranges from 0 to 80, ticks every 10 units
    - Title: 'Number of Fruit per Person'
    """
    # Seed random generator and create fruit data
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    people = ['Farrah', 'Fred', 'Felicia']
    fruit_names = {
        'apples': 'red',
        'bananas': 'yellow',
        'oranges': '#ff8000',
        'peaches': '#ffe5b4'
    }
    bottom = np.zeros(len(people))
    # Loop through fruit types in order and plot stacked bars
    for i, (name, color) in enumerate(fruit_names.items()):
        plt.bar(
            np.arange(len(people)),
            fruit[i],
            width=0.5,
            bottom=bottom,
            color=color,
            label=name
        )
        bottom += fruit[i]
    # Set x-ticks and labels
    plt.xticks(np.arange(len(people)), people)
    # Set y-axis limits and ticks
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    # Labels and title
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.show()
