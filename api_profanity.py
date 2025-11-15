from abc_api_base import APIBase
import requests
import json

BASE_URL = 'https://vector.profanity.dev'


class APIProfanity(APIBase):
    def __init__(self, params, timeout=10):
        super().__init__(BASE_URL, params, timeout)
        self._params = params
        self._timeout = timeout
        self._base_url = BASE_URL
        self.__data = None

    def call_api(self):
        # Build payload from params
        if isinstance(self._params, dict):
            if 'message' in self._params:
                payload = {'message': self._params['message']}
            elif 'text' in self._params:
                payload = {'message': self._params['text']}
            elif 'name' in self._params:
                payload = {'message': self._params['name']}
            else:
                payload = self._params
        elif isinstance(self._params, str):
            payload = {'message': self._params}
        else:
            payload = {'message': str(self._params)}

        try:
            resp = requests.post(self._base_url, json=payload, timeout=self._timeout)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.RequestException as e:
            self._APIBase__message = f'A Network/HTTP error occurred {e}'
            self._APIBase__status = -1
            self.__data = None
            return self.status, self.message
        except ValueError:
            self._APIBase__message = 'The server response was not valid JSON'
            self._APIBase__status = -1
            self.__data = None
            return self.status, self.message
        else:
            self._APIBase__status = 0
            self._APIBase__message = None
            self.__data = data
            return self.status, self.__data

    def __str__(self):
        if self.__data is None:
            return '\nNo data available.'

        try:
            return '\n' + json.dumps(self.__data, indent=2)
        except (TypeError, ValueError):
            return '\n' + str(self.__data)
