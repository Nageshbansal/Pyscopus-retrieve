import json
import requests

base_url = "https://api.elsevier.com/content/search/sciencedirect"

headers = {
        'X-ELS-APIKey' : '45c6063a93408d8c4f3925dcf8e02e01',
        'Accept' : 'application/json'
}

data = {
        'qs': ' "thermal adaptation" ',
       'offset': 0
       } 

Url = "https://api.elsevier.com/content/search/sciencedirect"

r = requests.put(Url, data =json.dumps(data), headers=headers)

with open('science_put.json','w') as f: 
    json.dump(r.json(),indent=4,fp=f)