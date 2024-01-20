import sys

from github import Github

# Authentication is defined via github.Auth
from github import Auth

user = sys.argv[1]
password = sys.argv[2]

# using an access token
# auth = Auth.Token(token)
print("user:", user)
print("password:", password)
auth = Auth.Login(user, password)

# First create a Github instance:
# print("token:", token)
# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

# query code
# ts.set_token
code = "hello=world"
repositories = g.search_repositories(query=code)
for repo in repositories:
    print(repo)
    print(repo.clone_url)

    print(repositories.totalCount)  # 打印总数

    break

# To close connections after use
g.close()
