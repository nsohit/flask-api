import requests
import json
url = 'http://localhost:5005/api'
r=request.get(url)
data=r.json()
print(data)

