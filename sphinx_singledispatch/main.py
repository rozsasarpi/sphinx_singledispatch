import numpy as np
import xarray as xr


def np_multiply(a: np.ndarray, b: np.ndarray):
    return a * b


def xr_multiply(a: xr.DataArray, b: xr.DataArray):
    return a + b
