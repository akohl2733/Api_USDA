from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = 'myCalorieTracker'



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        food = request.form['food']
        session['foods'] = food
        foodname = session['foods']
        api = 'HgqycftTlROw8txzFIKamDRZTPLsugezIphFQu1g'
        r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(api, foodname))
        result = r.json()

        options = {}

        for x in result['foods']:
            temp = []
            ider = x['description']
            for i in x['foodNutrients']:
                name = i['nutrientName']
                if name == 'Energy' and i['unitName'] == 'KCAL':
                    cal = 'Calories -- ' + str(i['value']) + ' ' + str(i['unitName'])
                    temp.append(cal)
                elif name == 'Carbohydrate, by difference':
                    carb = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
                    temp.append(carb)
                elif name == 'Protein':
                    protein = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
                    temp.append(protein)
                elif name == 'Total lipid (fat)':
                    fat = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
                    temp.append(fat)
            options[ider] = temp
        return render_template('options.html', options=options)
    else:
        return render_template('foodSelect.html')
            
@app.route('/analyze', methods=['POST', "GET"])
def analyze():
    decision = request.form.get('comp_select')
    api = 'HgqycftTlROw8txzFIKamDRZTPLsugezIphFQu1g'
    r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(api, decision))
    result = r.json()

    for x in result['foods']:
        if x['description'] == str(decision):
            for i in x['foodNutrients']:
                name = i['nutrientName']
                if name == 'Energy' and i['unitName'] == 'KCAL':
                    cal = 'Calories -- ' + str(i['value']) + ' ' + str(i['unitName'])
                elif name == 'Carbohydrate, by difference':
                    carb = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
                elif name == 'Protein':
                    protein = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
                elif name == 'Total lipid (fat)':
                    fat = str(i['nutrientName']) + ' -- ' + str(i['value']) + ' ' + str(i['unitName'])
    return(f'{decision} -- {cal} -- {carb} -- {fat} -- {protein}')

        

if __name__ == '__main__':
    app.run(debug=True)