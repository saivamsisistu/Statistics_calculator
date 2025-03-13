import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_regression(X, y):
    """Performs Simple Linear Regression and returns the slope, intercept, and predictions."""
    try:
        X = np.array(X).reshape(-1, 1)  # Reshape for sklearn
        y = np.array(y)

        model = LinearRegression()
        model.fit(X, y)

        return {
            'slope': model.coef_[0],
            'intercept': model.intercept_,
            'predicted_values': model.predict(X).tolist()
        }
    except Exception as e:
        return {'error': str(e)}
