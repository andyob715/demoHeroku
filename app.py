#IMPORT NECESSARY LIBRARIES
from flask import Flask, render_template, request
import pandas as pd 
import pickle

#IMPORT ALL THE THINGS
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.datasets import make_regression, make_swiss_roll
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# # SQLALCHEMY SETUP
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# import psycopg2

#os allows you to call in environment variables
# we will set the remote environment variables in heroku 
# from dotenv import load_dotenv
# import os 

# load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", 'POST'])
def index():
        #Line below will load your machine learning model
    Outcome = "Your Value Here!"
    
    if request.method == 'POST': 


        filename = 'static/pickle/pilot_forest_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        loaded_scaler = pickle.load(open('static/pickle/scaler.pkl', 'rb'))
    
        input_1=request.json.get("student_class_input")
        input_2=request.json.get("exampleDataList2")
        input_3=request.json.get("exampleDataList3")
        input_4=request.json.get("daysform")

        var1 = int(input_1)
        var2 = int(input_2)
        var3 = int(input_3)
        var4 = int(input_4)
        
        input_list = ["coursename", "start_month", "course_count", "e2e_course_days"]

        raw_user_input = pd.DataFrame([[var1,var2,var3,var4]],columns=input_list)

        scaled_user_input = loaded_scaler.transform(raw_user_input)
        Prediction = loaded_model.predict(scaled_user_input)
        # return Prediction
        return {"Prediction": Prediction}
        
    return render_template("index.html", Prediction=Outcome)

if __name__ == '__main__':
    app.run(debug=True)
