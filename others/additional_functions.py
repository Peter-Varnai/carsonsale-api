import pandas as pd
import numpy as np
from pprint import pprint


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('../cars_on_sale.csv')
# cc_list = df.seller_country_code.unique()

# def correct_strings(value):
#     value = value.lower()
#     value = value.replace(" ", "_")
#     value = value.replace("-", "_")
#     return value
# print(df.manufacturer.unique())

# df = df.dropna(subset=["manufacturer"])
# df.manufacturer = df.manufacturer.apply(correct_strings)
# df.loc[df.manufacturer == 'tesla', 'fuel_type'] = 'Electric'
# df.loc[df.manufacturer == 'polestar', 'fuel_type'] = 'Electric'
# df.loc[df.manufacturer == "citroën", "manufacturer"] = "citroen"
# df.loc[df.manufacturer == 'tesla', 'manufacturer'] = df.loc[df.manufacturer == 'tesla', 'manufacturer'].str.lower()
# df.loc[df.manufacturer == "chevrolet___daewoo", "manufacturer"] = "chevrolet"
# print(df.manufacturer.unique())

# df.loc[df['seller_country_code'] == 'FR', 'seller_country_code'] = -99

# df = df.rename(columns={})

# def get_data(df, brand):
#     df_filtered = df.loc[df.manufacturer == brand]
#     cc_codes = df_filtered.seller_country_code.unique().tolist()
#     df_filtered = df_filtered.to_json(orient="records")
#     json_out = json.loads(df_filtered)
#     return json_out, cc_codes

df = df.loc[df.manufacturer == 'audi'].sample(5)
df_fil = df.to_json(orient='records')
df_fil2 = df.to_json(orient='values')

pprint(df_fil)
pprint(df_fil2)


value_order = {
    'date_of_manufacturing': 1,
    'engine_power': 2,
    'fuel_type': 3,
    'latitude_coordinates':4,
    'longitude_coordinates': 5,
    'manufacturer': 6,
    'mileage': 7,
    'price': 8,
    'seller_country_code':9
}



# df.to_csv('cars_on_sale.csv', index = False)



