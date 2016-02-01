from __future__ import unicode_literals

from tests.test_helper import get_sdk


def test_integration():
    sdk = get_sdk()
    project = sdk.projects.create('en-US', ['ru'])
    project_id = project['id']

    sdk.projects.launch(project_id)

    result = sdk.packaging.package_translation(project_id, 'ru')
    assert 'key' in result
    key = result['key']

    result = sdk.packaging.check_status(project_id, key)
    assert result['status'] in ['packaging', 'completed']


if __name__ == '__main__':
    test_integration()
