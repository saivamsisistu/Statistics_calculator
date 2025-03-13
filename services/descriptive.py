import numpy as np
from scipy import stats

def calculate_descriptive(data):
    """Calculates mean, median, mode, variance, and standard deviation."""
    try:
        # mode_result = stats.mode(data, keepdims=True)  # Ensures correct shape

        return {
            'mean': np.mean(data),
            'median': np.median(data),
            # 'mode': mode_result.mode[0] if mode_result.mode.size > 0 else None,
            'variance': np.var(data),
            'std_dev': np.std(data)
        }
    except Exception as e:
        return {'error': str(e)}
