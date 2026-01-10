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
    # Generate x values from 0 to 10
    x = np.arange(0, 11)
    
    # Compute y = x^3
    y = x ** 3

    # Create a new figure with default size
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot y vs x as a solid red line
    plt.plot(x, y, 'r-', linewidth=2)
    
    # Add x and y axis labels
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Add a title
    plt.title('y = x^3')
    
    # Display the plot
    plt.show()
