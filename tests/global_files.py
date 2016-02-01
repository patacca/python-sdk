from __future__ import unicode_literals

import os

from tests.test_helper import get_sdk

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FILES_PATH = os.path.join(BASE_PATH, 'files')


def test_integration():
    sdk = get_sdk()
    result = sdk.global_files.update_style_guide(
        os.path.join(FILES_PATH, 'styleguide.pdf'))
    assert result.status_code == 200

    result = sdk.global_files.download_style_guide()
    with open(os.path.join(FILES_PATH, 'styleguide.pdf')) as f:
        style_guide_pdf = f.read()
    assert result.content == style_guide_pdf

    result = sdk.global_files.update_glossary(
        os.path.join(FILES_PATH, 'glossary.xlsx'))
    assert result.status_code == 200

    result = sdk.global_files.download_glossary()
    with open(os.path.join(FILES_PATH, 'glossary.xlsx')) as f:
        glossary_xlsx = f.read()
    assert result.content == glossary_xlsx


if __name__ == '__main__':
    test_integration()
