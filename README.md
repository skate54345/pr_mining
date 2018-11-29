Runs in command line with repo path as argument
example: "python mining.py torvalds/linux"

- Mines all pull requests from a GitHub repository and scans each title for keywords
- Categorizes PRs into 3 categories and creates a csv with the format:
REPO_TITLE, BUG_FIX, NEW_FEATURE, REFACTORING\n
