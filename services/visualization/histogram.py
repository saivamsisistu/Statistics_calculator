import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, bins=10, title="Histogram", xlabel="Values"):
    """
    Plots a histogram to show the distribution of data.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, color='purple', alpha=0.7, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.title(title)
    plt.grid(True)
    plt.show()
