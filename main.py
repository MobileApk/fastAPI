"""
My Main file
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return 'Namaste bharat'