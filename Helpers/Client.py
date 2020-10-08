import json
import requests

ACCESS_TOKEN = '6e6440fc8fb8134f95231d15d458f9ab6110936869ab9a0cfca92ca4abea6a2e'
BASE_URL = 'https://gorest.co.in/'
TIMEOUT = 10


class ClientApi:

    def __init__(self, token=None):
        self.base_url = BASE_URL
        self.token = token

    def get_default_headers(self):
        if self.token is not None:
            return {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json',
            }
        return {'Content-Type': 'application/json'}

    def get(self, url, **kwargs):
        full_url = self.base_url + url
        kwargs.setdefault('headers', {}).update(self.get_default_headers())
        print(full_url, kwargs, sep='\n')
        try:
            response = requests.get(full_url, timeout=TIMEOUT, **kwargs)
            print(response, response.text)
            return response.json()
        except requests.exceptions.Timeout as e:
            raise SystemExit(e)

    def post(self, url, **kwargs):
        full_url = self.base_url + url
        kwargs.setdefault('headers', {}).update(self.get_default_headers())
        print(full_url, kwargs.items(), sep='\n')
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])
        try:
            response = requests.post(full_url, timeout=TIMEOUT, **kwargs)
            print(response, response.text)
            return response.json()
        except requests.exceptions.Timeout as e:
            raise SystemExit(e)

