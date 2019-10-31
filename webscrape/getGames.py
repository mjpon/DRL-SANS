import requests
import csv

url = "https://api-v3.igdb.com/games"

payload = "fields name,platforms;\nwhere platforms = 48;\noffset 49;\nlimit 50;\n"
headers = {
    'user-key': "65870b1858a85d7e30df9a6d9c40fdd0",
    'cache-control': "no-cache",
    'Postman-Token': "b4537987-904d-42e7-9af6-1b230d933f9c"
    }

response = requests.request("GET", url, data=payload, headers=headers)
sol = (response.json()[0]['id'])

print(sol)