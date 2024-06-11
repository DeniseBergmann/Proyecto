# código de main (principal)

from scraping import scrape_data
from data_processing import clean_and_transform_data
from analysis import analyze_data
import pandas as pd

urls = [
    "https://www.rapsodia.com.ar/woman/camisas-y-tops.html",
    "https://www.onasaez.com/product-category/mujer/remeras-tops-mujer/tops/",
    "https://www.benka.com.ar/sale/remeras-remerones1/"
]

all_products = []
for url in urls:
    products = scrape_data(url)
    all_products.extend(products)
    print(f"Se encontraron {len(products)} productos en {url}")

if len(all_products) == 0:
    print("No se encontraron productos en ninguna de las URLs proporcionadas. Revisa las URLs y la lógica de scraping.")
else:
    print(f"Se encontraron un total de {len(all_products)} productos.")

    df = clean_and_transform_data(all_products)
    price_summary, trend_analysis = analyze_data(df)

    if not df.empty:
        print("Resumen de precios:")
        print(price_summary)
        print("\nAnálisis de tendencias:")
        print(trend_analysis)

        df.to_csv('products_data.csv', index=False)
