"""
Automated Comment Bot
Triggers on new issues labeled 'feedback' or 'suggestion'
Adds comment 'Thank you for your contribution!' and closes issue
"""
import sys

def process_issue(labels, issue_number):
    if any(label in ['feedback', 'suggestion'] for label in labels):
        print(f"Issue #{issue_number}: Adding comment 'Thank you for your contribution!'")
        print(f"Issue #{issue_number}: Closing issue")
        return True
    else:
        print(f"Issue #{issue_number}: Label not in target list, skipping")
        return False

if __name__ == "__main__":
    process_issue(["feedback"], 1)
    process_issue(["suggestion"], 2)
    process_issue(["bug"], 3)
