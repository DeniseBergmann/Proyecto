# código para el analisis

import pandas as pd
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time} segundos")
        return result
    return wrapper

@measure_time
def analyze_data(df):
    if df.empty:
        print("No hay datos para analizar.")
        return pd.Series(), pd.DataFrame()

    price_summary = df.groupby('name')['price'].mean()
    trend_analysis = df.groupby('name')['price'].describe()
    return price_summary, trend_analysis
