# código de data processing

import pandas as pd

def clean_and_transform_data(products):
    df = pd.DataFrame(products)
    print("Datos antes del procesamiento:")
    print(df)

    if df.empty:
        print("No hay datos para procesar.")
        return df

    # Función para filtrar los datos para eliminar aquellos sin nombre o sin precio
    df = df[(df['name'] != 'No name found') & (df['price'] != 'No price found')]

    # Función para convertir el precio a formato numérico y normalizar la disponibilidad
    df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float)
    df['availability'] = df['availability'].apply(lambda x: x.lower() == 'available')

    print("Datos después del procesamiento:")
    print(df)

    return df
