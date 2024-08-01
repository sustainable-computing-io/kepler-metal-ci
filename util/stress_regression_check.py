import os
import requests
from openai import OpenAI
from github import Github

github_token = os.getenv("GITHUB_TOKEN")
repo_name = "sustainable-computing-io/kepler-metal-ci"

# URLs of the reports
url = "https://sustainable-computing-io.github.io/kepler-metal-ci/kepler-stress-test-metrics.html"

def fetch_report(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def check_regression(report):
    prompt = f"""
    Please check if there is any performance regression from the test results. 
    A regression is defined as a significant increase in CPU utilization or Std Dev compared to the previous test results.
    Please read this test report and tell me what happened in the last two days' results. 

    Report:
    {report}

    Provide a detailed analysis and conclusion. 
    In order to help parsing the analysis, please output the summary first. 
    The summary should be in this format: 
    if there is any significant regression, the summary is exactly "Significant Regression Detected" and then followed by the detailed analysis and conclusion. 
    Otherwise, the summary should be exactly "No Significant Regression" and then stop generating any content, just stop there.
    """
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-turbo",
        temperature=0,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def create_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)

def main():
    # Fetch reports
    print("Fetching reports...")
    report = fetch_report(url)

    # Check for regression
    print("Checking for regression...")
    result = check_regression(report)

    # Analyze the result for regression
    print("Analyzing the result...")
    regression_detected = False
    if "Significant Regression Detected".lower() in result.lower():
        regression_detected = True

    # Create GitHub issue if regression detected
    if regression_detected:
        print("Creating GitHub issue...")
        g = Github(github_token)
        repo = g.get_repo(repo_name)
        title = "Regression Detected in Kepler or kube-apiserver CPU Utilization Performance"
        body = f"Regression detected from the following reports:\n\nReport: {url}\n\nDetails:\n{result}"
        create_github_issue(repo, title, body)

if __name__ == "__main__":
    main()
