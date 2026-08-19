# Auto Comment Bot Implementation

This repository contains a GitHub Actions workflow that automatically adds a comment and closes issues.

**Workflow file:** `.github/workflows/auto-comment-bot-implementation.yml`

**Trigger:**
- issues: opened, labeled

**Logic:**
- If issue has label `feedback` OR `suggestion`
- Add comment: `Thank you for your contribution!`
- Close the issue

**Test Results 2026-08-19:**
- UI improvement (feedback) -> closed ✅
- New feature (suggestion) -> closed ✅
- Login error (bug) -> open ✅
