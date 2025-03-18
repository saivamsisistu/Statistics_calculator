import numpy as np
import pandas as pd
"""
1) variance
2)standard Deviation
3)Range
"""
def calculate_variance(data, sample=True):
    """
    Computes the variance of a dataset.

    :param data: List or Pandas Series
    :param sample: Boolean, if True computes Sample Variance (n-1), otherwise Population Variance (n)
    :return: Variance value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    if sample:
        return data.var(ddof=1)  # Sample Variance (n-1)
    else:
        return data.var(ddof=0)  # Population Variance (n)
def calculate_std_dev(data, sample=True):
    """
    Computes the standard deviation of a dataset.

    :param data: List or Pandas Series
    :param sample: Boolean, if True computes Sample Std Dev (n-1), otherwise Population Std Dev (n)
    :return: Standard Deviation value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    if sample:
        return data.std(ddof=1)  # Sample Standard Deviation
    else:
        return data.std(ddof=0)  # Population Standard Deviation
def calculate_range(data):
    """
    Computes the range of a dataset (Max - Min).

    :param data: List or Pandas Series
    :return: Range value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    return data.max() - data.min()