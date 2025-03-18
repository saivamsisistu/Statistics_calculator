import numpy as np
import pandas as pd
def calculate_mean(data):
      """
      Compute the mean of the numerical data
      Handles missing values by ignoring them.

      :param data: List or Pandas Series
      :return: Mean value
      """
      if isinstance(data,pd.Series):
        return data.dropna().mean()
      elif isinstance(data,list):
        return np.nanmean()
      else:
        raise TypeError("Inpust should be list or pandas series")
def calculate_median(data):
    """
    Computes the median of a given numerical dataset.
    Handles missing values by ignoring them.

    :param data: List or Pandas Series
    :return: Median value
    """
    if isinstance(data, pd.Series):
        return data.dropna().median()
    elif isinstance(data, list):
        return np.nanmedian(data)  # Ignores NaN values
    else:
        raise TypeError("Input should be a list or a Pandas Series")
def calculate_mode(data):
    """
    Computes the mode of a given dataset.
    Works for both numerical and categorical data.
    Handles missing values by ignoring them.
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values

    if isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Remove NaN values manually

    mode_values = data.mode()  # Pandas handles mode calculation

    if len(mode_values) == 0:
        return None  # No mode found
    elif len(mode_values) == 1:
        return mode_values.iloc[0]  # Return single mode value
    else:
        return mode_values.tolist()  # Return list if multiple modes exist