from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json
from pprint import pprint

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

value_order = {
    'date_of_manufacturing': 0,
    'engine_power': 1,
    'fuel_type': 2,
    'latitude_coordinates': 3,
    'longitude_coordinates': 4,
    'manufacturer': 5,
    'mileage': 6,
    'price': 7,
    'seller_country_code': 8
}


@app.get("/")
def home():
    return {'carsonsale.info'}


@app.get("/{car_brands}")
def index(car_brands: str):
    df = pd.read_csv('cars_on_sale.csv')
    df = df.drop(columns=['seller_location'])
    out = {}
    data_list = []
    cc_list = []
    if ',' in car_brands:
        brands_list = car_brands.split(',')
        for brand in brands_list:
            d = get_data(df, brand)
            data_list += d[0]
            cc_list += d[1]
        cc_list = list(set(cc_list))
    else:
        d = get_data(df, car_brands)
        data_list += d[0]
        cc_list += d[1]
    out["cc"] = cc_list
    out["data"] = data_list
    return JSONResponse(out)


def get_data(df, brand):
    df_filtered = df.loc[df.manufacturer == brand]
    cc_codes = df_filtered.seller_country_code.unique().tolist()
    df_filtered = df_filtered.to_json(orient="values")
    json_out = json.loads(df_filtered)
    return json_out, cc_codes


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
