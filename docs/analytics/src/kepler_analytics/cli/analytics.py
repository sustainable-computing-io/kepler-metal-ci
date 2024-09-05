import click

from kepler_analytics.__about__ import __version__

import os
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
import base64
from io import BytesIO

NUM_DAYS = 5  # Number of days to analyze
BASE_DIR = "../validation"
JSON_FILES = {
    "vm": "kepler_node_package_joules_total--dynamic.json",
    "metal": "kepler_vm_package_joules_total--dynamic.json",
}
REPORT_FILE = "../kepler-model-validation-chart.md"


def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def process_date(date):
    date_str = date.strftime("%Y-%m-%d")
    date_dir = os.path.join(BASE_DIR, date_str)

    if not os.path.exists(date_dir):
        click.secho(f"Directory for date {date_str} not found")
        return None

    folder_names = [name for name in os.listdir(date_dir) if os.path.isdir(os.path.join(date_dir, name))]

    results = []
    for folder_name in folder_names:
        folder_path = os.path.join(date_dir, folder_name)

        df_metal = None
        df_vm = None

        for data_type, json_file in JSON_FILES.items():
            file_path = os.path.join(folder_path, json_file)
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    data = json.load(f)

                timestamps = [datetime.datetime.fromtimestamp(ts) for ts in data["timestamps"]]
                values = data["values"]

                df = pd.DataFrame({"Timestamp": timestamps, "Watts": values})

                if data_type == "metal":
                    df_metal = df
                elif data_type == "vm":
                    df_vm = df
            else:
                print(f"File {json_file} not found in folder {folder_name}")

        if df_metal is not None and df_vm is not None:
            df_merged = pd.merge(df_metal, df_vm, on="Timestamp", how="inner", suffixes=("_metal", "_vm"))

            if not df_merged.empty:
                mse = mean_squared_error(df_merged["Watts_metal"], df_merged["Watts_vm"])
                mape = mean_absolute_percentage_error(df_merged["Watts_metal"], df_merged["Watts_vm"])

                results.append(
                    {
                        "date": date_str,
                        "folder": folder_name,
                        "df_metal": df_metal,
                        "df_vm": df_vm,
                        "mse": mse,
                        "mape": mape,
                    }
                )

    return results


def create_chart(result, compare_to=None):
    fig, ax1 = plt.subplots(figsize=(14, 7))

    result["df_metal"]["Data_Point"] = range(len(result["df_metal"]))
    result["df_vm"]["Data_Point"] = range(len(result["df_vm"]))

    ax1.plot(
        result["df_metal"]["Data_Point"],
        result["df_metal"]["Watts"],
        marker="x",
        color="#024abf",
        label=f'metal data ({result["date"]})',
    )
    ax1.set_xlabel("Data Points")
    ax1.set_ylabel("Metal [Watts]", color="#024abf")
    ax1.tick_params(axis="y")

    ax2 = ax1.twinx()
    ax2.plot(
        result["df_vm"]["Data_Point"],
        result["df_vm"]["Watts"],
        marker="o",
        color="#ff742e",
        label=f'vm data ({result["date"]})',
    )
    ax2.set_ylabel("VM [Watts]", color="#ff742e")
    ax2.tick_params(axis="y")

    if compare_to:
        compare_to["df_metal"]["Data_Point"] = range(len(compare_to["df_metal"]))
        compare_to["df_vm"]["Data_Point"] = range(len(compare_to["df_vm"]))

        ax1.plot(
            compare_to["df_metal"]["Data_Point"],
            compare_to["df_metal"]["Watts"],
            linestyle="--",
            color="#024abf",
            alpha=0.5,
            label=f'metal data ({compare_to["date"]})',
        )

        ax2.plot(
            compare_to["df_vm"]["Data_Point"],
            compare_to["df_vm"]["Watts"],
            linestyle="--",
            color="#ff742e",
            alpha=0.5,
            label=f'vm data ({compare_to["date"]})',
        )

    plt.title(f'Kepler Metal & VM / {result["folder"]} / Date: {result["date"]}')
    plt.grid(True)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper left")

    textstr = f'MSE: {result["mse"]:.2f}\nMAPE: {result["mape"]:.2f}%'
    ax1.text(
        0.98,
        0.97,
        textstr,
        transform=ax1.transAxes,
        fontsize=14,
        verticalalignment="top",
        horizontalalignment="right",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()


def generate_reports(all_results, num_days: int, report_file: str):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kepler Analysis Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .chart { margin-bottom: 30px; }
        </style>
    </head>
    <body>
        <h1>Kepler Analysis Report</h1>
    """

    for i, result in enumerate(all_results):
        if i < num_days:
            compare_to = next(
                (r for r in all_results[i + 1 :] if r["folder"] == result["folder"]),
                None,
            )
            chart_img = create_chart(result, compare_to)
            html_content += f"""
        <div class="chart">
            <h2>{result['date']} - {result['folder']}</h2>
            <img src="data:image/png;base64,{chart_img}" alt="Chart for {result['date']} - {result['folder']}">
        </div>
    """

    html_content += """
    </body>
    </html>
    """

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    os.makedirs(date_str, exist_ok=True)
    output_path = f"{date_str}/kepler_report.html"
    with open(output_path, "w") as f:
        f.write(html_content)

    with open(report_file, "a") as f:
        f.write(f"| {date_str} | [{output_path}](analytics/{output_path}) |\n")


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=False,
)
@click.version_option(version=__version__, prog_name="kepler-analytics")
def main():
    pass


@main.command()
@click.option(
    "--end-date",
    type=click.DateTime(["%Y-%m-%d"]),
    default=str(datetime.datetime.now().date()),
    help="End date to analyze",
)
@click.option("--base-dir", default=BASE_DIR, help="Base directory to search for folders", show_default=True)
@click.option("--num-days", default=NUM_DAYS, help="Number of days to analyze", show_default=True)
@click.option("--report-file", default=REPORT_FILE, help="Report file", show_default=True)
def run(end_date: datetime.datetime, base_dir: str, num_days: int, report_file: str):
    start_date = end_date - datetime.timedelta(days=num_days)
    click.echo(f"Analyzing {num_days} days from {start_date.date()} to {end_date.date()} in {base_dir}")

    all_results = []
    for i in range(num_days):
        date = end_date - datetime.timedelta(days=i)
        results = process_date(date)
        if results:
            all_results.extend(results)

    all_results.sort(key=lambda x: (x["date"], x["folder"]), reverse=True)
    generate_reports(all_results, num_days, report_file)
