from data.data_load import load_data
from model.model_train import train_model
from model.model_predict import predict


df, start_time = load_data("BTC")

model = train_model(df)

# Hacer una predicción
predicted_price = predict(model, df, start_time)