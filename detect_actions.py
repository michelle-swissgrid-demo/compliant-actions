import base64
import os
import requests


# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Setup session with auth
session = requests.Session()
session.headers.update({
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
})

def list_repositories(org):
    """
    List all repositories in the organization.
    """
    repos = []
    page = 1
    while True:
        # fetches in chuncks (if there are >100 repos)
        url = f"{GITHUB_API_URL}/orgs/{org}/repos?per_page=100&page={page}"
        response = session.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repositories: {response.text}")
        data = response.json()
        # no more repositories
        if not data:
            break
        repos.extend([repo["name"] for repo in data])
        page += 1
    return repos


def list_workflows(org, repo):
    """
    List all workflow files in a repository.
    """
    # Gets the contents of the .github/workflows directory
    url = f"{GITHUB_API_URL}/repos/{org}/{repo}/contents/.github/workflows"
    response = session.get(url)
    if response.status_code != 200:
        return []
    data = response.json() # list of all workflow files
    return [item["path"] for item in data if item["type"] == "file"]


def fetch_workflow_content(org, repo, path):
    """
    Fetch and decode a workflow file.
    """
    url = f"{GITHUB_API_URL}/repos/{org}/{repo}/contents/{path}"
    response = session.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content


def main():
    affected_repos = []

    print(f"Scanning organization: {ORG_NAME} for vulnerable action: {VULNERABLE_ACTION}\n")
    repos = list_repositories(ORG_NAME)

    for repo in repos:
        print(f"Checking repository: {repo}")
        workflows = list_workflows(ORG_NAME, repo)
        for wf in workflows:
            content = fetch_workflow_content(ORG_NAME, repo, wf)
            if content and VULNERABLE_ACTION in content:
                print(f"Vulnerable action found in {repo} ({wf})")
                affected_repos.append(repo)
                break

    with open(OUTPUT_FILE, "w") as f:
        for repo in affected_repos:
            f.write(repo + "\n")

    print("\nScan complete. Affected repositories written to", OUTPUT_FILE)


if __name__ == "__main__":
    ORG_NAME = input("Enter the GitHub organization to scan: ").strip()
    VULNERABLE_ACTION = input("Enter the action to scan for: ").strip()
    OUTPUT_FILE = input("Enter the file to write the results to: ").strip()
    main()
