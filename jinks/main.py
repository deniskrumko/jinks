import argparse
import subprocess
import webbrowser
from collections import OrderedDict
from typing import Optional

from .display import green, red
from .resources import (
    Environments,
    Projects,
    URLTypes,
    shortcuts,
    url_patterns,
)


class App:
    """Application to open links in specified project."""

    def __init__(self, project: Projects):
        """Initialize class instance."""
        self.project = project
        self.args = self.parse_arguments()
        self.task = self.args.task or ''
        self.env = self.get_environment()
        self.urls = OrderedDict()

    def run(self):
        """Run script."""
        if not self.task and not self.detect_task_from_git():
            exit('\nDefine task number or environment (rc, prod)' * red)

        self.add_urls([URLTypes.ADMIN, URLTypes.FRONT, URLTypes.API])

        if self.env == Environments.STAND:
            self.add_urls([URLTypes.JIRA])

            if self.project != Projects.RND:
                self.add_urls([
                    URLTypes.GITLAB,
                    URLTypes.K8S,
                    URLTypes.LOGHOUSE,
                ])

        name = self.issue if self.env == Environments.STAND else self.env

        output = f'\n {name * green}\n\n'

        choices = {}
        for index, key in enumerate(self.urls.keys()):
            choice = str(index + 1)
            value = self.urls[key]
            choices[choice] = value

            if key in shortcuts:
                displayed = shortcuts[key][1].ljust(19)
                choices[shortcuts[key][0]] = value
            else:
                displayed = key.ljust(9)

            output += f' {choice * green}  {displayed} {value}\n'

        if self.args.action and self.args.action in choices:
            action = self.args.action
        else:
            print(output)
            action = input('>>> ').lower()

        if action in choices:
            webbrowser.open(choices[action])

    def parse_arguments(self) -> argparse.Namespace:
        """Parse arguments."""
        parser = argparse.ArgumentParser(
            prog='mrpl',
            description=f'CLI to open {self.project} links',
            epilog='Ⓒ 2019 Denis Krumko'
        )
        parser.add_argument(
            'task',
            nargs='?',
            help='task/stand (1234, rc, prod)',
        )
        parser.add_argument(
            'action',
            nargs='?',
            help='j/k/s/l/a/f/i/g'
        )
        return parser.parse_args()

    def get_environment(self) -> Environments:
        """Get environment from task."""
        if self.task.lower() == 'rc':
            return Environments.RC

        if self.task.lower() in ('prod', 'production'):
            return Environments.PRODUCTION

        return Environments.STAND

    def add_urls(self, url_list: list):
        """Add urls from list to `self.urls` dict."""
        for url_type in url_list:
            url = self.get_url(url_type=url_type)
            if url:
                self.urls[url_type] = url

    def get_url(self, url_type: URLTypes) -> Optional[str]:
        """Get url from url patterns."""
        url = url_patterns.get(url_type)

        if isinstance(url, dict):
            try:
                url = url[self.env][self.project]
            except KeyError:
                return

        return url.format(
            task=self.task,
            issue=self.issue,
            issue_lower=self.issue.lower(),
            full_issue=self.full_issue,
        )

    def detect_task_from_git(self):
        """Detect task from git branch.

        If git branch is `feature/MRPL-1234`, then we can get task number
        from it!

        """
        try:
            command = 'git rev-parse --abbrev-ref HEAD'
            output = subprocess.check_output(command.split())
            output = output.decode('utf-8').strip()

            if self.project in output:
                task_number = output.split(self.project)[1][1:]
                if task_number.isdigit():
                    self.task = task_number
                    return True

        except Exception:
            return False

    def detect_origin_branch_name(self, issue: str) -> Optional[str]:
        """Detect full branch name for correct link to GitLab"""
        try:
            command = 'git branch -r'
            output = subprocess.check_output(command.split())
            output = output.decode('utf-8').strip()
            for line in output.splitlines():
                if issue.lower() in line.lower():
                    branch = line.lstrip('*').strip()  # * is current HEAD
                    branch = branch.split('/', 1)[1]  # cut '<remote_name>/'
                    return branch
        except Exception:
            pass
        return f'feature/{issue}'

    @property
    def issue(self):
        """Get task as JIRA issue."""
        return f'{self.project}-{self.task}'

    @property
    def full_issue(self):
        """Get branch full name for GitLab url."""
        return self.detect_origin_branch_name(self.issue)


if __name__ == '__main__':
    # App().run()
    import configparser
    config = configparser.ConfigParser
    result config.read('config.cgf')
    import ipdb; ipdb.set_trace(context=8)  # FIXME: Breakpoint
    return
