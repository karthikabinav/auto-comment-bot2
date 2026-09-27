"""
GitHub Automation Script
Automatically adds comment Thank you for your contribution! to issues labeled feedback or suggestion, then closes them.
"""

TARGET_LABELS = {"feedback", "suggestion"}
COMMENT_BODY = "Thank you for your contribution!"

def handle_issue(issue):
    labels = {label.name for label in issue.labels}
    if labels & TARGET_LABELS:
        issue.create_comment(COMMENT_BODY)
        issue.edit(state="closed")
        return True
    return False
