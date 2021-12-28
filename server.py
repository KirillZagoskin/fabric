#pet-project fabric on fastapi

from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()

@app.get('/')
def main_page():
    response = Response('<h1>Hello, World!</h1>', media_type='text/html')
    return response