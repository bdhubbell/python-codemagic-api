from python_codemagic_api.base_endpoint import BaseEndpoint

class Artifacts(BaseEndpoint):

    ENDPOINT = 'artifacts'
    
    def __init__(self, api_token, app_id):
        self.api_token = api_token
        self.app_id = app_id