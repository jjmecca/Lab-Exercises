import requests

class DictionaryWrapper:
    def __init__(self):
        self.base_url="https://api.dictionaryapi.dev/api/v2/entries/en/"
    def definition(self, word):
        url=self.base_url+word
        response=requests.get(url)
        data=response.json()
        return data[0]['meanings'][0]['definitions'][0]['definition']
print(DictionaryWrapper().definition("balls"))