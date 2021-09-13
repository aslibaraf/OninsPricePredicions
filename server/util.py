import pickle
import json
import numpy as np

__market = None
__data_columns = None
__model = None

def get_estimated_price(market,min_price,max_price):
    try:
        loc_index = __data_columns.index(market.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = min_price
    x[1] = max_price
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],0)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __market

    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __market = __data_columns[2:]

    global __model
    if __model is None:
        with open('./model/farm1.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def marketlist():
    return __market

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(marketlist())
    print(get_estimated_price('abohar',2560, 4800))
    print(get_data_columns())