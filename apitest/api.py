import requests


def focus():
 response = requests.get("http://35.225.243.133/bloggers/")
 response_json = response.json()
 print(response_json)

 full_name={ "full_name": "Idris Shabanli"}

 request=requests.post("http://35.225.243.133/bloggers/",full_name)
 print(request.json())

print(focus())