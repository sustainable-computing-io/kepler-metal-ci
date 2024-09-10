# tests/conftest.py
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generate_daily_validations import ErrorMetric 

@pytest.fixture
def generate_error_metric():
    metric = ErrorMetric(name="core_absolute", mse="103", mape="5")
    return metric

@pytest.fixture
def generate_error_metric_list():
    error_metrics = [
        ErrorMetric(name="core_absolute", mse="0.3", mape="10"),
        ErrorMetric(name="platform_absolute", mse="0.25", mape="11"),
        ErrorMetric(name="package_absolute", mse="0.1", mape="8"),
    ]
    return error_metrics