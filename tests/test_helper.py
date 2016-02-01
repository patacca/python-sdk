from __future__ import unicode_literals

import os

import motaword_sdk

try:
    from .test_credentials import CLIENT_ID, CLIENT_SECRET
except ImportError:
    CLIENT_ID = ''
    CLIENT_SECRET = ''


def get_sdk(debug=True):
    client_id = os.environ.get('MOTAWORD_CLIENT_ID', CLIENT_ID)
    client_secret = os.environ.get('MOTAWORD_CLIENT_SECRET', CLIENT_SECRET)

    return motaword_sdk.MotaWordSDK(client_id, client_secret, debug=debug)
