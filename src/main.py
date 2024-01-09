import json
from threading import Thread
import threading
import time
import requests
import xlsxwriter

TARGET_ACCESS_ID="24845"
AUTHORIZATION_KEY = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3MDQwOTkzRDU4NkRENjFCNjVDOEYwNTM5RTBEQzU2RjIyNDZGQ0UiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiIxNzY5OCIsInVzciI6IjE3Njk4IiwiYWNjIjoiMTU2MzkiLCJyb2xlIjoiMiIsIm5hbWUiOiLYtdio2YjYsduMIiwiYWNjZXNzIjoiQ1RSLFNNUyxTQUwsQ1JTIiwibmJmIjoxNzA0ODAwNTkyLCJleHAiOjE3MDQ4MDQxOTIsImlhdCI6MTcwNDgwMDU5MiwiaXNzIjoiUFMuSWRlbnRpdHkiLCJhdWQiOiJQU0MifQ.uwJhhe0tdkRfpUONB0U6V_XViNfOFlFcySC8Nvgkz2tQ-C7OJ9zW4RG0JFuHvAE7SpNEmPi88ojkXk2Cm7s62tXKNRIAl7jP2xLZ2xoyooDk2etv8ltEjsaip2zmhaR2kZGoOp43zQv-QnG7QUXFqeIGukD_KDEYSKemyqLACvFesEGQ38kIXphqSe9yeOBH7kXTTz9yPqhHs4uIOaJNGMDOrx84C6uU2tN0TfWybrSriFs_bdAtvJ-RghtROOFn_Sdi3rOHNVeEH9AJWR-Bj9Pow8fRLLHqs-ribwhIK2f7t8Wk2OmOUZvWMJoL1xtp-xQV__VPfdYIt-FiL4BfCA"
REQUEST_HEADERS = {
        "authority": "my.persiansaze.com",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,fa;q=0.8",
        "authorization": AUTHORIZATION_KEY,
        "origin": "https://my.persiansaze.com",
        "referer": "https://my.persiansaze.com/",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
DEFAULT_PAYLOAD = {
        "type": "All",
        "onlyWithConstructor": True,
        "cityIds": [],
        "regionIds": [],
        "subRegionIds": [],
        "phaseIds": [],
        "folderIds": [],
        "usageTypes": [],
        "usageTypesIds": [],
        "structureTypeIds": [],
        "targetAccessId":TARGET_ACCESS_ID
}
DEFAULT_DATA_FILE = "dump.json"

def getEntriesCount():
    url = 'https://my.persiansaze.com/rest/api/user/v1/Project/Filter'
    body = DEFAULT_PAYLOAD
    response = requests.post(f"{url}?limit=0&offset=0", headers = REQUEST_HEADERS, json=body)
    if (response.status_code != 200):
        raise Exception(f"HTTP call to {url} failed with error status code {response.status_code}")
    
    data = response.json()

    return data["count"]
    
def getEntryDetails(hashId):
    constructorUrl = f"https://my.persiansaze.com/rest/api/user/v1/Project/{hashId}/Constructor"
    body = {}
    
    response = requests.post(constructorUrl, headers = REQUEST_HEADERS, json=body)
    if (response.status_code != 200):
        raise Exception(f"HTTP call to {constructorUrl} failed with error status code {response.status_code}")
    
    return response.json()

    
def fetchEntries(offset, limit, resultset, resultsetLock):

    print (f"running fetchEntries for {offset} to {offset + limit}")

    url = 'https://my.persiansaze.com/rest/api/user/v1/Project/Filter'
    body = DEFAULT_PAYLOAD
    response = requests.post(f"{url}?limit={limit}&offset={offset}", headers = REQUEST_HEADERS, json=body)
    data = response.json()

    for result in data['results']:
        hashId = result['hashId']
        regionId = result['regionId']
        subRegionId = result['subRegionId']
        groundArea = result['groundArea']
        lastUpdateDate = result['lastUpdateDate']
        units = result['units']
        floors = result['floors']
        cityId = result['cityId']
        residentialArea = result['residentialArea']
        structureTypeId = result['structureTypeId']

        # constructor = getEntryDetails(hashId)

        result = {
                "hashId": hashId,
                "cityId": cityId,
                "subRegionId": subRegionId,
                "groundArea": groundArea,
                "residentialArea": residentialArea,
                "units": units,
                "floors": floors,
                "structureTypeId": structureTypeId,
                "lastUpdateDate": lastUpdateDate
            }
        
        resultsetLock.acquire()
        if (not regionId in resultset):
            resultset[regionId] = []
        resultset[regionId].append(result)
        resultsetLock.release()

def exportToJsonFile(data, outputFile):
    json_object = json.dumps(data, indent=4)
 
    with open(outputFile, "w") as outfile:
        outfile.write(json_object)

def rebuildDataFile():
    offset = 0
    limit = 20
    threadPoolSize = 3
    totalCount = getEntriesCount()
    
    totalBatches = totalCount / limit
    batchesInProcess = 0    
    results = {}
    resultsetLock = threading.Lock()
    activeThreads = []

    start_time = time.time()

    while batchesInProcess < totalBatches:
        for x in range(threadPoolSize):
            t = Thread(target=fetchEntries, args=[offset, limit, results, resultsetLock])
            offset += limit
            t.start()
            batchesInProcess += 1
            activeThreads.append(t)
            if (batchesInProcess == totalBatches):
                break
        
        for t in activeThreads:
            t.join()
            
        print ("waiting for next iteration...")


    print("all batches completed")
    print(f"{len(results)} entries fetched in total, {time.time() - start_time} seconds elpased")
    
    outputFilename = DEFAULT_DATA_FILE
    print (f"writing output to file {outputFilename}...")
    exportToJsonFile(results, outputFilename)


def fetchAndSaveDetails(regionId):
    dataFilename = DEFAULT_DATA_FILE
    print (f"reading data file {dataFilename}...")

    f = open(dataFilename)
    data = json.load(f)
    f.close()

    entries = data[regionId]
    entriesCount = len(entries)
    i = 0
    for entry in entries:
        i+=1
        print(f"Fetching details... {i}/{entriesCount}", end="\r" if i < entriesCount else "\n")    
        constructorDetails = getEntryDetails(entry["hashId"])
        entry["constructor"] = {
            "address": constructorDetails.get("address"),
            "name": constructorDetails["constructor"].get('name')  if constructorDetails.get('constructor') != None else  "NULL",
            "mobileNumbers": constructorDetails["constructor"].get('mobileNumbers')  if constructorDetails.get('constructor') != None else  "NULL"
        }
        time.sleep(.5)

    print(f"All entries loaded, start updating data file {dataFilename}")
    exportToJsonFile(data, DEFAULT_DATA_FILE)




def exportToExcel(regionId):
    dataFilename = DEFAULT_DATA_FILE
    print (f"reading data file {dataFilename}...")

    f = open(dataFilename)
    data = json.load(f)
    f.close()

    entries = data[regionId]

    excelOutFileName = "numbers_" + regionId + ".xlsx"
    workbook = xlsxwriter.Workbook(excelOutFileName)
    worksheet = workbook.add_worksheet("Sheet1")
    
    row = 0
    for item in (entries):
        if (item["constructor"]["mobileNumbers"] == "NULL"):
            continue
        worksheet.write(row, 0, item["constructor"]["name"])
        phoneNumbers = item["constructor"]["mobileNumbers"]
        phoneNumberIndex = 0
        for phone in phoneNumbers:
            phone = phone[1:] if phone[0]=="0" else phone
            worksheet.write(row, 1 + phoneNumberIndex , phone)
            phoneNumberIndex+=1
        row += 1
    
    workbook.close()

    print(f"Exported to excel file {excelOutFileName}")

def main():

    # rebuildDataFile()

    fetchAndSaveDetails("105")
    exportToExcel("105")

    # for x in range(101,123):
    #    fetchAndSaveDetails(str(x))
    #    exportToExcel(str(x))

    # print(f"Finished all operations")


# Usage instruction:

    # rebuildDataFile()     # use only once to create the base file
    # fetchAndSaveDetails("120")
    # exportToExcel("120")

main()



