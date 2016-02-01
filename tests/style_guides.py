from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')


def test_integration():
    sdk = get_sdk()
    project = sdk.projects.create('en-US', ['ru'])
    project_id = project['id']

    style_guide_list = sdk.style_guides.list(project_id)
    assert isinstance(style_guide_list['styleguides'], list)

    style_guide = sdk.style_guides.upload(
        project_id,
        os.path.join(FILES_DIR, 'styleguide.pdf')
    )
    assert 'id' in style_guide['styleguides'][0]
    style_guide_id = style_guide['styleguides'][0]['id']

    result = sdk.style_guides.get(project_id, style_guide_id)
    assert result['id'] == style_guide_id

    result = sdk.style_guides.update(
        project_id,
        style_guide_id,
        os.path.join(FILES_DIR, 'styleguide2.pdf')
    )
    assert result['id'] == style_guide_id

    result = sdk.style_guides.download(
        project_id,
        style_guide_id
    )

    with open(os.path.join(FILES_DIR, 'styleguide2.pdf')) as f:
        styleguide2 = f.read()
    assert result.content == styleguide2

    result = sdk.style_guides.delete(project_id, style_guide_id)
    assert result['status'] == 'success'


if __name__ == '__main__':
    test_integration()
