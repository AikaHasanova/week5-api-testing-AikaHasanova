import requests

url = input("Enter the a link")

response = requests.get(url)

if response.status_code == 200:
    print("200 success")
else:
    print("404 not found")
