import requests

class DictionaryWrapper:
    def __init__(self):
        self.base_url="https://api.dictionaryapi.dev/api/v2/entries/en/"
    def definition(self, word):
        try:
            url=self.base_url+word
            response=requests.get(url)
            data=response.json()
            return data[0]['meanings'][0]['definitions'][0]['definition']
        except:
            return "No data found"
    def exampleUsage(self, word):
        try:
            url = self.base_url + word
            response = requests.get(url)
            data = response.json()
            return data[0]['meanings'][0]['definitions'][0]['example']
        except:
            return "No data found"
    def pronounciation(self, word):
        try:
            url = self.base_url + word
            response = requests.get(url)
            data = response.json()
            return data[0]['phonetics'][1]['text']
        except:
            return "No data found"
    def partOfSpeech(self, word):
        try:
            url = self.base_url + word
            response = requests.get(url)
            data = response.json()
            return data[0]['meanings'][0]['partOfSpeech']
        except:
            return "No data found"