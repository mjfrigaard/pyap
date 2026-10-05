import numpy as np

from pyap.data import geyser_waiting


def test_geyser_waiting_length():
    assert len(geyser_waiting()) == 272


def test_geyser_waiting_reproducible():
    np.testing.assert_array_equal(geyser_waiting(seed=1), geyser_waiting(seed=1))
