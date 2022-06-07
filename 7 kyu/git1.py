from git import Repo
from datetime import datetime
# from time import time, gmtime

PATH_OF_GIT_REPO = r'S:/Everything/codewars/'  # make sure .git folder is properly configured
COMMIT_MESSAGE = "Last Sync: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def git_push():
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(A=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()


git_push()
# datetime.now().strftime("%Y-%m-%d %H:%M:%S")