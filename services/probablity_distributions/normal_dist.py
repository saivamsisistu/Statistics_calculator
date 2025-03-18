import numpy as np
import scipy.stats as stats

def normal_pdf(x, mean=0, std_dev=1):
    """Returns the Probability Density Function (PDF) of a Normal Distribution."""
    return stats.norm.pdf(x, mean, std_dev)

def normal_cdf(x, mean=0, std_dev=1):
    """Returns the Cumulative Distribution Function (CDF) of a Normal Distribution."""
    return stats.norm.cdf(x, mean, std_dev)

def normal_percentile(percentile, mean=0, std_dev=1):
    """Returns the value at a given percentile for a Normal Distribution."""
    return stats.norm.ppf(percentile, mean, std_dev)
