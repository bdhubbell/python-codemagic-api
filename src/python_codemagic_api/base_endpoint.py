import json
import requests

class BaseEndpoint:

    BASE_URL = 'https://api.codemagic.io'

    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            'X-Auth-Token': api_token,
            'Content-Type': 'application/json'
        }
        

    def get(self, endpoint, headers={}):
        return requests.get(
            f'{self.BASE_URL}/{endpoint}',
            headers={**self.headers, **headers}
        )

    def post(self, endpoint, data, headers={}):
        return requests.post(
            f'{self.BASE_URL}/{endpoint}',
            data=json.dumps(data),
            headers={**self.headers, **headers},
        )

    def delete(self, endpoint, data, headers={}):
        return requests.delete(
            f'{self.BASE_URL}/{endpoint}',
            data=json.dumps(data),
            headers={**self.headers, **headers},
        )
