# 'requests' is a popular python library used to send HTTP requests
import requests

# The URL is the API endpoint we are using from this site: https://sv443.net/jokeapi/v2/
# You can configure the endpoint to use different categories of jokes
# In this example we are using the 'Any' category. BEWARE OF NSFW JOKES!
url = "https://v2.jokeapi.dev/joke/Any"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)

# Store the response in a JSON format
data = response.json()
# Store the "Joke" text from the returned JSON dictionary
joke = data.get("joke")

# Print the category of the joke to the console
print("The following Joke Category is: " + data.get("category"))

# If a joke was retrieved, Print it. Else, Print "Nothing was returned"
if joke is not None:
    print(data.get("joke"))
else: 
    print("Nothing was returned")

# DISCLAIMER: THE JOKES RETURNED FROM THIS SCRIPT DO NOT BELONG TO THE DEV, J0S!
# SOMETIMES THIS SCRIPT PRINTS NSFW JOKES. SORRY. YOU'VE BEEN WARNED!