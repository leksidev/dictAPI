import os
from fastapi import FastAPI
from dotenv import load_dotenv
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = 'Token ' + os.getenv('TOKEN')

app = FastAPI()


@app.get("/{word}")
def get_definition_word(word):
    response = requests.get(url=f'https://owlbot.info/api/v4/dictionary/{word}',
                            headers={'Authorization': TOKEN})
    return response.json()
