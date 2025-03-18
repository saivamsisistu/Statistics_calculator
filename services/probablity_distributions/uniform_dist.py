import scipy.stats as stats

def uniform_pdf(x, a=0, b=1):
    """Returns the Probability Density Function (PDF) of a Uniform Distribution."""
    return stats.uniform.pdf(x, a, b-a)

def uniform_cdf(x, a=0, b=1):
    """Returns the Cumulative Distribution Function (CDF) of a Uniform Distribution."""
    return stats.uniform.cdf(x, a, b-a)
