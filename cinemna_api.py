import requests

API_KEY = "cinema_api_key_here"
BASE_URL = "https://api.cinemaapi.com"

def get_cinemas(location):
    endpoint = f"{BASE_URL}/cinemas"
    params = {
        "location": location,
        "apiKey": API_KEY
    }
    response = requests.get(endpoint, params=params)
    return response.json()

def get_showtimes(cinema_id, date):
    endpoint = f"{BASE_URL}/showtimes"
    params = {
        "cinemaId": cinema_id,
        "date": date,
        "apiKey": API_KEY
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# How to use
cinemas = get_cinemas("London")
if cinemas.get("cinemas"):
    cinema_id = cinemas["cinemas"][0]["id"]
    showtimes = get_showtimes(cinema_id, "2023-08-22")
    print(showtimes)
else:
    print("No cinemas found.")
