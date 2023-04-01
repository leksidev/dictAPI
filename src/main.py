import os
import json
from fastapi import FastAPI
from dotenv import load_dotenv
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = 'Token ' + os.getenv('TOKEN')
TRANSLATOR_TOKEN = os.getenv('TRANSLATOR_TOKEN')

app = FastAPI()


@app.get("/definition/{word}")
def get_definition_word(word):
    response = requests.get(url=f"https://owlbot.info/api/v4/dictionary/{word}",
                            headers={'Authorization': TOKEN})
    return response.json()


@app.get("/translate/{word}")
def get_translation_word(word):
    response = requests.post(url="https://dictionary.yandex.net/api/v1/dicservice.json/lookup",
                             params={'key': TRANSLATOR_TOKEN,
                                     'lang': 'en-ru',
                                     'text': word})
    translate = response.json()['def'][0]['tr'][0]['text']
    return json.dumps({'translate': translate}, ensure_ascii=False)

print(get_definition_word('yes'))
