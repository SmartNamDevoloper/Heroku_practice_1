import pickle
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
app = Flask(__name__)

bike_model = pickle.load(open("model","rb"))
@app.route('/')
def home():
    return render_template("Bike_share.html")
@app.route('/predict', methods=['POST'])
def predict():
    # cols = ['temp', 'season_spring', 'yr_2019', 'mnth_Sep', 'holiday_Yes',
    #         'weathersit_Misty', 'weathersit_Rainy']
    # temp =request.args["temp"]
    # spring = request.args["spring"]
    # year = request.args["year"]
    # month = request.args["month"]
    # holiday = request.args["holiday"]
    # misty = request.args["misty"]
    # rainy = request.args["rainy"]
    int_features = [x for x in request.form.values()]
    print("First", int_features)
    int_features.insert(0,1)
    # int_features = pd.Series(int_features)
    print(type(int_features))
    int_features = [float(x) for x in int_features]
    print(type(int_features))
    print("Second", int_features)
    final_features = [int_features]
    print("Third", final_features)
    pred = bike_model.predict(final_features)
    print(pred)
    output = "Prediction is "+str(pred)
    return str(output)


if __name__ =='__main__':
  app.debug=True
  app.run()











