import matplotlib.pyplot as plt

def plot_scatter(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Plots a scatter plot to show relationships between two variables.
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='r', alpha=0.7, label="Scatter Plot")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
