import requests


r = requests.get("https://surabhitea.in//")
print(r.status_code)
print(r.ok)
