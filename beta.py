import joblib
import pickle
import numpy as np
import pandas as pd


with open ("weights_variables/scaler.pkl", "rb") as s:
    scaler = pickle.load(s)
    
    with open("weights_variables/lin_reg.joblib", "rb") as m:
        model = joblib.load(m)
        
        data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 2006, 51258, 4, 2]])
        
        data = {'Manufacturer': [0],
                'Category': [0],
                'Leather interior': [0],
                'Fuel type': [0],
                'Engine volume': [0],
                'Gear box type': [0],
                'Drive wheels': [0],
                'Wheel': [0],
                'Turbo': [0],
                'Prod. year': [2006],
                'Mileage': [51258],
                'Cylinders': [4],
                'Doors': [2]}
        
        new_data = pd.DataFrame(data)
        
        scaled_data = scaler.transform(new_data)
        
        print(scaler.get_feature_names_out())
        
        print(model.predict(scaled_data))

        