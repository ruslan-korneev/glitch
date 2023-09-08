from datetime import datetime, timedelta
from enum import auto

from gitlab import Gitlab
from gitlab.const import MINIMAL_ACCESS
from strenum import LowercaseStrEnum

# MINIMAL_ACCESS.GUEST


class TimeTracker:
    # gitlab = Gitlab(oauth=user, get_gitlab_access_token())

    def __init__(self, project_id: int, user_id: int, gitlab: Gitlab):
        self.project_id = project_id
        self.username = user_id
        self.gitlab = gitlab

    def get_project(self):
        project = self.gitlab.projects.get(self.project_id)
        return project

    def get_user(self):
        user = self.gitlab.users.get(self.user_id)
        return user

    def get_time_by_project(self):
        """
        Method to get list of spent time for issues
        and merge-requests of certain project
        """
        return self.get_project().issues.list().mergerequest.list().asdict()

    def get_time_by_user(self):
        """
        Method to get list of spent time for issues
        and merge-requests by certain user
        """
        return self.get_user().issues.list().mergerequest.list().asdict()

    def get_time_by_user_and_project(self):
        """
        Method to get list of spent time for issues
        and merge-requests of certain project by certain user
        """
        return self.get_user().get_project().issues.list().mergerequest.list().asdict()

    def get_time_one_issue_or_merge_request(self):
        """
        Method to get list of spent time of one
        certain issue OR merge-request
        """
        return self.get_project().issues.list().mergerequest.list().asdict()

    def get_list_one_issue_or_merge_request_by_user(self):
        """
        Method to get list of spent time of one
        certain issue OR merge-request by certain user
        """
        return self.get_user().issues.list().mergerequest.list().asdict()


class Filter:
    @staticmethod
    def last_week_filter():
        datetime.now() - timedelta(weeks=1)

    @staticmethod
    def one_specific_date(date: int):
        datetime.strftime(date).format("%Y-%m-Yd")

    @staticmethod
    def daterange(first_date, second_date):
        datetime.date(first_date) - datetime.date(second_date)


class Target(LowercaseStrEnum):
    Issue = auto()
    Project = auto()


class SpentTime:
    target: Target
    spent_time: int
    posted_at: datetime | None
    gitlab_profile_id: int | None
