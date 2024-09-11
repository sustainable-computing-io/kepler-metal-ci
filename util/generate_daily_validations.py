import tabulate
import json
import argparse
import os
from typing import NamedTuple, List, Tuple
from datetime import datetime


# Global Variable which stores the ordering and desired error metrics
ERROR_METRIC_LIST = [
    "platform_absolute",
    "package_absolute",
    "platform_dynamic",
    "package_dynamic",
    "platform_idle",
    "package_idle",
]


class ErrorMetric(NamedTuple):
    """
    A class to represent an immutable error metric object 
    which stores metric name, mse, and mape.

    ...

    Attributes
    ----------
    name : str
        metric name
    mse : str
        mean squared error
    mape : str
        mean absolute percentage error
    """
    name: str
    mse: str
    mape: str

    def __eq__(self, other) -> bool:
        if isinstance(other, ErrorMetric):
            return self.name == other.name
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name, self.mse, self.mape))

    def __str__(self) -> str:
        return f'MSE={self.mse}\nMAPE={self.mape}'


class SortErrorMetrics:
    """
    A class which sorts a list of ErrorMetric Objects
    based on the name ordering in the error metric name
    order list.
    ...

    Attributes
    ----------
    error_metric_name_order : List[str]
        list of error metric names
    error_metric_list : List[ErrorMetric]
        ErrorMetrics list

    Property
    -------
    sorted_error_metric_list:
        the sorted the error_metric_list based on name
        ordering in error_metric_name_order
    """
    def __init__(self, error_metric_name_order: List[str], 
                 error_metric_list: List[ErrorMetric]):
        """
        Initializes error_metric_name_order,
        error_metric_list, and
        sorted_error_metric_list

        Parameters
        ----------
            error_metric_name_order: List[str]
                list of error metric names
            error_metric_list: List[ErrorMetric]
                ErrorMetrics list
        """
        self.error_metric_name_order = error_metric_name_order
        self.error_metric_list = error_metric_list
        self._sorted_error_metric_list = self._sort_error_metrics()
    
    def sorted_error_metric_list(self) -> List[ErrorMetric]:
        return self._sorted_error_metric_list

    def _prune_error_metrics(self) -> List[ErrorMetric]:
        """
        removes error metrics not included in error_metric_name_order

        Returns
        -------
        List[ErrorMetric]
        """
        cleaned_error_metric_list = [error_metric for error_metric in self.error_metric_list
                        if error_metric.name in self.error_metric_name_order]
        
        for metric_name in self.error_metric_name_order:
            if not any(metric_name == error_metric.name 
                       for error_metric in cleaned_error_metric_list):
                raise ValueError(f"{metric_name} does not exist in validator")

        return cleaned_error_metric_list

    def _sort_error_metrics(self) -> List[ErrorMetric]:
        """
        sorts the error_metric_list based on name
        ordering in error_metric_name_order

        Returns
        -------
        List[ErrorMetric]
        """
        pruned_list = self._prune_error_metrics()
        sorted_list = sorted(pruned_list, 
                             key=lambda metric: 
                             self.error_metric_name_order.index(metric.name))
        return sorted_list
        

def retrieve_metrics_from_new_report(error_metrics_filepath: str) -> List[ErrorMetric]:
    """
    Retrieve error metrics from error metric json report outputted from kepler validator

    Parameters
    ----------
        error_metrics_filepath (str): filepath to json report outputted from 
        kepler validator
    
    Returns
    -------
        ErrorMetric list
    """
    #found_file = glob.glob(error_metrics_filepath)[0]
    if not os.path.exists(error_metrics_filepath):
        raise FileNotFoundError(
            f"The file at {error_metrics_filepath} was not found."
        )
    print(error_metrics_filepath)
    error_metrics = []
    with open(error_metrics_filepath, 'r') as json_file:
        new_metrics = json.load(json_file)
        for row in new_metrics['result']:
            error_metrics.append(ErrorMetric(
                name=str(row['metric-name']),
                mse=str(row['value']['mse']),
                mape=str(row['value']['mape'])
            ))
    # sort error metrics based on error metric list order
    sort_error_metrics = SortErrorMetrics(
        ERROR_METRIC_LIST,
        error_metrics
    )
    current_date = datetime.now()
    date_str = current_date.strftime("%Y-%m-%d-%H:%M:%S")
    return [date_str] + sort_error_metrics.sorted_error_metric_list()


def retrieve_json_table_report(filepath) -> Tuple[str, str, List[str], List[List[str]]]:
    """
    Retrieve current results from daily validations json table report

    Parameters
    ----------
        filepath (str): filepath to daily validations json table report
    
    Returns
    -------
        title, description, headers, rows
    """
    with open(filepath, 'r') as json_file:
        current_json_table = json.load(json_file)
        title = current_json_table['title']
        desc = current_json_table['description']
        headers = current_json_table['headers']
        rows = current_json_table['rows']
    return title, desc, headers, rows


def save_report_to_json(filepath, dict_data):
    """
    Save dict_data to daily validations json table report

    Parameters
    ----------
        filepath (str): filepath to daily validations json report to update
        dict_data (str): new report in form of python dict to save
    
    Returns
    -------
        None
    """
    with open(filepath, 'w') as json_file:
        json.dump(dict_data, json_file, indent=4)


def generate_markdown_table_report(title, description, headers, rows):
    """
    Generate new markdown table report

    Parameters
    ----------
        title (str): title of table report
        description (str): description of table report
        headers (List[str]): headers of table
        rows (List[List[str]]): rows of table 
    
    Returns
    -------
        markdown_content (str)
    """
    markdown_content = f"# {title}\n\n"
    markdown_content += f"## Introduction\n"
    markdown_content += f"{description}\n\n"
    markdown_content += f"## Daily Test Results\n"
    markdown_table = tabulate.tabulate(rows, headers, tablefmt="pipe")    
    markdown_content += markdown_table
    return markdown_content


def save_report_to_markdown(filepath, content):
    """
    Save markdown content to daily validations markdown table report

    Parameters
    ----------
        filepath: filepath to daily validations markdown report to update
        content: new markdown report to save directly
    
    Returns
    -------
        None
    """
    with open(filepath, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown table.")
    parser.add_argument('--report-md-filepath', required=True, help='filepath to md report object')
    parser.add_argument('--report-json-filepath', required=True, help='filepath to json report object')
    parser.add_argument('--new-val-filepath', required=True, help='filepath to newly generated json report object')

    args = parser.parse_args()

    report_md_filepath = args.report_md_filepath
    report_json_filepath = args.report_json_filepath
    new_val_filepath = args.new_val_filepath

    new_error_metrics_list = retrieve_metrics_from_new_report(new_val_filepath)
    
    title, desc, headers, rows = retrieve_json_table_report(report_json_filepath)
    headers =  ["Date"] + ERROR_METRIC_LIST
    new_row = [str(metric) for metric in new_error_metrics_list]
    rows.append(new_row)
    new_json_report = {
        "title": title,
        "description": desc,
        "headers": headers,
        "rows": rows,
    }

    markdown_content = generate_markdown_table_report(title, desc, headers, rows)

    save_report_to_json(report_json_filepath, new_json_report)

    save_report_to_markdown(report_md_filepath, markdown_content)

    print(f"Markdown table generated successfully and saved to JSON: {report_json_filepath} and MD: {report_md_filepath}.")