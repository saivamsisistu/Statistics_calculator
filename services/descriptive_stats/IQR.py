import pandas as pd

"""
1) Inter quartile range
"""
def calculate_iqr(data):
    """
    Computes the Interquartile Range (IQR) of a dataset.

    :param data: List or Pandas Series
    :return: IQR value
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    q1 = data.quantile(0.25)  # 25th percentile (Q1)
    q3 = data.quantile(0.75)  # 75th percentile (Q3)
    return q3 - q1  # IQR = Q3 - Q1
