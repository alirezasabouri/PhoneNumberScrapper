$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("_gid", "GA1.2.607347849.1688249103", "/", ".persiansaze.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("_ga_1NYMKCTZB4", "GS1.1.1688249102.1.1.1688252898.60.0.0", "/", ".persiansaze.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("_ga", "GA1.2.969530264.1688249102", "/", ".persiansaze.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("_gat_UA-161921713-1", "1", "/", ".persiansaze.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://my.persiansaze.com/rest/api/user/v1/Project/Filter?limit=20&offset=0" `
-Method "POST" `
-Headers @{
"authority"="my.persiansaze.com"
  "method"="POST"
  "path"="/rest/api/user/v1/Project/Filter?limit=20&offset=0"
  "scheme"="https"
  "accept"="application/json"
  "accept-encoding"="gzip, deflate, br"
  "accept-language"="en-US,en;q=0.9,fa;q=0.8"
  "authorization"="Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3MDQwOTkzRDU4NkRENjFCNjVDOEYwNTM5RTBEQzU2RjIyNDZGQ0UiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiIxMjk0IiwidXNyIjoiMTI5NCIsImFjYyI6IjExMjciLCJyb2xlIjoiMSIsIm5hbWUiOiLYotmC2KfbjCDYqNmC2KfbjNuMIiwiYWNjZXNzIjoiIiwibmJmIjoxNjg4MjUyODk5LCJleHAiOjE2ODgyNTY0OTksImlhdCI6MTY4ODI1Mjg5OSwiaXNzIjoiUFMuSWRlbnRpdHkiLCJhdWQiOiJQU0MifQ.zdLOFmw_RwwdhtRac0wyQY0ZPX2kFMAEcB-AqabOLLCcr5z37uwMImh_BfQuRrtXZVgabZNKTwyllEZPT5FrEBz-pFTVX6Qg6eKoMMMFeplgXSNmHzPlGPvXGhl1PgYawemB-nUQvvUznXj21XncxB9x2vEJT5PHpltcP29edOMtKHfm2EAcBnb57-XJGyI2m24dM7zi9S7fYlYbx8RmCJggN9cRksGDSLBR9eLBM1XxKck0tdj6j83TVg8DhpPFDCnXMCgD8sBbDaup7za42RYBDsraTecyTH45GrivmeEWhUXwGCF-k3lG_6BggjfxVy-F3VTHUzC48jsCw2o5nA"
  "origin"="https://my.persiansaze.com"
  "referer"="https://my.persiansaze.com/"
  "sec-ch-ua"="`"Not.A/Brand`";v=`"8`", `"Chromium`";v=`"114`", `"Google Chrome`";v=`"114`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
  "sec-fetch-dest"="empty"
  "sec-fetch-mode"="cors"
  "sec-fetch-site"="same-origin"
} `
-ContentType "application/json" `
-Body "{`"type`":`"New`",`"onlyWithConstructor`":true,`"cityIds`":[],`"regionIds`":[],`"subRegionIds`":[],`"phaseIds`":[],`"folderIds`":[],`"usageTypesIds`":[],`"structureTypeIds`":[],`"targetAccessId`":3046}"