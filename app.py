import numpy as np
from flask import Flask, request,render_template
from flask_cors import CORS
import os
import joblib
import pickle
import flask
import os
import urllib
from flask import jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json


app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

with open('finalpipeline.pkl', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('main.html')
@app.route("/predict", methods=['GET','POST'])
def predict():

    # Validate the request body contains JSON


        # Parse the JSON into a Python dictionary
        req = request.get_json()

        # Print the dictionary



        # Return a string along with an HTTP status code
        news=(req.get("text"))
        #return news
        pred = model.predict([news])
        return (jsonify(authenticity=pred[0]))

if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
