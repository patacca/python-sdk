from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')


def test_integration():
    sdk = get_sdk()
    project = sdk.projects.create('en-US', ['ru'])
    project_id = project['id']

    activity_list = sdk.activities.list(project_id)
    isinstance(activity_list['activities'], list)

    project_comment_list = sdk.activities.list_comments(project_id)
    isinstance(project_comment_list['comments'], list)


if __name__ == '__main__':
    test_integration()
