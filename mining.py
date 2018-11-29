from github import Github
import sys

#get access token
with open("token.txt","r") as csv:
    token = csv.read().replace('\n', '')
csv.close()

g = Github(token)

bug_tally = 0
feature_tally = 0
refactor_tally = 0

pull_titles = []

#inputs path from user args
repo_path = sys.argv[1]
repo = g.get_repo(repo_path)
pulls = repo.get_pulls(state='closed', sort='created', base='master')

for pr in pulls:
    pull_titles.append(pr.title)
    if "bug" in pr.title or "fix" in pr.title or "patch" in pr.title or "smell" in pr.title:
        bug_tally = bug_tally+1
    if "new" in pr.title or "feature" in pr.title or "add" in pr.title or "implement" in pr.title:
        feature_tally = feature_tally+1
    #"rewr" covers rewrite and rewrote
    if "refactor" in pr.title or "rewr" in pr.title or "revise" in pr.title or "restructure" in pr.title:
        refactor_tally = refactor_tally+1

total_num = len(pull_titles)
total_that_have_keywords = bug_tally+feature_tally+refactor_tally
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("repository: %s" % repo_path)
print("total pull request titles scanned: %s" % total_num)
print("total titles with any keyword: %s" % total_that_have_keywords)
print("bug fixes: %s" % bug_tally)
print("new features: %s" % feature_tally)
print("refactoring: %s" % refactor_tally)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCSV ready!")


#create csv

#append to end of file
with open("data.csv","a") as csv:
    csv.write("%s, %s, %s, %s, %s\n" % (repo_path, total_that_have_keywords, bug_tally, feature_tally, refactor_tally))
csv.close()
