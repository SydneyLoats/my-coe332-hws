from flask import Flask
import redis
import json

app = Flask(__name__)

app_data = {}



@app.route('/data', methods=['POST'])
def load_data():
    """
    Loads information from ML data sample.
    """
    rd = redis.Redis(host='172.17.0.12', port=6379)
	
    global app_data

    with open('ML_Data_Sample.json', 'r') as f:
        app_data = json.load(f)

    for d in app_data['meteorite_landings']:
        rd.set(d['id'], json.dumps(d))

    return f'Data loaded from file to dictionary.\n'



@app.route('/data', methods=['GET'])
def get_data():
    """
    Outputs the names in meteorite_landings.

    Returns:
        ret_list (json list): json list of meteorite landings
    """
    
    rd = redis.Redis(host='172.17.0.12', port=6379)

    ret_list = []
    for i in range(10001, 10301, 1):
        ret_list.append(json.loads(rd.get(i)))


    return json.dumps(ret_list, indent=2)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
