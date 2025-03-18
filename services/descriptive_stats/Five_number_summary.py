import numpy as np
"""
1) Five Number Summary.
"""
def five_number_summary(data):
    """
    Compute the Five-Number Summary: Minimum, Q1, Median, Q3, Maximum.

    Parameters:
    data (list or np.array): A numerical dataset.

    Returns:
    dict: A dictionary containing the five-number summary.
    """
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("Input data must be a list or numpy array.")

    if len(data) == 0:
        raise ValueError("Data cannot be empty.")

    data = np.array(data)
    minimum = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    maximum = np.max(data)

    return {
        "Minimum": minimum,
        "Q1 (25th percentile)": q1,
        "Median (Q2)": median,
        "Q3 (75th percentile)": q3,
        "Maximum": maximum
    }


# Example Usage
if __name__ == "__main__":
    sample_data = [12, 15, 14, 10, 18, 22, 25, 30, 28, 35]
    summary = five_number_summary(sample_data)
    print("Five-Number Summary:", summary)
