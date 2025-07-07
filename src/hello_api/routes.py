from fastapi import FastAPI
from .config import Settings, Config


#the app var will be an instance of the FastAPI class
app = FastAPI()
app_settings = Settings()  # Load settings from config

#this tells FastAPI that the function handles requests that go to the path "/" using a get
@app.get("/")
async def root():
    return {"message": f"Hello World, welcome to {app_settings.proj_name}"}