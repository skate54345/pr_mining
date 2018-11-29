- Generate and copy an access token through GitHub
- Create "token.txt" and paste your token
- Run in command line with repo path as argument
example: "python mining.py torvalds/linux"

- Mines all pull requests from a GitHub repository and scans each title for keywords
- Categorizes PRs into 3 categories and creates a csv with the format:
REPO_TITLE, TOTAL_TITLES_WITH_KEYWORDS, BUG_FIX, NEW_FEATURE, REFACTORING\n
