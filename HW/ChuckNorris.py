import json
import requests

resp =requests.get('http://api.icndb.com/jokes/random')

joke = json.loads(resp.text)

print(joke["value"]["joke"])