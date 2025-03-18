

import statsmodels.stats.weightstats as sm
import numpy as np


def z_test(sample, population_mean, confidence=0.95):
    """Performs a One-Sample Z-Test and returns test statistic, p-value, and confidence interval."""
    z_stat, p_value = sm.ztest(sample, value=population_mean, alternative='two-sided')

    # Confidence Interval Calculation
    mean_sample = np.mean(sample)
    std_err = np.std(sample, ddof=1) / np.sqrt(len(sample))
    margin_error = stats.norm.ppf((1 + confidence) / 2) * std_err
    confidence_interval = (mean_sample - margin_error, mean_sample + margin_error)

    return z_stat, p_value, confidence_interval

    return z_stat, p_value

if __name__=="__main__":
    sample1 = np.random.normal(50, 10, 30)  # Sample 1
    sample2 = np.random.normal(55, 12, 30)  # Sample 2
    population_mean = 50
    population_std = 10
    # Z-Test Example
    z_stat, p_value = z_test(sample1, population_mean)
    print("Z-Test:", z_stat, p_value)