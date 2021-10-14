from decouple import config
import requests

response = requests.get(config("OMDB_API_KEY"))
print(response.status_code)
print(response.content)
