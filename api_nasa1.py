#API: Application Programming Interfaces
#Nasa API: https://api.nasa.gov/
#API_KEY_NASA: imxenWKTiuKcgC8TAZWJoq5Es3FpzyvdfOXrYYBU
#Developer David C. Mosquera
#Date: 24012024
#Script description: Get and read data from NASA API about comets
#https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key=imxenWKTiuKcgC8TAZWJoq5Es3FpzyvdfOXrYYBU

import requests
def get_comet_data(api_key):
    print("::: COMET INFORMATION:::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        #Realizar la solicitud a la API
        response = requests.get(url)
        response.raise_for_status() #Valida si sepresenta algun error en la peticion
        #Convertir la respuesta a formato JSON (JS Object Notation)
        datos = response.json()

        print(f"Comet name: {datos['name']}")
        print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max: {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (Km): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")

    except request.exceptions.RequestException as e:
        print(f"Error al realizar la peticion a la API de NASA: {e}")

api_key_nasa = 'imxenWKTiuKcgC8TAZWJoq5Es3FpzyvdfOXrYYBU'

get_comet_data(api_key_nasa)
