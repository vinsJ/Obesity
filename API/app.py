from flask import Flask, request, jsonify

from sklearn.preprocessing import LabelEncoder

import json
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('RF_model.sav', 'rb'))

@app.route('/api/predict', methods=['POST'])
def index():
    if request.method == 'POST':
        content = request.json

        #! Put the data into the right shape

        data = pd.read_json(content)
        
        #! Let's do the predictions
        predictions = model.predict(data)

        return json.dumps(list(predictions)), 200, {'ContentType':'application/json'}

@app.route('/', methods=['GET'])
def homepage():
    return 'This API was designed by Vincent DEBANDE and Ludovic CHEVALLIER'
    
if __name__ == '__main__':
    app.run('0.0.0.0', 42, True)
