from fastapi import FastAPI
import requests


app = FastAPI()


@app.get("/")
async def root():
    sahkohinta_api ="https://www.sahkohinta-api.fi/api/v1/halpa?tunnit=2&tulos=haja&aikaraja=2024-11-03" #ok
    sahkonhintatanaan_api = "https://www.sahkonhintatanaan.fi/api/v1/prices/2024/11-03.json"
    porssisahko_api="https://api.porssisahko.net/v1/price.json?date=2024-11-03&hour=7" #ok
    product_data = requests.get(porssisahko_api).json()
    return {"data": product_data}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
