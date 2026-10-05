"""Data for the pyap app."""

import numpy as np


def geyser_waiting(seed: int = 42) -> np.ndarray:
    """Simulate Old Faithful geyser waiting times.

    Draws from two normal distributions (short and long waits) to
    mimic the bimodal shape of the original geyser data.

    Args:
        seed: Seed for the random number generator.

    Returns:
        A 1D array of 272 waiting times (in minutes).
    """
    rng = np.random.default_rng(seed)
    return np.concatenate([
        rng.normal(54, 5, 100),
        rng.normal(80, 6, 172),
    ])
