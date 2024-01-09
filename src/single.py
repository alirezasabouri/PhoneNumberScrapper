
# Replace 'url' with the actual endpoint URL
url = 'https://my.persiansaze.com/rest/api/user/v1/Project/Filter'


offset = 0
limit = 20
results = []
headers = {
    "authority": "my.persiansaze.com",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3MDQwOTkzRDU4NkRENjFCNjVDOEYwNTM5RTBEQzU2RjIyNDZGQ0UiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiIxMjk0IiwidXNyIjoiMTI5NCIsImFjYyI6IjExMjciLCJyb2xlIjoiMSIsIm5hbWUiOiLYotmC2KfbjCDYqNmC2KfbjNuMIiwiYWNjZXNzIjoiIiwibmJmIjoxNjg4MjUyODk5LCJleHAiOjE2ODgyNTY0OTksImlhdCI6MTY4ODI1Mjg5OSwiaXNzIjoiUFMuSWRlbnRpdHkiLCJhdWQiOiJQU0MifQ.zdLOFmw_RwwdhtRac0wyQY0ZPX2kFMAEcB-AqabOLLCcr5z37uwMImh_BfQuRrtXZVgabZNKTwyllEZPT5FrEBz-pFTVX6Qg6eKoMMMFeplgXSNmHzPlGPvXGhl1PgYawemB-nUQvvUznXj21XncxB9x2vEJT5PHpltcP29edOMtKHfm2EAcBnb57-XJGyI2m24dM7zi9S7fYlYbx8RmCJggN9cRksGDSLBR9eLBM1XxKck0tdj6j83TVg8DhpPFDCnXMCgD8sBbDaup7za42RYBDsraTecyTH45GrivmeEWhUXwGCF-k3lG_6BggjfxVy-F3VTHUzC48jsCw2o5nA",
    "origin": "https://my.persiansaze.com",
    "referer": "https://my.persiansaze.com/",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
}
body = {
    "type": "New",
    "onlyWithConstructor": True,
    "cityIds": [],
    "regionIds": [],
    "subRegionIds": [],
    "phaseIds": [],
    "folderIds": [],
    "usageTypes": [],
    "usageTypesIds": [],
    "structureTypeIds": [],
    "targetAccessId":"3046"
}
response = requests.post(f"{url}?limit={limit}&offset={offset}", headers = headers, json=body)
data = response.json()

print(data)