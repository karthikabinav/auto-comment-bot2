"""
Automated Comment Bot

This script automatically adds a comment 'Thank you for your contribution!'
to any new issue labeled 'feedback' or 'suggestion', and then closes the issue.

It is intended to be used as a GitHub Automation (e.g., via GitHub Actions or as a webhook handler).
"""
import os
from github import Github

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-comment-bot2")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"feedback", "suggestion"}
COMMENT_BODY = "Thank you for your contribution!"

def should_process_issue(issue):
    """Check if issue has target labels."""
    labels = {label.name for label in issue.get_labels()}
    return bool(labels & TARGET_LABELS)

def process_issue(issue):
    """Add comment and close issue."""
    if should_process_issue(issue):
        print(f"Processing issue #{issue.number}: {issue.title}")
        issue.create_comment(COMMENT_BODY)
        issue.edit(state="closed")
        print(f"Closed issue #{issue.number}")
    else:
        print(f"Skipping issue #{issue.number} - no target label")

def main():
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set - running in dry-run mode for demonstration")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        if issue.pull_request is None:
            process_issue(issue)

if __name__ == "__main__":
    main()
