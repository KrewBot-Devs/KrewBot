

import json

# Data to be written
dictionary ={
'Brazil':{
        'Rum' : '60',
        'Coffee': '26',
        'Spice': '25',
        'Silk': '150'
        },
'Guinea': {
        'Rum' : '38',
        'Coffee': '22',
        'Spice': '22',
        'Silk': '310'
        },
'Labrador': {
        'Rum'  : '48',
        'Coffee': '40',
        'Spice': '14',
        'Silk': '230'
        },
'Spain': {
        'Rum' : '60',
        'Coffee': '26',
        'Spice': '53',
        'Silk': '180'
        },
'Brazil': {
        'Rum' : '32',
        'Coffee': '70',
        'Spice': '40',
        'Silk': '240'
        }

}

# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)
