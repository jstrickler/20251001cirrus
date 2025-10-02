import pytest

from cirrus import sample_function
def test_cirrus_has_sample_function():
    assert sample_function() is None  # no return value
