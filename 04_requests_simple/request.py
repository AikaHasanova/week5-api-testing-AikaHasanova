import requests

response = requests.get("http://www.omdbapi.com/?t=the blade &apikey=35b13908")
response_json= response.json()
print(response_json)