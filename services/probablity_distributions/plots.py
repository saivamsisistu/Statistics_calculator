import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def plot_pdf(dist_func, params, x_range=(-5, 5), title="PDF Graph"):
    """Plots Probability Density Function."""
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = dist_func(x, **params)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="PDF")
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_cdf(dist_func, params, x_range=(-5, 5), title="CDF Graph"):
    """Plots Cumulative Distribution Function."""
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = dist_func(x, **params)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="CDF", color="red")
    plt.xlabel("x")
    plt.ylabel("Cumulative Probability")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
