import scipy.stats as stats

def anova_test(*groups):
    """Performs One-Way ANOVA test for multiple groups."""
    f_stat, p_value = stats.f_oneway(*groups)
    return f_stat, p_value
