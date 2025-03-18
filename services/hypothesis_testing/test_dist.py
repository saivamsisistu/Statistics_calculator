import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def plot_distribution(sample, test_statistic, critical_value=None, test_type='t'):
    """
    Plots the distribution of the test and highlights critical regions.
    - sample: Data sample
    - test_statistic: Calculated test statistic
    - critical_value: Critical value for the test
    - test_type: 't' for T-Test, 'z' for Z-Test
    """
    plt.figure(figsize=(8, 5))

    # Generate x-axis range
    x = np.linspace(-4, 4, 1000) if test_type == 'z' else np.linspace(-4, 4, 1000)

    # Choose the correct distribution
    if test_type == 't':
        y = stats.t.pdf(x, df=len(sample) - 1)
        plt.title("T-Test Distribution")
    else:
        y = stats.norm.pdf(x)
        plt.title("Z-Test Distribution")

    plt.plot(x, y, label="Probability Density Function", color="blue")

    # Highlight critical region
    if critical_value:
        plt.axvline(x=critical_value, linestyle="--", color="red", label="Critical Value")

    # Mark the test statistic
    plt.axvline(x=test_statistic, linestyle="--", color="green", label="Test Statistic")

    plt.legend()
    plt.xlabel("Test Statistic Value")
    plt.ylabel("Probability Density")
    plt.show()
