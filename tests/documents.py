from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')


def test_integration():
    sdk = get_sdk()
    project = sdk.projects.create('en-US', ['ru'])
    project_id = project['id']

    project_list = sdk.documents.list(project_id)
    assert isinstance(project_list['documents'], list)

    result = sdk.documents.upload(
        project_id,
        os.path.join(FILES_DIR, 'document.txt')
    )
    assert 'id' in result['documents'][0]

    document_id = result['documents'][0]['id']
    document = sdk.documents.get(project_id, document_id)
    assert document['id'] == document_id

    result = sdk.documents.update(
        project_id,
        document_id,
        os.path.join(FILES_DIR, 'document2.txt')
    )
    assert 'id' in result

    result = sdk.documents.download(project_id, document_id)

    with open(os.path.join(FILES_DIR, 'document2.txt')) as f:
        document2 = f.read()

    assert result.content == document2

    result = sdk.documents.delete(project_id, document_id)
    assert result['status'] == 'success'


if __name__ == '__main__':
    test_integration()
