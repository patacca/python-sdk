from __future__ import print_function

import os

from credentials import CLIENT_ID, CLIENT_SECRET
from motaword_sdk import MotaWordSDK

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')

sdk = MotaWordSDK(CLIENT_ID, CLIENT_SECRET, debug=True)

project = sdk.projects.create('en-US', ['ru'])
project_id = project['id']

project_list = sdk.documents.list(project_id)
print(project_list)

result = sdk.documents.upload(
    project_id,
    os.path.join(FILES_DIR, 'document.txt')
)
print(result)

document_id = result['documents'][0]['id']
document = sdk.documents.get(project_id, document_id)

result = sdk.documents.update(
    project_id,
    document_id,
    os.path.join(FILES_DIR, 'document2.txt')
)
print(result)

result = sdk.documents.download(project_id, document_id)
print(result)

result = sdk.documents.delete(project_id, document_id)
print(result)
