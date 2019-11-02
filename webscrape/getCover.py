import requests
import csv 
import shutil





def cover(gameID):
    url = "https://api-v3.igdb.com/covers"

    payload = "fields game, image_id, url;\nwhere game = %d;\n" % (int(gameID))
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
    
    res = response.json()


    
    if res:
        image_id = res[0]['image_id']
        print('got id: ' + str(image_id))

        url = 'http://images.igdb.com/igdb/image/upload/t_1080p/' + image_id + '.jpg'
        print('getting response for: ' + str(image_id))
        resp = requests.get(url, stream=True)
        local_file = open('./images_gameboyColor/' + image_id + '.jpg', 'wb')
        resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)
        # Remove the image url response object.
        del resp
    else:
        print('no cover for: ' + gameID)


if __name__ == '__main__':
    gameID = []
    with open('results_gameboyColor.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            gameID.append(row[0])
    csvFile.close()

    print(len(gameID))

    for game in gameID:
        cover(game)
    
    # cover()