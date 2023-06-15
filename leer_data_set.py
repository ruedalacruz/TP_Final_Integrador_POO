import pandas as pd

def leer_data_set():
    
    archivo_csv = "./RUEDA_BUJAN/observatorio-de-obras-urbanas.csv"
    try:
        df = pd.read_csv(archivo_csv, sep=",")
        return df
    except FileNotFoundError as e:
        print("Error al conectar el dataset", e)
        return False