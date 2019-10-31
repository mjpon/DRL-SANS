import requests
import csv 


def cover():
    url = "https://api-v3.igdb.com/covers"

    payload = "fields game, image_id, url;\nwhere game = 1199;"
    headers = {
        'user-key': "65870b1858a85d7e30df9a6d9c40fdd0",
        'Content-Type': "text/plain",
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "7f8e469f-502a-4e15-96c4-93abdbe85f4d,2c19c043-4a9d-47e1-a04a-aabdbf33a8dc",
        'Host': "api-v3.igdb.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "46",
        'Cookie': "__cfduid=d2247e241c9db5ccd0582909b012a3df21571094093",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)

if __name__ == '__main__':
    results = open('results.csv' 'r')
    
    cover()