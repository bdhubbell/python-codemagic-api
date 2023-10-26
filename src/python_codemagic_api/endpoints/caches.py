from python_codemagic_api.base_endpoint import BaseEndpoint


class Caches(BaseEndpoint):

    ENDPOINT = 'caches'

    def __init__(self, api_token, app_id):
        self.api_token = api_token
        self.app_id = app_id
        