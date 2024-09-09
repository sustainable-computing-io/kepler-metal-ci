# tests/test_error_metrics.py
from generate_daily_validations import SortErrorMetrics 

def test_error_metric_generation(generate_error_metric):
    """Test ErrorMetric generation"""
    assert generate_error_metric.name == "core_absolute"
    assert generate_error_metric.mse == "103"
    assert generate_error_metric.mape == "5"


def test_error_metric_str(generate_error_metric):
    """Test str(ErrorMetric) outputs desirable string values for tabulation"""
    assert str(generate_error_metric) == "MSE=103\nMAPE=5"


def test_sort_error_metrics_unordered(generate_error_metric_list):
    """Test ErrorMetrics sorting based on name order"""
    name_order = ["platform_absolute", "package_absolute", "core_absolute"]
    sorter = SortErrorMetrics(error_metric_name_order=name_order, 
                              error_metric_list=generate_error_metric_list)

    sorted_names = [metric.name for metric in sorter.sorted_error_metric_list]
    assert sorted_names == name_order

    # note include test cases for when name order provided contains values that 
    # do not exist?

# TODO: include tests for json and markdown reports