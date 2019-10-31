# 	WOwlDlrs6RG8DN9jLtrw1g== this is the API key

import http.client

conn = http.client.HTTPConnection("WWW.api-v3.igdb.com")

payload = "fields name,category,platforms,screenshots.*;\nwhere category = 0 & platforms = 48;\n"

headers = {
    'user-key': "65870b1858a85d7e30df9a6d9c40fdd0",
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.18.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f9e5d2de-bca5-4fbc-af5b-be5612e33c1a,c7f07107-6333-40e8-9c82-68da791166ad",
    'Host': "api-v3.igdb.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "83",
    'Cookie': "__cfduid=dcbf933e31d8187fc52e3add96229c2821571093157",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("GET", "games", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))