from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
import pandas as pd
import json
from pprint import pprint

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

app = FastAPI()

@app.get("/")
def home():
    return {'carsonsale.info'}


@app.get("/{car_brands}")
def index(car_brands: str):
    df = pd.read_csv('cars_on_sale.csv')
    if '%' in car_brands:
        print(car_brands)
        data_list = []
        brands_list = car_brands.split('%')
        print(brands_list)
        for brand in brands_list:
            df_filtered = df.loc[df.manufacturer == brand]
            out = df_filtered.to_json(orient="records")
            json_out = json.loads(out)
            print(brand)
            pprint(json_out)
            data_list += json_out
        return JSONResponse(data_list)
    df = df.loc[df.manufacturer == car_brands]
    out = df.to_json(orient='records')
    json_out = json.loads(out)
    return JSONResponse(json_out)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
