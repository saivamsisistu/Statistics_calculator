import scipy.stats as stats

def poisson_pmf(lam, k):
    """Returns the Probability Mass Function (PMF) of a Poisson Distribution."""
    return stats.poisson.pmf(k, lam)

def poisson_cdf(lam, k):
    """Returns the Cumulative Distribution Function (CDF) of a Poisson Distribution."""
    return stats.poisson.cdf(k, lam)
