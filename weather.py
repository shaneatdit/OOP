##########################################################################
#                                                                        #
# weather.py                                                             #
#   by Shane                                                             #
#                                                                        #
# Prompts the user for the a zip code, then prints the current weather   #
# from the National Weather Service (http://forecast.weather.gov)        #
#                                                                        #
##########################################################################
import urllib.request

URL = "http://forecast.weather.gov/zipcity.php?inputstring="
WEATHER_TAG = '<p class="myforecast-current">'
FAHRENHEIT_TAG = '<p class="myforecast-current-lrg">'
CELSIUS_TAG = '<p class="myforecast-current-sm">'
CLOSING_TAG = '</p>'


def getpage(url):
    # Accesses the web page
    with urllib.request.urlopen(url) as f:
        return str(f.read())


def getinfo(page, opening_tag):
    # Finds the relevant info in page
    i = page.find(opening_tag, 0)
    if i == -1:
        return None
    j = page.find(CLOSING_TAG, i)
    return page[i + len(opening_tag):j]


def main():

    # Prompt user for zip code and Celsius/Fahrenheit
    print("")
    zip_code = input("Enter ZIP code: ")
    while True:
        units = input("Celsius or Fahrenheit? (C/F) ")
        if units.upper() == "C":
            temp_tag = CELSIUS_TAG
            temp_units = "degrees Celsius"
            break
        elif units.upper() == "F":
            temp_tag = FAHRENHEIT_TAG
            temp_units = "degrees Fahrenheit"
            break
    print("Connecting, please wait...")
    print("")

    # Retrieve info from website
    page = getpage(URL + zip_code)
    weather = getinfo(page, WEATHER_TAG)
    if weather is None:
        print("Unable to retrieve weather for", zip_code)
        print("Please check the zip code and try again")
        return
    temperature = getinfo(page, temp_tag)
    temperature = temperature.strip('&deg;C')
    temperature = temperature.strip('&deg;F')
    # temperature = getinfo(page, temp_tag, "&deg")

    # Print the weather
    print("Today's weather:", weather)
    print("Temperature:", temperature, temp_units)

main()
