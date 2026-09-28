from eab.metrics import error_metrics
import pytest

def test_roundoff_above_one_is_clamped():
    assert error_metrics(1.0+2e-15,0.5,1e-12)["p0"]==1.0

def test_roundoff_below_zero_is_clamped():
    assert error_metrics(-2e-15,0.5,1e-12)["p0"]==0.0

def test_materially_invalid_probability_still_fails():
    with pytest.raises(ValueError):
        error_metrics(1.000001,0.5,1e-12)
