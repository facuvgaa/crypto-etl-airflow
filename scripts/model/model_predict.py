import datetime
import numpy as np 

def predict(model, df, start_time):
    next_timestamp = np.array([[df["timestamp"].max() + 60]])
    predict_price = model.predict(next_timestamp)[0]
    
    start_time = datetime.datetime.utcfromtimestamp(start_time)
    next_time = start_time + datetime.timedelta(seconds=int(next_timestamp[0][0]))


    print(f"prediccion pára {next_time} : ${predict_price:2f}")
    return predict_price

