import requests
import csv

import shutil

# 

csv_path = "out.csv"

with open(csv_path, "r") as f_obj:
    reader = csv.reader(f_obj)
    print(20)
    for row in reader:
        print(type(row))


        ## first grab the ID
        url = "https://api-v3.igdb.com/covers"

        payload = "fields game, image_id, url;\nwhere game = "+str(row)+ ";"
        headers = {
            'user-key': "65870b1858a85d7e30df9a6d9c40fdd0",
            'Content-Type': "text/plain",
            'User-Agent': "PostmanRuntime/7.18.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ab797645-d125-4935-a2a9-48597867d049,7b1032ff-e721-41ad-b720-b7f624983d23",
            'Host': "api-v3.igdb.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "47",
            'Cookie': "__cfduid=dcbf933e31d8187fc52e3add96229c2821571093157",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers)



        print(response.json()[0].get('url'))
        print(type(response.json()))


        holdImageUrl = response.json()[0].get('url')
        shortfront = holdImageUrl[2:36]
        print(shortfront + 't_1080p' + holdImageUrl[43:])


        #### second to grab the image
        url = "https://"+ shortfront + 't_1080p' + holdImageUrl[43:]

        headers = {
            'User-Agent': "PostmanRuntime/7.18.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "3d9f3804-c6a9-4b36-93c0-cf748fa1662f,196f6365-3c0e-472e-b8a0-6557f23b6ea1",
            'Host': "images.igdb.com",
            'Accept-Encoding': "gzip, deflate",
            'Cookie': "__cfduid=dcbf933e31d8187fc52e3add96229c2821571093157",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, stream=True)


        # https://www.dev2qa.com/how-to-download-image-file-from-url-use-python-requests-or-wget-module/ 
        # print(response.text)


        # This is the image url.
        # image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
        # Open the url image, set stream to True, this will return the stream content.
        # resp = requests.get(image_url, stream=True)
        # Open a local file with wb ( write binary ) permission.
        local_file = open(row+'.jpg', 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        response.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(response.raw, local_file)
        # Remove the image url response object.
        del response
# if __name__ == "__main__":
#     csv_path = "out.csv"