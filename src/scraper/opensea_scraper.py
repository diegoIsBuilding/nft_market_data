import requests

url = "https://testnets-api.opensea.io/api/v2/collections/boredapeyachtclub/stats"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)