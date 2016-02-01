from __future__ import unicode_literals

from tests.test_helper import get_sdk


def test_endpoints():
    sdk = get_sdk()
    assert 'swagger' in sdk.info.endpoints()


def test_languages():
    sdk = get_sdk()
    assert 'name' in sdk.info.languages()[0]


def test_formats():
    sdk = get_sdk()
    assert 'documents' in sdk.info.formats()


if __name__ == '__main__':
    test_endpoints()
    test_languages()
    test_formats()
