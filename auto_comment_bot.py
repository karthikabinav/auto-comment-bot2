"""
Automated Comment Bot
A script to automatically add a comment and close issues labeled with feedback or suggestion.
"""
import os
from github import Github

# Configuration
REPO_NAME = "karthikabinav/auto-comment-bot2"
TARGET_LABELS = {"feedback", "suggestion"}
COMMENT_BODY = "Thank you for your contribution!"

def process_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Processing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment(COMMENT_BODY)
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}")

if __name__ == "__main__":
    process_issues()
