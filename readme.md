# Crypto ETL + ML Model ![Python](https://img.shields.io/badge/python-3.11-blue)


🚀 **Proyecto desarrollado en Python 3.11.12**. Se recomienda usar esta misma versión para evitar incompatibilidades.

## Requisitos

- Python 3.11.12
- Pip
- (Opcional) Virtualenv

## ¿Qué hace este proyecto?

- Realiza un ETL de datos de criptomonedas (por defecto Bitcoin).
- Entrena un modelo de regresión lineal para predecir precios futuros.
- Utiliza SQLite como base de datos para almacenar los datos.

## Estructura

scripts/
├── createTable.py # Crea la base de datos y la tabla
├── main.py # Ejecuta el ETL y el modelo
├── data/
│ ├── data_load.py
│ ├── model_predict.py
│ └── model_train.py


## Instalación

```bash
git clone https://github.com/facuvgaa/crypto-etl-airflow
# 🚨 Requiere Python 3.11.12 🚨
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

##Cómo correr Airflow
airflow db init 
airflow webserver --port 8080
airflow scheduler

## manual use 

task1 - python scripts/etl.py
task2 - python scripts/main.py

se puede jugar con el tiempo de prediccion, viene por defecto 1 minuto para probar rapidez, modificar a gusto, ademas de hace predicciones de BTC cuando puede hacer predicciones de todas las criptomonedas que la api te da y guarda en la db. 


# Crypto ETL + ML Model ![Python](https://img.shields.io/badge/python-3.11-blue)


🚀 **Project developed in Python 3.11.12**. It is recommended to use this version to avoid incompatibilities.

##Requirements

- Python 3.11.12
- pepita
- (Optional) Virtualenv

## What does this project do?

- Performs ETL of cryptocurrency data (Bitcoin by default).
- Trains a linear regression model to predict future prices.
- Uses SQLite as the database to store the data.

##Structure

scripts/
├── createTable.py # Create the database and table
├── main.py # Run the ETL and the model
├── data/
│ ├── load_data.py
│ ├── model_predict.py
│ └── model_train.py

## Installation

```
git clone https://github.com/facuvgaa/crypto-etl-airflow
# 🚨 Requires Python 3.11.12 🚨
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

##How to run Airflow
start database Airflow
Airflow web server --port 8080
Airflow scheduler

## manual use

task1 - python scripts/etl.py
task2 - python scripts/main.py

You can play with the prediction time. It comes with a default setting of 1 minute for quick testing and modification. It also makes BTC predictions, which can be used to make predictions for all the cryptocurrencies the API provides and saves to the database.

## License

This project is licensed under the MIT License.

## Autor

Walter Facundo Vega.
