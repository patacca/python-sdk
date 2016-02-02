from __future__ import unicode_literals

from motaword_sdk.controllers.base import BaseController


class Projects(BaseController):
    def update(self, project_id, source_language, target_languages,
               callback_url=None, custom=None):
        """
        Update project language pairs

        Args:
            project_id: int
            source_language: string
            target_languages: list
            callback_url: string
            custom: list

        Returns: mixed response from the API call
        """
        data = {
            'source_language': source_language,
            'target_languages[]': target_languages
        }

        if callback_url:
            data['callback_url'] = callback_url
        if custom:
            data['custom'] = custom

        path = '/projects/{project_id}'.format(project_id=project_id)

        return self._request_json(path,
                                  method='post',
                                  data=data,
                                  params={'method': 'put'})

    def list(self, page=1, per_page=10):
        """
        Get a list of your projects
        Args:
            page: int
            per_page: int

        Returns: mixed response from the API call
        """
        return self._request_json('/projects',
                                  params={'page': page, 'per_page': per_page})

    def create(self, source_language, target_languages, callback_url=None,
               custom=None, document=None, glossary=None, style_guide=None):
        """

        Args:
            source_language: string
            target_languages: list
            callback_url: string
            custom: list
            document: string
            glossary: string
            style_guide: string

        Returns: mixed response from the API call
        """
        data = {
            'source_language': source_language,
            'target_languages[]': target_languages,
            'callback_url': callback_url,
            'custom': custom or []
        }

        files = {}

        if document:
            files['documents[]'] = open(document, 'rb')

        if glossary:
            files['glossaries[]'] = open(glossary, 'rb')

        if style_guide:
            files['styleguides[]'] = open(style_guide, 'rb')

        return self._request_json('/projects', 'post', data=data, files=files)

    def get(self, project_id):
        """
        Get single project

        Args:
            project_id: int

        Returns: mixed response from the API call
        """
        path = '/projects/{project_id}'.format(project_id=project_id)

        return self._request_json(path)

    def launch(self, project_id, payment_method=None,
               payment_code=None, budget_code=None):
        """
        Launch the project

        Args:
            project_id: int
            payment_method: str
            payment_code: str
            budget_code: str

        Returns: mixed response from the API call
        """
        data = {}

        if payment_method:
            data['payment_method'] = payment_method

        if payment_code:
            data['payment_code'] = payment_code

        if budget_code:
            data['budget_code'] = budget_code

        path = '/projects/{project_id}/launch'.format(project_id=project_id)

        return self._request_json(path, 'post', data=data)

    def get_progress(self, project_id):
        """
        Get the progress of an already launched project

        Args:
            project_id: int

        Returns: mixed response from the API call
        """
        path = '/projects/{project_id}/progress'.format(project_id=project_id)
        return self._request_json(path)
