import requests
import git
import sys
import configparser

from requests.auth import HTTPBasicAuth

configs = configparser.ConfigParser()
configs.read('../../projects.ini')

message = sys.argv[2]
project_name = sys.argv[1]
jenkins_auth_url = configs['generic']['jenkins_auth_url']
jenkins_url = configs[project_name]['jenkins_url']
repo_url = configs[project_name]['repo']
repo_orig = configs[project_name]['origin']


def git_push(url, orig):
    git_repo = git.Repo(url)
    git_repo.index.commit(message)
    origin = git_repo.remote(orig)
    origin.push()


def execute_jenkins():
    user = configs['generic']['user']
    api_token = configs['generic']['api_token']
    response = requests.get(jenkins_auth_url, auth=HTTPBasicAuth(user, api_token))
    credentials = response.content.decode('utf-8').split(':')
    print('Credentials retrieved from jenkins')
    h = {
        credentials[0]: credentials[1]
    }
    requests.post(jenkins_url, headers=h, auth=HTTPBasicAuth(user, api_token))
    print('Build request send')


def main():
    try:
        # git_push(repo_url, repo_orig)
        execute_jenkins()
    except ValueError:
        print(f'Failed to execute - Details {ValueError}')


main()
