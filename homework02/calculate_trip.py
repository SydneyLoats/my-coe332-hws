import math
import json



def calc_sampletime(stringsample):
    if(stringsample == 'stony'):
        return 1
    elif(stringsample == 'iron'):
        return 2
    else:
        return 3


mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )


def calc_traveltime(lat1: float, long1: float, lat2: float, long2: float) -> float:
    dist = calc_gcd(lat1, long1, lat2, long2)
    return dist/10

def main():
    
    with open('sites.json', 'r') as f:
        sites_data = json.load(f)

    total_time_elapsed = 0;
    lat1 = 16.0
    long1 = 82.0
    lat2 = 0
    long2 = 0
    count = 0
    for i in sites_data['sites']:
        latitude_value = sites_data['sites'][count]['latitude']
        longitude_value = sites_data['sites'][count]['longitude']
        composition_value = sites_data['sites'][count]['composition']

        lat2 = latitude_value
        long2 = longitude_value

        leg = count +1
        traveltime = calc_traveltime(lat1, long1, lat2, long2)
        sampletime = calc_sampletime(composition_value)        

        total_time_elapsed = total_time_elapsed + traveltime

        count = count +1
        lat1 = latitude_value
        long1 = longitude_value


        print('leg = ' + str(leg)+ ', time to travel = ' + str(traveltime) + ' hr, time to sample = ' + str(sampletime) + ' hr' )

    print('number of legs = ' + str(leg) + ', total time elapsed = ' + str(total_time_elapsed) + ' hr')

main()
