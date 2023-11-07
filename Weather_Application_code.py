import requests
import json
import time
import sys

# Make a request to the weather API for the current weather data for a given city.
API_KEY = "49d519d91d174024a21112322230809"


def get_weather_data(city):
    url = "https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(API_KEY, city)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        # return data

    else:
        raise Exception("API request failed")
    print(f"Name of  City  : {data['location']['name']}")
    print(f"Country of the City : {data['location']['country']}")
    print(f"Temperature in  Celcius : {data['current']['temp_c']}")
    print(f"Temperature in  Fahrenheit : {data['current']['temp_f']}")
    print(f"Weather Condtion is {data['current']['condition']['text']}")


city_list = []


def valid_city(name):
    if name.isalpha():
        return True
    else:
        return False


def favourite_city():
    print("enter favourite city names")
    city_name = input().strip().split()
    for j in city_name:
        if j in city_list:
            print(f"{city_name} is already in your favourite list")
        else:
            if valid_city(j):
                city_list.append(j.capitalize())
            else:
                print(f"{j} must Alphabets only")
    print(f"*****  successfully added to favorite cities *****")


def fav_list():
    print(city_list)


def remove_city():
    print("enter removing city name")
    city_name = input()
    city_name = city_name.capitalize()
    if city_name not in city_list:
        print(f"{city_name} is not in your favourite list")
    else:
        city_index = city_list.index(city_name)
        city_list.remove(city_name)
        print(f"{city_name} removed succefully")


def update_city():
    print("enter old city name")
    city = input()
    if valid_city(city):
        city = city.capitalize()
    else:
        print("Enter only Alphabets")
    print("New data")
    new_data = input()
    if valid_city(new_data):
        new_data = new_data.capitalize()
    old_city_index = city_list.index(city)
    city_list[old_city_index] = new_data
    print(f"City name updated Successfully")


print("Welcome to Weather checking application")
net = 0
while True:
    if net > 0:
        print("******************************************")
    print("What do you want")
    print("press 1 for Weather Checking")
    print("press 2 for Adding your Favourite City")
    print("press 3 for Removing city from Favourite City")
    print("print 4 for Updating Favourite list")
    print("print 5 for Seeing Favourite list")
    print("6 for exit")
    print("Enter Your choice")
    input_no = int(input())
    if input_no == 1:
        print("Enter city name")
        city = input()
        get_weather_data(city)
    elif input_no == 2:
        favourite_city()
    elif input_no == 3:
        remove_city()
    elif input_no == 4:
        update_city()
    elif input_no == 5:
        fav_list()
    else:
        print("Thanks for using this application")
        sys.exit(0)
    net += 1
    time.sleep(3)
