# codigo para el scraping

import time
from bs4 import BeautifulSoup
import requests

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time} segundos")
        return result
    return wrapper

@measure_time
def scrape_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        if "rapsodia.com.ar" in url:
            # función para los selectores de Rapsodia
            for item in soup.select('.product-item-details'):
                name_element = item.select_one('.product-item-name')
                name = name_element.text.strip() if name_element else "No name found"
                price_element = item.select_one('.price')
                price = price_element.text.strip() if price_element else "No price found"
                availability = "Available"
                products.append({
                    'name': name,
                    'price': price,
                    'availability': availability
                })
        
        elif "onasaez.com" in url:
            # función para los selectores de Ona Saez
            for item in soup.select('.product'):
                name_element = item.select_one('.woocommerce-loop-product__title')
                name = name_element.text.strip() if name_element else "No name found"
                price_element = item.select_one('.price')
                price = price_element.text.strip() if price_element else "No price found"
                availability = "Available"
                products.append({
                    'name': name,
                    'price': price,
                    'availability': availability
                })
        
        elif "benka.com.ar" in url:
        # función para los selectores de Benka
            for item in soup.select('.item-description'):
                name_element = item.select_one('.item-name')
                name = name_element.text.strip() if name_element else "No name found"
                price_element = item.select_one('.item-price')
                price = price_element.text.strip() if price_element else "No price found"
                availability = "Available"
                products.append({
                    'name': name,
                    'price': price,
                    'availability': availability
                })
        
        if not products:
            print(f"No se encontraron productos en {url}")
        
        return products
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {url}: {e}")
        return []
