# ============================================
# UNDERSTANDING APIs - SIMPLE WEATHER EXAMPLE
# ============================================
# API = Application Programming Interface
# Think of it like ordering food at a restaurant:
# - You (your code) ask the waiter (API) for food
# - The waiter takes your order to the kitchen (server)
# - The kitchen prepares it and gives it back to the waiter
# - The waiter brings you your food (data)

# We'll use the requests library to talk to APIs
# requests is like a messenger that sends and receives data from websites
import requests

print("=" * 60)
print("WHAT IS AN API?")
print("=" * 60)
print()
print("API = A way for programs to talk to each other")
print("We send a REQUEST, and get back a RESPONSE")
print()
print("Today we'll get weather data from wttr.in")
print("wttr.in is a FREE weather service - no signup needed!")
print()

# ============================================
# EXAMPLE 1: SIMPLEST API CALL
# ============================================
# Let's get weather for a city
# We just need to ask the API nicely with a URL

print("=" * 60)
print("EXAMPLE 1: Get Weather for Seattle")
print("=" * 60)
print()

# Step 1: Build the URL (the address where we ask for data)
# Format: http://wttr.in/CITYNAME?format=j1
# - wttr.in is the weather service
# - Seattle is the city we want
# - ?format=j1 means "give me JSON data" (JSON = organized data format)
city = "New York"
url = f"http://wttr.in/{city}?format=j1"

print(f"Step 1: We built the URL: {url}")
print()

# Step 2: Send the request (ask for the data)
# requests.get() sends a GET request (GET = "please give me data")
print("Step 2: Sending request to the weather service...")
response = requests.get(url)

print(f"Step 3: Got response! Status code: {response.status_code}")
# Status code 200 = Success! (like getting a thumbs up)
# Status code 404 = Not found (like "sorry, we don't have that")
print()

# Step 3: Get the data from the response
# .json() converts the response into a Python dictionary
weather_data = response.json()

print("Step 4: We got the data! It's a dictionary with weather info")
print()

# Step 4: Extract useful information
# The data is nested (dictionaries inside dictionaries)
current = weather_data["current_condition"][0]  # Current weather is in a list

# Pull out specific pieces of information
temperature = current["temp_F"]  # Temperature in Fahrenheit
feels_like = current["FeelsLikeF"]  # What it feels like
description = current["weatherDesc"][0]["value"]  # Weather description
humidity = current["humidity"]  # Humidity percentage

# Display the results
print(f"Weather in {city}:")
print(f"  Temperature: {temperature}°F")
print(f"  Feels like: {feels_like}°F")
print(f"  Conditions: {description}")
print(f"  Humidity: {humidity}%")
print()

# ============================================
# EXAMPLE 2: GET WEATHER FOR MULTIPLE CITIES
# ============================================
# Now let's use a loop to get weather for several cities

print("=" * 60)
print("EXAMPLE 2: Weather for Multiple Cities")
print("=" * 60)
print()

# List of cities we want weather for
cities = ["Portland", "Denver", "Austin", "Boston"]

# Loop through each city
for city in cities:
    # Build the URL for this city
    url = f"http://wttr.in/{city}?format=j1"
    
    # Send the request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Get the data
        data = response.json()
        current = data["current_condition"][0]
        
        # Extract temperature and description
        temp = current["temp_F"]
        desc = current["weatherDesc"][0]["value"]
        
        # Print results
        print(f"{city}: {temp}°F - {desc}")
    else:
        print(f"{city}: Could not get weather (error {response.status_code})")

print()

# ============================================
# EXAMPLE 3: ERROR HANDLING
# ============================================
# What if something goes wrong? Let's handle errors properly

print("=" * 60)
print("EXAMPLE 3: Handling Errors")
print("=" * 60)
print()

# Try to get weather for a city (might have typo or connection issues)
city = "InvalidCityName12345"
url = f"http://wttr.in/{city}?format=j1"

print(f"Trying to get weather for: {city}")

# try/except catches errors so our program doesn't crash
try:
    response = requests.get(url, timeout=5)  # timeout = give up after 5 seconds
    
    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        temp = current["temp_F"]
        print(f"Temperature: {temp}°F")
    else:
        print(f"Error: Got status code {response.status_code}")
        
except requests.exceptions.Timeout:
    print("Error: Request took too long (timeout)")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the weather service")
except Exception as e:
    print(f"Error: Something went wrong - {e}")

print()

# ============================================
# EXAMPLE 4: INTERACTIVE WEATHER CHECKER
# ============================================
# Let's make it interactive - user can type a city name

print("=" * 60)
print("EXAMPLE 4: Interactive Weather Checker")
print("=" * 60)
print()

# Ask user for a city
user_city = input("Enter a city name (or press Enter for New York): ")

# If they didn't type anything, use New York as default
if user_city == "":
    user_city = "New York"

print(f"\nGetting weather for {user_city}...")

# Build URL and make request
url = f"http://wttr.in/{user_city}?format=j1"

try:
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        
        # Get more detailed information
        temp_f = current["temp_F"]
        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeF"]
        description = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        wind_speed = current["windspeedMiles"]
        
        # Display nicely formatted results
        print()
        print(f"Current Weather in {user_city}:")
        print("-" * 40)
        print(f"  Conditions:    {description}")
        print(f"  Temperature:   {temp_f}°F ({temp_c}°C)")
        print(f"  Feels Like:    {feels_like}°F")
        print(f"  Humidity:      {humidity}%")
        print(f"  Wind Speed:    {wind_speed} mph")
        print()
    else:
        print(f"Could not find weather for '{user_city}'")
        
except Exception as e:
    print(f"Error getting weather: {e}")

# ============================================
# SUMMARY: HOW APIs WORK
# ============================================
print()
print("=" * 60)
print("SUMMARY: HOW APIs WORK")
print("=" * 60)
print()
print("1. BUILD URL: Create the address where data lives")
print("   Example: http://wttr.in/Seattle?format=j1")
print()
print("2. SEND REQUEST: Use requests.get(url) to ask for data")
print("   This is like clicking a link in your browser")
print()
print("3. CHECK STATUS: response.status_code tells if it worked")
print("   200 = Success, 404 = Not found, 500 = Server error")
print()
print("4. GET DATA: response.json() converts data to dictionary")
print("   Now you can access it like: data['key']['subkey']")
print()
print("5. USE DATA: Extract what you need and display it")
print()
print("APIs let your programs get data from anywhere in the world!")
print("Weather, stocks, news, maps, social media - all use APIs!")
print()
