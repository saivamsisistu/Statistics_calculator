import scipy.stats as stats

def binomial_pmf(n, p, k):
    """Returns the Probability Mass Function (PMF) of a Binomial Distribution."""
    return stats.binom.pmf(k, n, p)

def binomial_cdf(n, p, k):
    """Returns the Cumulative Distribution Function (CDF) of a Binomial Distribution."""
    return stats.binom.cdf(k, n, p)
