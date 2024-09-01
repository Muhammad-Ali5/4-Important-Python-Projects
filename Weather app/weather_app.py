import requests  # Import the requests library to make HTTP requests
import json  # Import the json library to work with JSON data
import pyttsx3  # Import the pyttsx3 library for text-to-speech functionality

API_KEY = "70f28f815f3544b2a44192647242308"  # API key for accessing the weather API
city = input("Enter the city name:\t")  # Prompt the user to enter the name of the city
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"  # Construct the URL with the API key and city name

r = requests.get(url)  # Make a GET request to the weather API
w_dict = json.loads(r.text)  # Parse the JSON response and convert it into a dictionary

# Try to access and print specific weather details from the dictionary
try:
    pressure_in = w_dict["current"]["pressure_in"]  # Get the atmospheric pressure in inches
    cloud_cover = w_dict["current"]["cloud"]  # Get the cloud cover percentage
    temp_c = w_dict["current"]["temp_c"]  # Get the temperature in Celsius

    print(f"Pressure (in): {pressure_in}")  
    print(f"Cloud cover (%): {cloud_cover}")
    print(f"Temperature (C): {temp_c}")  

    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(f"The current weather in {city} is: Pressure: {pressure_in} inches, Cloud cover: {cloud_cover}%, and Temperature: {temp_c} degrees Celsius.")
    engine.runAndWait()  # Run the text-to-speech engine to speak the message
except KeyError as e:
    # Handle the error if a weather detail is missing in the response
    print(f"KeyError: {e} not found in the response")
