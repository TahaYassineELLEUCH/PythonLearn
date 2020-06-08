import requests

API_KEY = "Th2wTXr2bXDqGzetljQI1HlOGS3hajCU"
BASE_URL = "https://api.nytimes.com/svc/archive/v1/2015/2.json?limit=20&api-key={}"
URL = str.format(BASE_URL, API_KEY)
response = requests.get(URL)
tab = response.content.split()
print(URL)
print(response.headers)

