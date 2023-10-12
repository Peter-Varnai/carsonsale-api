import pandas as pd
from random import randint
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


# GENERATING RANDOM COLORS FOR CSS CLASSES
# brand_list = df.manufacturer.unique().tolist()
# for brand in brand_list:
#     print(f'\n.{brand} path {{\n\tfill: rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})\n}}')


def fuel_corrector(input):
    if input == 'Electric/Gasoline' or input == 'Electric/Diesel':
        return 'hybrid'
    else:
        return input.lower()



df.fuel_type = df.fuel_type.apply(fuel_corrector)



df.to_csv('../cars_on_sale.csv', index = False)



