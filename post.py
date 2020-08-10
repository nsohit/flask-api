import requests
import json
DATA = { 'nama' :"dede", 'umur' :"22"}
url ='http://localhost:5005/api'
headers = { 'Content-Type': 'application/json' }
requests.post(url,DATA)

