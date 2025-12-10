from sklearn.metrics import mean_squared_error
import numpy as np

def rmse(true, pred):
    """Calculate Root Mean Square Error."""
    return np.sqrt(mean_squared_error(true, pred))
