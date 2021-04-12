import json

player = {
    'name': 'ronaldo',
    'age': 35,
    'team': 'Juventus'
}


f = open("newfile.json", 'w')
json.dump(player, f)
f.close()