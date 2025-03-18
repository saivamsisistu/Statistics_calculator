import matplotlib.pyplot as plt

def plot_boxplot(data, title="Boxplot"):
    """
    Plots a boxplot to visualize outliers and distribution.
    """
    plt.figure(figsize=(8, 5))
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    plt.title(title)
    plt.ylabel("Values")
    plt.grid(True)
    plt.show()
