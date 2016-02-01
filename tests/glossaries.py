from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FILES_PATH = os.path.join(BASE_PATH, 'files')


def test_integration():
    sdk = get_sdk()
    project = sdk.projects.create('en-US', ['ru'])

    glossary_list = sdk.glossaries.list(project['id'])
    assert 'glossaries' in glossary_list

    glossary = sdk.glossaries.upload(
        project['id'],
        os.path.join(FILES_PATH, 'glossary.xlsx')
    )
    assert 'id' in glossary

    glossary = sdk.glossaries.get(project['id'], glossary['id'])
    assert 'id' in glossary

    with open(os.path.join(FILES_PATH, 'glossary.xlsx')) as f:
        glossary_xlsx = f.read()
    result = sdk.glossaries.download(project['id'], glossary['id'])
    assert result.content == glossary_xlsx

    result = sdk.glossaries.delete(project['id'], glossary['id'])
    assert result['status'] == 'success'


if __name__ == '__main__':
    test_integration()
