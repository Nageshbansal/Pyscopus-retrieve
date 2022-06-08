from os import getenv

import requests
import json
import pandas as pd

base_url = "https://api.elsevier.com/content/search/scopus"

apiKey = getenv("apiKey")

headers = {
        'X-ELS-APIKey' : '45c6063a93408d8c4f3925dcf8e02e01',
        'Accept' : 'application/json'
}

title = []
url = []

response = requests.get('https://api.elsevier.com/content/search/scopus?query=TITLE-ABS-KEY("thermal adaptation") AND ( LIMIT-TO ( SUBJAREA,"ENGI" ) OR LIMIT-TO ( SUBJAREA,"COMP" ) OR LIMIT-TO ( SUBJAREA,"SOCI" ) OR LIMIT-TO ( SUBJAREA,"PSYC" ) )&count=200',headers=headers)
response_json = response.json()

with open('reponse.json','w') as f :
        json.dump(response_json,fp=f,indent=4)



for i in range(0,200):
      print(response_json['search-results']['entry'][i]['dc:title'])
      title.append(response_json['search-results']['entry'][i]['dc:title'])
      url.append(response_json['search-results']['entry'][i]['prism:url'])


df = pd.DataFrame({'title':title,'url':url})
df.to_csv('papers_info')