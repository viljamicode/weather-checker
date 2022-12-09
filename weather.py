import requests

# Ask the user to input a city and a country
city = input("Enter a city: ")
country = input("Enter a country: ")

# Use the OpenWeatherMap API to get the current weather for the given city and country
api_key = "YOUR_API_KEY_HERE"
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"

response = requests.get(api_url)

# Parse the JSON response
data = response.json()

# If you wish to add more information about the current weather conditions,
# you can print out the JSON response and check what keys are available by uncommenting this line:
# print(response.json())


if data["cod"] != "404":
    # Get the value of 'main' key and store it
    main = data['main']
    # Get temperature in kelvin and convert it to celsius
    temperature = round(main['temp'] - 273.15, 1)
    # Get the weather report
    report = data['weather']

    # Print the current weather
    print(
        f"The weather in {city}, {country} is currently {report[0]['description']} and the temperature is {temperature} degrees celsius.")
else:
    print("City not found.")
