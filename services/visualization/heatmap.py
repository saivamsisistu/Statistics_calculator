import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_heatmap(dataframe, title="Correlation Heatmap"):
    """
    Plots a heatmap for correlation matrix.
    """
    plt.figure(figsize=(8, 5))
    sns.heatmap(dataframe.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title(title)
    plt.show()
