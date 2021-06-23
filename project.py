import requests
 
from datetime import datetime
 
apikey="70eec3832026d6db375972c5a382a6fe"
location=input("enter the city name:")
 
complete_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apikey
api_link = requests.get(complete_link)
api_data = api_link.json()
 
temp_city =((api_data["main"]['temp']) - 273.15)
weather=api_data['weather'][0]["description"]
humidity=api_data["main"]['humidity']
date_time= datetime.now().strftime("%d %b %Y |  %I:%M:%S %p")
 
print("weather stats for - {} ||{}".format(location.upper(), date_time))
print("Temperature of the city:",temp_city,"deg C")
print("weather of the city:", weather)
print("Humidity of the city:", humidity,"%")
