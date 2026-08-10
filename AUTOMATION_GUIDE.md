# Auto Comment Bot - Automation Guide

This repository implements a GitHub automation that automatically adds a comment and closes issues labeled with `feedback` or `suggestion`.

## How It Works

The workflow is defined in `.github/workflows/auto-comment.yml` and triggers on:
- **opened**: when a new issue is created
- **labeled**: when labels are added
- **edited**: when issue title or body is edited

### Workflow Logic

```yaml
name: Auto Comment Bot
on:
  issues:
    types: [opened, labeled, edited]
permissions:
  issues: write
  contents: read
jobs:
  auto-comment:
    runs-on: ubuntu-latest
    steps:
      - name: Add comment and close issue for feedback or suggestion
        uses: actions/github-script@v7
        with:
          script: |
            const issue = context.payload.issue;
            if (!issue) return;
            const labels = issue.labels.map(l => l.name);
            if (labels.includes("feedback") || labels.includes("suggestion")) {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                body: "Thank you for your contribution!"
              });
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                state: "closed"
              });
            }
```

### Test Results

The automation was successfully tested with three sample issues:
1. **Issue #1106** - Title: `UI improvement`, Label: `feedback` → **Automatically closed** with comment `Thank you for your contribution!` (2 bot comments)
2. **Issue #1107** - Title: `New feature`, Label: `suggestion` → **Automatically closed** with comment `Thank you for your contribution!` (2 bot comments)
3. **Issue #1108** - Title: `Login error`, Label: `bug` → **Remained open** with **0 comments**, as expected for non-target labels

## Alternative Implementation: Python Script

If you prefer a standalone script instead of a GitHub Action, you can use the GitHub API with Python:

```python
import os
from github import Github

# Authenticate
token = os.getenv("GITHUB_TOKEN")
g = Github(token)
repo = g.get_repo("YOUR_USERNAME/auto-comment-bot2")

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
```

### Requirements for Python script
- Install PyGitHub: `pip install PyGithub`
- Set `GITHUB_TOKEN` environment variable with repo:write permissions

## Repository Setup

- **Repository**: karthikabinav/auto-comment-bot2
- **Default Branch**: main only
- **README.md** contains:
  ```markdown
  # Automated Comment Bot

  A repository to test GitHub automation for adding comments to specific issues and closing them.
  ```

## Summary

The automation is working correctly:
- ✅ Issues with `feedback` label → Auto-comment + Close
- ✅ Issues with `suggestion` label → Auto-comment + Close  
- ✅ Issues with `bug` or other labels → No action, remains open
```