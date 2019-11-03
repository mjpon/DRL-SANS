import requests
import csv


url = "https://api-v3.igdb.com/games"


def scrape(platform, offset, limit):

    payload = "fields name,platforms;\nwhere platforms = %d;\noffset %d;\nlimit %d;\n" % (platform, offset, limit)
    # print(payload)
    headers = {
        'user-key': "65870b1858a85d7e30df9a6d9c40fdd0",
        'cache-control': "no-cache",
        'Postman-Token': "b4537987-904d-42e7-9af6-1b230d933f9c"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    sol = (response.json())

    ids = []
    for item in sol:
        ids.append(item['id'])

    # print('ids in')
    # print(ids)
    return ids

    


if __name__ == '__main__':
    arr = []
    for i in range(0, 1000, 50):
        solution = scrape(20, i, 50)
        if solution:
            arr.append(solution)
            # print(solution)

    
    # print(len(arr))


    # # print(arr)
    resultFile = open("results_ds.csv",'w', newline='')
    wr = csv.writer(resultFile, delimiter=";")
    for items in arr:
        wr.writerows(map(lambda x: [x], items))
    resultFile.close()

    

