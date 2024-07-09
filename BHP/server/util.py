import json
import pickle
import numpy as np
import pandas as pd
__locations=None
__data_columns=None
__model=None
def get_estimated_price(location,sqm2,bhk,bath):#the second routine

    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(__data_columns))
    x[1] = sqm2
    x[0] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return (__model.predict([x])[0],)


def load_saved_artifacts():
    print("loading saved artifacts...Start")
    global __locations
    global __data_columns
    
    with open("C:/Users/Walid/Desktop/project1/BHP/server/artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    
    global __model
    if __model is None:
        with open("C:/Users/Walid/Desktop/project1/BHP/server/artifacts/tunisian_home_prices_model.pickle",'rb') as f:
            __model=pickle.load(f)
    
    print("loading saved artifacts...done")


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('hammamet',92.9,2,2))
    print(get_estimated_price('ras jbal',92.9,3,3))
    print(get_estimated_price('sidi boubakr',92.9,2,2))
    print(get_estimated_price('sbitla',92.9,2,2))