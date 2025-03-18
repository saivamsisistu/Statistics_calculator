import matplotlib.pyplot as plt
import numpy as np

def plot_bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values"):
    """
    Plots a bar chart.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='skyblue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()
