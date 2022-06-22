from functools import singledispatch

import numpy as np
import xarray as xr


@singledispatch
def multiply(a, b):
    """Multiply `a` and `b`.

    Args:
        a:
        b:

    Returns:
        The product of `a` and `b`.
    """
    raise NotImplementedError("Unsupported type")


@multiply.register(np.ndarray)
def _(a: np.ndarray, b: np.ndarray):
    return a * b


@multiply.register(xr.DataArray)
def _(a: xr.DataArray, b: xr.DataArray):
    """Multiply strings: joining them."""
    return a + b
