import matplotlib.pyplot as plt
import seaborn as sns
"""
1) regression line
"""
def plot_regression_line(X, y, model):
    """
    Plots scatter plot with regression line.

    :param X: Feature(s) (Pandas DataFrame)
    :param y: Target variable (Pandas Series)
    :param model: Trained Linear Regression Model
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='blue', label="Actual Data")
    plt.plot(X, model.predict(X), color='red', linewidth=2, label="Regression Line")
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.title("Regression Line")
    plt.legend()
    plt.show()


# Example Usage
if __name__ == "__main__":
    plot_regression_line(X, y, model)
