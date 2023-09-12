from datetime import datetime, timedelta
from enum import auto

from gitlab import Gitlab
from gitlab.const import AccessLevel
from strenum import LowercaseStrEnum


class TimeTracker:
    def __init__(self, gitlab: Gitlab) -> None:
        self.gitlab = gitlab

    def get_project_list(self):
        return self.gitlab.projects.list(min_access_level=AccessLevel.GUEST)

    def get_project(self, project_id: int):
        return self.gitlab.projects.get(project_id)

    def get_current_user(self):
        return self.gitlab.user

    def get_spent_time_for_issues_by_project(self, project_id: int):
        """
        Method to get list of spent time
        for issues by certain project
        """
        return self.get_project(project_id).issues.list()

    def get_spent_time_for_mergerequests_by_project(self, project_id: int):
        """
        Method to get list of spent time for
        merge-requests by certain project
        """
        return self.get_project(project_id).mergerequests.list()

    # ===================================================================================

    def get_spent_time_for_issues_by_user(self):
        """
        Method to get list of spent time
        for issues by certain user
        """
        return self.gitlab.user.issues.list()

    def get_spent_time_for_mergerequests_by_user(self):
        """
        Method to get list of spent time for
        merge-requests by certain user
        """
        return self.gitlab.user.mergerequest.list()

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
