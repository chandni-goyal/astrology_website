import requests

API_BASE_URL = 'https://api.divineapi.com'  # Replace with the actual API URL
API_KEY = 'your_api_key_here'


def fetch_daily_horoscope(sign):
    url = f"{API_BASE_URL}/horoscope/daily"
    headers = {'Authorization': f'Bearer {API_KEY}'}
    params = {'sign': sign}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()  # Assumes the API returns JSON data
    except requests.RequestException as e:
        print(f"Error fetching horoscope: {e}")
        return None
