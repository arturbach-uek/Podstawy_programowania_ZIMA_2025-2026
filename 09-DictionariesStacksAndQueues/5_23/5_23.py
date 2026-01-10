import requests
import json

url = "https://api.nbp.pl/api/exchangerates/rates/C/EUR/last/10/?format=json"
response = requests.get(url)
data = response.json()

with open('euro.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("Date            Buying Rate     Selling Rate")
print("============================================")

for item in data['rates']:
    date = item['effectiveDate']
    bid = item.get('bid')
    ask = item.get('ask')
    print(f"{date}      {bid:.4f}          {ask:.4f}")
