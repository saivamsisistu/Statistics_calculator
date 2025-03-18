import matplotlib.pyplot as plt
import seaborn as sns
"""
1)histogram
2)boxplot
3)frequency table
"""

def plot_histogram(data, title="Histogram"):
    """
    Plots a histogram of the dataset.

    :param data: List or Pandas Series
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    plt.figure(figsize=(8, 5))
    sns.histplot(data, bins=10, kde=True, color='blue')
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()


def plot_boxplot(data, title="Boxplot"):
    """
    Plots a boxplot of the dataset to identify outliers.

    :param data: List or Pandas Series
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    plt.figure(figsize=(5, 6))
    sns.boxplot(y=data, color="red")
    plt.ylabel("Value")
    plt.title(title)
    plt.show()


def frequency_table(data):
    """
    Generates a frequency table for categorical or numerical data.

    :param data: List or Pandas Series
    :return: DataFrame containing frequency counts
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    return data.value_counts().reset_index().rename(columns={'index': 'Value', 0: 'Frequency'})
# Example Usage
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50, 60, 70, 100, np.nan]
    sample_series = pd.Series(sample_list)

    plot_histogram(sample_series, title="Sample Data Histogram")
    plot_boxplot(sample_series, title="Sample Data Boxplot")
    print("Frequency Table:\n", frequency_table(sample_series))