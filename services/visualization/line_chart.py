import matplotlib.pyplot as plt

def plot_line_chart(x, y, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
    """
    Plots a simple line chart.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Line Chart")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
