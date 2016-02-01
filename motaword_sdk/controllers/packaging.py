from __future__ import unicode_literals

from motaword_sdk.controllers.base import BaseController


class Packaging(BaseController):
    def package_translation(self, project_id, language='', async=1):
        """
        Package the translation project, make it ready to be downloaded.

        Args:
            project_id: int
            language: str
            async: int

        Returns: mixed response from the API call
        """
        path = '/projects/{project_id}/package/{language}'.format(
            project_id=project_id,
            language=language)

        if async:
            return self._request_json(path, 'post', params={'async': async})
        else:
            return self._request(path, 'post', params={'async': async})

    def check_status(self, project_id, key):
        """
        This request will tell you the current progress of the translation packaging.
        You will use the 'key' provided by the /package call

        Args:
            project_id: int
            key: str

        Returns: mixed response from the API call
        """
        path = '/projects/{project_id}/package/check'.format(
            project_id=project_id)

        return self._request_json(path, params={'key': key})

    def download_translations(self, project_id, language=''):
        """
        Download the latest translation package.
        If a language is provided, only the translation package of that language is returned.
        You must have given a /package call beforehand and wait until the packaging status is 'completed'.

        Args:
            project_id: int
            language: str

        Returns: mixed response from the API call
        """
        path = '/projects/{project_id}/download/{language}'.format(
            project_id=project_id, language=language)

        return self._request_json(path)
