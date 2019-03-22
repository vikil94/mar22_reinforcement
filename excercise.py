import requests
import json

res = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)

bahamas_url = body[20]["legislatures"][0]["popolo_url"]

res_baha = requests.get(bahamas_url)
body_baha = json.loads(res_baha.content)

polo_1 = body_baha['persons'][0]['name']

print(polo_1)