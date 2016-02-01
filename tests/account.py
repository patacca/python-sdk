from __future__ import unicode_literals

from tests.test_helper import get_sdk


def test_account():
    sdk = get_sdk()
    assert 'id' in sdk.account.get()


if __name__ == '__main__':
    test_account()
