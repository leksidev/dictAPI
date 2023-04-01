import os
import json
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse
from dotenv import load_dotenv
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = 'Token ' + os.getenv('TOKEN')
TRANSLATOR_TOKEN = os.getenv('TRANSLATOR_TOKEN')

app = FastAPI()


@app.get("/definition/{word}", response_class=JSONResponse, description='get definition word in english')
def get_definition_word(word: str):
    response = requests.get(url=f"https://owlbot.info/api/v4/dictionary/{word}",
                            headers={'Authorization': TOKEN})
    definitions = [x['definition'] for x in response.json()['definitions']]
    return json.dumps({'definitions': definitions, })


@app.get("/translate/{word}", response_class=JSONResponse, description='get translate word from english to russian')
def get_translation_word(word: str = 'deer'):
    response = requests.post(url="https://dictionary.yandex.net/api/v1/dicservice.json/lookup",
                             params={'key': TRANSLATOR_TOKEN,
                                     'lang': 'en-ru',
                                     'text': word})
    translate = response.json()['def'][0]['tr'][0]['text']
    return json.dumps({'translate': translate, }, ensure_ascii=False)