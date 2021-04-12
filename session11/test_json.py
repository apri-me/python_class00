import json

# f = open('js.json')
# d = json.load(f)
# f.close()

with open('js.json') as f:
    d = json.load(f)


print (d['topping'][3]['id'])
