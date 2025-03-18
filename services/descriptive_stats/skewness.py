from scipy.stats import skew
import numpy as np
import pandas as pd
"""
1)skewness
2)Kurtosis
"""
def calculate_skewness(data):
    """
    Computes the skewness of a dataset.

    :param data: List or Pandas Series
    :return: Skewness value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    return skew(data)


from scipy.stats import kurtosis


def calculate_kurtosis(data):
    """
    Computes the kurtosis of a dataset.

    :param data: List or Pandas Series
    :return: Kurtosis value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    return kurtosis(data)


# Example Usage
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50, 60, 70, np.nan]
    sample_series = pd.Series(sample_list)

    print("Skewness:", calculate_skewness(sample_series))
    print("Kurtosis:", calculate_kurtosis(sample_series))