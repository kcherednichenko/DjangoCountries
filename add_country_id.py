import json

new_countries = {
    "countries": []
}

with open('country-by-languages.json', 'r') as countries:
    data = json.load(countries)
    cnt = 1
    for country in data['countries']:
        new_country = country.copy()
        new_country['id'] = cnt
        new_countries["countries"].append(new_country)
        cnt += 1

with open('country-by-languages2.json', 'w') as new_json_file:
    new_countries_json = json.dumps(new_countries)
    new_json_file.write(new_countries_json)
