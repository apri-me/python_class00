my_dict = {
    'name': 'alireza',
    'last name': 'afroozi',
    'face': {
        'hair color': 'Brown',
        'eye color': 'Blue'
    } ,
    'friends': ['sina', 'vahid', 'amir', 'erfan'] ,
}

for key, val  in  my_dict.items():
    print(f'key {key} is {val}')

for key in my_dict.keys():
    print(f'key {key} is {my_dict[key]}')