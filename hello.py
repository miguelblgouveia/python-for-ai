import requests

def get_weather(latitude, longitude):
     url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
     response = requests.get(url)
     data = response.json()
     return data['current_weather']['temperature']

latitude_paris = 48.85 # Paris
longitude_paris = 2.35 # Paris

latitude_funchal = 32.65 # Funchal
longitude_funchal = -16.92 # Funchal

temperature_paris = get_weather(latitude_paris, longitude_paris)  

temperature_funchal = get_weather(latitude_funchal, longitude_funchal)

print(f"A temperatura atual em Paris é {temperature_paris}°C")
print(f"A temperatura atual em Funchal é {temperature_funchal}°C")