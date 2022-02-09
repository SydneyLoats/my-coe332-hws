import random
import json

def generate_latitude():
    ret = random.uniform(16.0, 18.0)
    return ret;



def generate_longitude():
    ret = random.uniform(82.0, 84.0)
    return ret;



def generate_siteid():
    randnum = random.randint(1, 3)
    return randnum;


def generate_composition(randnum):
    if( randnum == 1 ):
        return "stony"
    elif( randnum == 2):
        return "iron"
    else:
        return "stony-iron"



data = {}
data['sites'] = []

for i in range(0,5):
 
    site_id = generate_siteid()
    data['sites'].append( {'site_id' : site_id,
                           'latitude' : generate_latitude(),
                           'longitude' : generate_longitude(),
                           'composition' : generate_composition(site_id)}
                        )


with open('sites.json', 'w') as out:
    json.dump(data, out, indent=2)

