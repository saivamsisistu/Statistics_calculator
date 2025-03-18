import scipy.stats as stats

def exponential_pdf(x, rate=1):
    """Returns the Probability Density Function (PDF) of an Exponential Distribution."""
    return stats.expon.pdf(x, scale=1/rate)

def exponential_cdf(x, rate=1):
    """Returns the Cumulative Distribution Function (CDF) of an Exponential Distribution."""
    return stats.expon.cdf(x, scale=1/rate)
