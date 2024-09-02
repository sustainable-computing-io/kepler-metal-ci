import os
import re
import requests
from datetime import datetime
from openai import OpenAI
from github import Github

github_token = os.getenv("GITHUB_TOKEN")
repo_name = "sustainable-computing-io/kepler-metal-ci"
# Directory containing the validation reports
validation_dir = "docs/validation"


def list_latest_folders(directory, n=5):
    folders = [
        f for f in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, f))
    ]
    sorted_folders = sorted(
        folders,
        key=lambda date: datetime.strptime(date, '%Y-%m-%d'),
        reverse=True)
    return sorted_folders[:n]


def read_report(folder_path):
    for file_name in os.listdir(folder_path):
        if re.match(r'report-v\d+\.\d+\.\d+-\d+-g\w+\.md', file_name):
            print(f"Reading report: {file_name}")
            with open(os.path.join(folder_path, file_name), 'r') as file:
                return file.read()
    return None


def check_regression(report_content):
    prompt = f"""
    Please check if there is any performance regression from the test results. 
    A regression is defined as a significant increase in MSE or MAPE in model performance compared to the previous test results. 
    Please only focus on MSE and MAPE that are in dynamic mode and ignore any regression in idle mode.

    Report: 
    {report_content}

    In order to help parsing the analysis, please output the summary first. 
    The summary should be in this format: 
    if there is any significant regression, the summary is exactly "Significant Regression Detected" and then followed by those with only the significant increase and conclusion. 
    Otherwise, the summary should be exactly "No Issue" and then stop generating any content, just stop there.
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), )
    completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="gpt-4-turbo",
        temperature=0,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def create_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)


def main():
    latest_folders = list_latest_folders(validation_dir, 5)
    report_content = ""
    print(f"Latest folders: {latest_folders}")
    for folder in latest_folders:
        folder_path = os.path.join(validation_dir, folder)
        this_content = read_report(folder_path)
        report_content += f"Report Date: {folder}, Content: {this_content} \n"

    if report_content:
        regression_check_result = check_regression(report_content)
        print(f"Regression Check Result: {regression_check_result}")
        print("-" + "=" * 40 + "-")

    # Analyze the result for regression
    print("Analyzing the result...")
    regression_detected = False
    if "Significant Regression Detected".lower(
    ) in regression_check_result.lower():
        regression_detected = True

    # Create GitHub issue if regression detected
    if regression_detected:
        print("Creating GitHub issue...")
        g = Github(github_token)
        repo = g.get_repo(repo_name)
        title = "Regression Detected in Model Validation Performance"
        body = regression_check_result
        create_github_issue(repo, title, body)


if __name__ == "__main__":
    main()
