import requests

class DictionaryWrapper:
    def __init__(self, api_key):
        self.api_key=api_key
        self.base_url="https://api.dictionaryapi.dev/api/v2/entries/en/"
    def definition(self, word):
        url=self.base_url+word
        response=requests.get(url)
        data=response.json()
        print(data)