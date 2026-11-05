"""GitHub automation script to comment and close issues labeled feedback or suggestion."""
# Example logic using GitHub API:
# For each new issue:
#   if "feedback" in labels or "suggestion" in labels:
#       add_comment(issue_number, "Thank you for your contribution!")
#       close_issue(issue_number)

TARGET_LABELS = {"feedback", "suggestion"}
COMMENT = "Thank you for your contribution!"

def should_process(labels):
    return bool(set(labels) & TARGET_LABELS)

def process_issue(issue_number, labels, add_comment_fn, close_issue_fn):
    if should_process(labels):
        add_comment_fn(issue_number, COMMENT)
        close_issue_fn(issue_number)
        return True
    return False
