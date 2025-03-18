import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

"""
1) linear regression
2)Poly regression
"""
def linear_regression(X, y):
    """
    Fits a linear regression model and returns predictions, evaluation metrics.

    :param X: Feature(s) (Pandas DataFrame)
    :param y: Target variable (Pandas Series)
    :return: Model, predictions, R² score, MAE, MSE, RMSE
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    return model, y_pred, r2, mae, mse, rmse
def polynomial_regression(X, y, degree=2):
    """
    Fits a polynomial regression model.

    :param X: Feature(s) (Pandas DataFrame)
    :param y: Target variable (Pandas Series)
    :param degree: Degree of the polynomial
    :return: Model, predictions, R² score
    """
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    y_pred = model.predict(X_poly)
    r2 = r2_score(y, y_pred)

    return model, y_pred, r2