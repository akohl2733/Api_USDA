import requests

# url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1'
url = 'https://api.nal.usda.gov/fdc/v1/foods/search?'

headers = {
    'Accepts': 'application/json',
    'X-api-key': 'HgqycftTlROw8txzFIKamDRZTPLsugezIphFQu1g'
}
api = 'HgqycftTlROw8txzFIKamDRZTPLsugezIphFQu1g'

foodname = input('What food are you looking for?\n')

r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(api, foodname))
result = r.json()

def ans():
    print(str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName']))

for x in result['foods']:
    print(x['description'])
    for i in x['foodNutrients']:
        name = i['nutrientName']
        if name == 'Energy' and i['unitName'] == 'KCAL':
            ans()
        elif name == 'Carbohydrate, by difference':
            ans()
        elif name == 'Protein':
            ans()
        elif name == 'Total lipid (fat)':
            ans()
    print()
