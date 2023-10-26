import requests

class BaseEndpoint:

    BASE_URL = 'https://api.codemagic.io'

    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            'x-auth-token': api_token
        }
        

    def get(self, endpoint, headers={}):
        return requests.get(
            f'{self.BASE_URL}/{endpoint}',
            headers={**self.headers, **headers}
        )

    def post(self, endpoint, headers={}, data={}):
        return requests.post(
            f'{self.BASE_URL}/{endpoint}',
            headers={**self.headers, **headers},
            data=data
        )

    def delete(self, endpoint, headers={}, data={}):
        return requests.delete(
            f'{self.BASE_URL}/{endpoint}',
            headers={**self.headers, **headers},
            data=data
        )
