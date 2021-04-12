import requests # pip install requests

response = requests.get("https://www.google.com/")

print(response.text)