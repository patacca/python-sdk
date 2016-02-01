from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')


def test_integration():
    sdk = get_sdk()

    project = sdk.projects.create(
        'en-US',
        ['ru', 'et'],
        document=os.path.join(FILES_DIR, 'document.txt'),
        glossary=os.path.join(FILES_DIR, 'glossary.xlsx'),
        style_guide=os.path.join(FILES_DIR, 'styleguide.pdf'),
    )
    assert 'id' in project

    project_id = project['id']

    project_list = sdk.projects.list()
    assert isinstance(project_list['projects'], list)

    result = sdk.projects.get(project_id)
    assert result['id'] == project_id

    result = sdk.projects.update(project_id, 'en-US', ['ru', 'et'])
    assert result['source_language'] == 'en-US'

    result = sdk.projects.launch(project['id'])
    assert result['status'] == 'started'

    result = sdk.projects.progress(project['id'])
    assert 'total' in result


if __name__ == '__main__':
    test_integration()
