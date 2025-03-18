import scipy.stats as stats
import numpy as np

def chi_square_test(observed):
    """
    Performs a Chi-Square Test.
    observed: 2D array of observed frequency values.
    """
    chi_stat, p_value, dof, expected = stats.chi2_contingency(observed)
    return chi_stat, p_value, dof, expected
