import json

# f = open('fruit.json', 'r')
# print(f.read())
# f.close()

with open('fruit.json', 'r') as f:
    data = json.load(f)

# print(data)

data['Fruit'][1]['Name'] = 'Guava'

print(data)

data['Fruit'].append({'Name': 'Strawberry', 'Color': 'Red'})

with open('fruit.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('fruit.json', 'r') as f:
    print(f.read())
