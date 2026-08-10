import os
from github import Github

# Authenticate
token = os.getenv("GITHUB_TOKEN")
g = Github(token)
repo = g.get_repo("karthikabinav/auto-comment-bot2")

# Get recent open issues
issues = repo.get_issues(state="open")

for issue in issues:
    labels = [label.name for label in issue.get_labels()]
    if "feedback" in labels or "suggestion" in labels:
        issue.create_comment("Thank you for your contribution!")
        issue.edit(state="closed")
        print(f"Closed issue #{issue.number}: {issue.title}")
    else:
        print(f"Skipped issue #{issue.number}: {issue.title}")
