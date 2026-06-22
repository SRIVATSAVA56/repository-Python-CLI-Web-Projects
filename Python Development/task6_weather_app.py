import requests

def get_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=j1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        weather_data = response.json()
        
        current_condition = weather_data['current_condition'][0]
        temp_c = current_condition['temp_C']
        humidity = current_condition['humidity']
        weather_desc = current_condition['weatherDesc'][0]['value']
        
        # Output real-time info
        print(f"\n--- Real-Time Weather Info: {city_name.strip().title()} ---")
        print(f"● Temperature: {temp_c}°C")
        print(f"● Humidity: {humidity}%")
        print(f"● Condition: {weather_desc}")
        print("-" * 40)
        
    except requests.exceptions.HTTPError:
        print("Error: City not found or API service temporarily unavailable.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except (KeyError, IndexError):
        print("Error: Could not parse weather data for the specified location.")

if __name__ == "__main__":
    print("--- Weather App ---")
    city = input("Enter city name: ").strip()
    
    if city:
        get_weather(city)
    else:
        print("Error: City name cannot be empty.")