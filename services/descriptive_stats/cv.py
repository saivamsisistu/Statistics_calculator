import pandas as pd
import numpy as np

def calculate_cv(data):
    """
    Computes the Coefficient of Variation (CV) of a dataset.

    :param data: List or Pandas Series
    :return: CV value in percentage
    """
    if isinstance(data, pd.Series):
        data = data.dropna()  # Remove NaN values
    elif isinstance(data, list):
        data = pd.Series([x for x in data if pd.notna(x)])  # Convert list to Pandas Series & remove NaN

    mean_value = data.mean()
    std_dev_value = data.std()

    if mean_value == 0:
        return None  # Avoid division by zero error

    return (std_dev_value / mean_value) * 100


# Example Usage
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50, np.nan]
    sample_series = pd.Series(sample_list)

    print("Coefficient of Variation (CV):", calculate_cv(sample_series))
