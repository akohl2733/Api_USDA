import requests

# url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1'
url = 'https://api.nal.usda.gov/fdc/v1/foods/list'

headers = {
    'Accepts': 'application/json',
    'X-api-key': 'HgqycftTlROw8txzFIKamDRZTPLsugezIphFQu1g'
}

r = requests.get(url, headers=headers)
result = r.json()
for x in result:
    print(x['description'])
    for i in x['foodNutrients']:
        print(str(i['name']) + ' -- ' + str(i['amount']) + ' ' + str(i['unitName']))
    print()
    print()