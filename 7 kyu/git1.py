from git import Repo
from datetime import datetime
# from time import time, gmtime

# PATH_OF_GIT_REPO = r'S:/Everything/codewars/'  # make sure .git folder is properly configured
git_repos = ['S:/Everything/codewars/', 'S:/obsidian_vault/lucky/notes', ]


def git_push(repo_path):
    git = Repo(repo_path).git
    git.add(A=True)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        git.commit('-m', "Last Sync: " + current_time)
        git.push()
    except Exception as e:
        with open(f'S:/Everything/git_errors_{repo_path}.txt', 'a') as git_errors:
            print(e, current_time, file=git_errors)


for repo_path in git_repos:
    git_push(repo_path)
# datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Gives a list of the differing objects
# diff_list = repo.head.commit.diff()

# for diff in diff_list:
#     # Print the old file path
#     print(diff.a_path)

#     # Print the new file path. If the filename (or path) was changed it will differ
#     print(diff.b_path)

# # Too many options to show. This gives a comprehensive description of what is available
# print(diff_list)
