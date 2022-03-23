from deep_translator import GoogleTranslator
import random
import json
from pathlib import Path

class Translator:
    def __init__(self):
        project_root = Path(__file__).parent.parent
        with open(project_root / 'data/country_with_language.json') as f:
            self.countries = json.load(f)
        self.supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)

    def translate(self, text, num_of_countries=10):
        self.text = text

        self.random_countries = random.sample(self.countries, num_of_countries)
        self.responses = []
        for country in self.random_countries:
            if country['lang_code'] is not None and country['lang_code'] in self.supported_languages.values():
                response = {}
                response['country'] = country['country_name']
                response['longitude'] = country['longitude']
                response['latitude'] = country['latitude']
                response['lang_code'] = country['lang_code']
                response['lang_name'] = country['lang_name']
                response['translation'] = GoogleTranslator(
                    source='auto', target=country['lang_code']).translate(text=text)
                self.responses.append(response)
        return self.responses
