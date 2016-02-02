from __future__ import print_function

import os
from time import sleep

from credentials import CLIENT_ID, CLIENT_SECRET
from motaword_sdk import MotaWordSDK

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'test_files')

sdk = MotaWordSDK(CLIENT_ID, CLIENT_SECRET, debug=True)

"""
Get meta information how file formats and languages we support. These language codes will be used when creating a project.
"""
formats = sdk.info.formats()
languages = sdk.info.languages()

"""
Create a new project
"""
project = sdk.projects.create('en-US', ['fr', 'ru', 'tr'])
project_id = project['id']

"""
Get a list of projects
"""
project_list = sdk.documents.list(project_id)
print(project_list)

"""
Add files to the project: a document to be translated, style guide and glossary.
"""

# Returns the updated list of documents in the project.
documents = sdk.documents.upload(
    project_id,
    os.path.join(FILES_DIR, 'document.txt')
)
print(documents)

# Returns the updated list of style guides in the project.
style_guides = sdk.style_guides.upload(
    project_id,
    os.path.join(FILES_DIR, 'styleguide.pdf')
)
print(style_guides)

# Returns the single glossary. A project currently accepts only 1 glossary file.
glossaries = sdk.glossaries.upload(
    project_id,
    os.path.join(FILES_DIR, 'glossary.xlsx')
)
print(glossaries)

"""
Get the updated project information. Word count and price updated.
"""
project = sdk.projects.get(project_id)
print(project)

"""
Start the project. You will be charged only when you actually launch a project.
Sandbox environment does not launch the project, but returns a positive response.
"""
try:
    launch_response = sdk.projects.launch(project_id)
except:
    launch_response = None

print(launch_response)

"""
Get progress of the project, overall and per language.
"""
progress = sdk.projects.get_progress(project_id)
print(progress)


"""
Packaging flow
"""
# Package the latest translations and get them ready for download.
package = sdk.packaging.package_translation(project_id)
is_packaged = False

# Check the packaging process. When packaging is "completed", then we can download it.
while not is_packaged:
    package_status = sdk.packaging.check_status(project_id, package['key'])

    if package_status['status'] == 'completed':
        is_packaged = True

    sleep(2)

# Download the recently packaged translations.
if is_packaged:
    download = sdk.packaging.download_translations(project_id)

"""
Alternative packaging flow

Alternatively, you can call createPackage synchronously. It will package the most recent translations
and return the download() response. This call will take longer than usual as it waits for packaging to be complete.
"""
download = sdk.packaging.package_translation(project_id, async=0)


"""
Global style guide and glossary for corporate accounts
"""
sdk.global_files.update_style_guide(os.path.join(FILES_DIR, 'styleguide.pdf'))
sdk.global_files.update_glossary(os.path.join(FILES_DIR, 'glossary.xlsx'))
sdk.global_files.download_style_guide()
sdk.global_files.download_glossary()