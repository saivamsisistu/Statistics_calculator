import scipy.stats as stats
import numpy as np


def one_sample_t_test(sample, population_mean, confidence=0.95):
    """Performs a One-Sample T-Test and returns test statistic, p-value, and confidence interval."""
    t_stat, p_value = stats.ttest_1samp(sample, population_mean)

    # Confidence Interval Calculation
    df = len(sample) - 1
    std_err = np.std(sample, ddof=1) / np.sqrt(len(sample))
    margin_error = stats.t.ppf((1 + confidence) / 2, df) * std_err
    mean_sample = np.mean(sample)
    confidence_interval = (mean_sample - margin_error, mean_sample + margin_error)

    return t_stat, p_value, confidence_interval
def one_sample_t_test(sample, population_mean):
    """Performs a One-Sample T-Test."""
    t_stat, p_value = stats.ttest_1samp(sample, population_mean)
    return t_stat, p_value

def two_sample_t_test(sample1, sample2):
    """Performs a Two-Sample (Independent) T-Test."""
    t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)  # Welch’s T-test
    return t_stat, p_value
